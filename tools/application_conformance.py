#!/usr/bin/env python3
"""Deterministic, scoped application-behavior conformance gate (stdlib only).

Inputs are observations, not model judgements. Only harness receipts supplied
by the host outside the agent's writable workspace can attest executions.
"""
import argparse
import hashlib
import json
import re
import sys
from pathlib import Path

VERSION = 'spari.application.behavior/1'
RUN_VERSION = 'spari.application.runs/1'
RECEIPT_VERSION = 'spari.application.receipts/1'
ID = re.compile(r'^[A-Za-z][A-Za-z0-9_.-]{0,63}$')
HEX = re.compile(r'^[a-f0-9]{64}$')


class ContractError(ValueError):
    pass


def fail(message):
    raise ContractError(message)


def object_fields(value, required, allowed, path):
    if not isinstance(value, dict):
        fail(path + ': expected object')
    missing = set(required) - value.keys()
    excess = value.keys() - set(allowed)
    if missing or excess:
        fail('%s: missing=%s unexpected=%s' % (path, sorted(missing), sorted(excess)))


def identifier(value, path):
    if not isinstance(value, str) or not ID.fullmatch(value):
        fail(path + ': invalid identifier')
    return value


def nonempty(value, path):
    if not isinstance(value, str) or not value.strip():
        fail(path + ': nonempty string required')
    return value


def array(value, path):
    if not isinstance(value, list):
        fail(path + ': array required')
    return value


def canonical(value):
    return json.dumps(value, sort_keys=True, ensure_ascii=False, separators=(',', ':'), allow_nan=False).encode('utf-8')


def digest(value):
    return hashlib.sha256(canonical(value)).hexdigest()


def unique(items, field, path):
    found = {}
    for index, item in enumerate(items):
        identifier(item.get(field), '%s[%d].%s' % (path, index, field))
        if item[field] in found:
            fail(path + ': duplicate ' + item[field])
        found[item[field]] = item
    return found


def validate_model(model):
    object_fields(model, ['schema_version', 'target', 'scope', 'initial_state', 'sources', 'requirements', 'states', 'transitions'],
                  ['schema_version', 'target', 'scope', 'initial_state', 'sources', 'requirements', 'states', 'transitions'], 'model')
    if model['schema_version'] != VERSION:
        fail('model: unsupported schema_version')
    nonempty(model['target'], 'model.target')
    nonempty(model['scope'], 'model.scope')
    for i, source in enumerate(array(model['sources'], 'sources')):
        object_fields(source, ['id', 'kind', 'locator'], ['id', 'kind', 'locator'], 'sources[%d]' % i)
        if source['kind'] not in ('OBSERVED', 'DOCUMENTED', 'INFERRED', 'OWNER_APPROVAL'):
            fail('sources[%d].kind: invalid' % i)
        nonempty(source['locator'], 'source.locator')
    sources = unique(model['sources'], 'id', 'sources')
    for i, req in enumerate(array(model['requirements'], 'requirements')):
        object_fields(req, ['id', 'scope', 'description', 'source_refs'],
                      ['id', 'scope', 'description', 'source_refs'], 'requirements[%d]' % i)
        nonempty(req['description'], 'requirement.description')
        if req['scope'] not in ('REQUIRED', 'OPTIONAL', 'EXCLUDED_BY_OWNER'):
            fail('requirements[%d].scope: invalid' % i)
        refs = array(req['source_refs'], 'requirement.source_refs')
        if not refs or any(identifier(v, 'requirement.source_ref') not in sources for v in refs):
            fail('requirements[%d]: ungrounded or unknown source' % i)
        if req['scope'] == 'EXCLUDED_BY_OWNER' and not any(sources[s]['kind'] == 'OWNER_APPROVAL' for s in refs):
            fail('requirements[%d]: exclusion requires owner approval evidence' % i)
        if req['scope'] != 'EXCLUDED_BY_OWNER' and any(sources[s]['kind'] == 'OWNER_APPROVAL' for s in refs):
            fail('requirements[%d]: approval is not feature evidence' % i)
    requirements = unique(model['requirements'], 'id', 'requirements')
    if not requirements:
        fail('model: requirements cannot be empty')
    for i, state in enumerate(array(model['states'], 'states')):
        object_fields(state, ['id', 'description'], ['id', 'description'], 'states[%d]' % i)
        nonempty(state['description'], 'state.description')
    states = unique(model['states'], 'id', 'states')
    if identifier(model['initial_state'], 'initial_state') not in states:
        fail('model: initial state not declared')
    for i, tr in enumerate(array(model['transitions'], 'transitions')):
        path = 'transitions[%d]' % i
        object_fields(tr, ['id', 'requirement_id', 'from_state', 'action', 'to_state', 'expected_output', 'source_refs'],
                      ['id', 'requirement_id', 'from_state', 'action', 'to_state', 'expected_output', 'source_refs'], path)
        if identifier(tr['requirement_id'], path + '.requirement_id') not in requirements:
            fail(path + ': unknown requirement')
        if requirements[tr['requirement_id']]['scope'] == 'EXCLUDED_BY_OWNER':
            fail(path + ': excluded scope cannot have required test transitions')
        if tr['from_state'] not in states or tr['to_state'] not in states:
            fail(path + ': unknown state')
        nonempty(tr['action'], path + '.action')
        refs = array(tr['source_refs'], path + '.source_refs')
        if not refs or any(identifier(v, path + '.source_ref') not in sources for v in refs):
            fail(path + ': ungrounded or unknown source')
        canonical(tr['expected_output'])
    transitions = unique(model['transitions'], 'id', 'transitions')
    reached = {model['initial_state']}
    while True:
        extended = reached | {t['to_state'] for t in transitions.values() if t['from_state'] in reached}
        if extended == reached:
            break
        reached = extended
    if any(t['from_state'] not in reached for t in transitions.values()):
        fail('model: unreachable transition')
    return sources, requirements, transitions


def execution_payload(run, model_sha256):
    payload = {k: run[k] for k in ('transition_id', 'from_state', 'action', 'to_state', 'output')}
    payload['model_sha256'] = model_sha256
    return payload


def validate_runs(doc, expected_hash):
    object_fields(doc, ['schema_version', 'model_sha256', 'runs'], ['schema_version', 'model_sha256', 'runs'], 'observations')
    if doc['schema_version'] != RUN_VERSION or doc['model_sha256'] != expected_hash:
        fail('observations: schema or model SHA mismatch')
    for i, run in enumerate(array(doc['runs'], 'observations.runs')):
        object_fields(run, ['id', 'transition_id', 'from_state', 'action', 'to_state', 'output'],
                      ['id', 'transition_id', 'from_state', 'action', 'to_state', 'output'], 'runs[%d]' % i)
        for k in ('transition_id', 'from_state', 'to_state'):
            identifier(run[k], 'runs[%d].%s' % (i, k))
        nonempty(run['action'], 'run.action')
        canonical(run['output'])
    return unique(doc['runs'], 'id', 'runs')


def validate_receipts(doc):
    object_fields(doc, ['schema_version', 'receipts'], ['schema_version', 'receipts'], 'receipts')
    if doc['schema_version'] != RECEIPT_VERSION:
        fail('receipts: wrong schema')
    for i, rec in enumerate(array(doc['receipts'], 'receipts.receipts')):
        object_fields(rec, ['id', 'sha256'], ['id', 'sha256'], 'receipts[%d]' % i)
        if not isinstance(rec['sha256'], str) or not HEX.fullmatch(rec['sha256']):
            fail('receipts[%d]: invalid hash' % i)
    return unique(doc['receipts'], 'id', 'receipts')


def evaluate(model, observation_doc, trusted_receipts):
    sources, requirements, transitions = validate_model(model)
    runs = validate_runs(observation_doc, digest(model))
    receipts = validate_receipts(trusted_receipts)
    if any(run['transition_id'] not in transitions for run in runs.values()):
        fail('observations: unknown transition_id')
    results = {}
    for tid, tr in transitions.items():
        candidates = [r for r in runs.values() if r['transition_id'] == tid]
        observed = any(sources[x]['kind'] == 'OBSERVED' for x in tr['source_refs'])
        result = 'UNVERIFIED'
        reason = 'REFERENCE_NOT_OBSERVED' if not observed else 'NO_ATTESTED_RUN'
        if observed and candidates:
            if any(r['id'] not in receipts or receipts[r['id']]['sha256'] != digest(execution_payload(r, digest(model))) for r in candidates):
                reason = 'UNTRUSTED_EXECUTION'
            elif any((r['from_state'] != tr['from_state'] or r['action'] != tr['action'] or
                      r['to_state'] != tr['to_state'] or canonical(r['output']) != canonical(tr['expected_output'])) for r in candidates):
                result, reason = 'FAILED', 'BEHAVIOR_MISMATCH'
            else:
                result, reason = 'VERIFIED', 'ATTESTED_BEHAVIOR_MATCH'
        results[tid] = {'requirement_id': tr['requirement_id'], 'status': result, 'reason': reason}
    requirements_result = {}
    for rid, req in requirements.items():
        if req['scope'] == 'EXCLUDED_BY_OWNER':
            status = 'EXCLUDED_BY_OWNER'
        else:
            relevant = [results[t] for t, tr in transitions.items() if tr['requirement_id'] == rid]
            if any(r['status'] == 'FAILED' for r in relevant):
                status = 'FAILED'
            elif relevant and all(r['status'] == 'VERIFIED' for r in relevant):
                status = 'VERIFIED'
            else:
                status = 'UNVERIFIED'
        requirements_result[rid] = {'scope': req['scope'], 'status': status}
    required = [r for r in requirements_result.values() if r['scope'] == 'REQUIRED']
    completed = sum(r['status'] == 'VERIFIED' for r in required)
    t_verified = sum(r['status'] == 'VERIFIED' for r in results.values())
    return {
        'model_sha256': digest(model), 'verdict': 'PASS' if required and completed == len(required) else 'BLOCKED',
        'completeness': 'DECLARED_OBSERVED_SCOPE_ONLY',
        'required_verified': completed, 'required_total': len(required),
        'transitions_verified': t_verified, 'transitions_total': len(results),
        'requirements': requirements_result, 'transitions': results,
    }


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--model', required=True)
    p.add_argument('--observations', required=True)
    p.add_argument('--trusted-receipts', required=True,
                   help='Host-controlled evidence; never read from an agent-writable directory')
    args = p.parse_args(argv)
    try:
        model, observations, receipts = [json.loads(Path(x).read_text(encoding='utf-8')) for x in
                                         (args.model, args.observations, args.trusted_receipts)]
        result = evaluate(model, observations, receipts)
        print(json.dumps(result, sort_keys=True, indent=2, ensure_ascii=False))
        return 0 if result['verdict'] == 'PASS' else 1
    except (ContractError, ValueError, OSError, TypeError) as exc:
        print(json.dumps({'verdict': 'INVALID', 'error': str(exc)}, ensure_ascii=False))
        return 2


if __name__ == '__main__':
    sys.exit(main())
