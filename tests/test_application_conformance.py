"""Executable positive, negative, and falsification checks for application parity."""
import copy
import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

PATH = Path(__file__).resolve().parents[1] / 'tools' / 'application_conformance.py'
spec = importlib.util.spec_from_file_location('application_conformance', PATH)
ac = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ac)


def fixture():
    model = {
        'schema_version': ac.VERSION, 'target': 'Permitted example booking UI',
        'scope': 'create and reject double booking', 'initial_state': 'FREE',
        'sources': [{'id': 'REF1', 'kind': 'OBSERVED', 'locator': 'fixture://reference-session/1'},
                    {'id': 'OWNER1', 'kind': 'OWNER_APPROVAL', 'locator': 'fixture://owner-decision/1'}],
        'requirements': [
            {'id': 'R1', 'scope': 'REQUIRED', 'description': 'Book one available slot', 'source_refs': ['REF1']},
            {'id': 'R2', 'scope': 'REQUIRED', 'description': 'Reject unavailable slot', 'source_refs': ['REF1']},
            {'id': 'R3', 'scope': 'OPTIONAL', 'description': 'Display a help page', 'source_refs': ['REF1']},
            {'id': 'R4', 'scope': 'EXCLUDED_BY_OWNER', 'description': 'Partner marketplace', 'source_refs': ['OWNER1']}],
        'states': [{'id': 'FREE', 'description': 'Slot free'}, {'id': 'BOOKED', 'description': 'Slot booked'}],
        'transitions': [
            {'id': 'T1', 'requirement_id': 'R1', 'from_state': 'FREE', 'action': 'book',
             'to_state': 'BOOKED', 'expected_output': {'result': 'confirmed'}, 'source_refs': ['REF1']},
            {'id': 'T2', 'requirement_id': 'R2', 'from_state': 'BOOKED', 'action': 'book',
             'to_state': 'BOOKED', 'expected_output': {'result': 'rejected'}, 'source_refs': ['REF1']}]
    }
    runs = [
        {'id': 'EXEC1', 'transition_id': 'T1', 'from_state': 'FREE', 'action': 'book',
         'to_state': 'BOOKED', 'output': {'result': 'confirmed'}},
        {'id': 'EXEC2', 'transition_id': 'T2', 'from_state': 'BOOKED', 'action': 'book',
         'to_state': 'BOOKED', 'output': {'result': 'rejected'}}]
    observations = {'schema_version': ac.RUN_VERSION, 'model_sha256': ac.digest(model), 'runs': runs}
    receipts = {'schema_version': ac.RECEIPT_VERSION, 'receipts': [
        {'id': r['id'], 'sha256': ac.digest(ac.execution_payload(r, ac.digest(model)))} for r in runs]}
    return model, observations, receipts


class ApplicationConformance(unittest.TestCase):
    def test_valid_required_behavior_and_exclusion(self):
        model, observations, receipts = fixture()
        result = ac.evaluate(model, observations, receipts)
        self.assertEqual(result['verdict'], 'PASS')
        self.assertEqual((result['required_verified'], result['required_total']), (2, 2))
        self.assertEqual(result['requirements']['R4']['status'], 'EXCLUDED_BY_OWNER')
        self.assertEqual(result['completeness'], 'DECLARED_OBSERVED_SCOPE_ONLY')

    def test_missing_required_transition_is_not_ignored(self):
        model, observations, receipts = fixture()
        model['requirements'].append({'id': 'R5', 'scope': 'REQUIRED', 'description': 'Cancel', 'source_refs': ['REF1']})
        observations['model_sha256'] = ac.digest(model)
        for record, run in zip(receipts['receipts'], observations['runs']):
            record['sha256'] = ac.digest(ac.execution_payload(run, ac.digest(model)))
        result = ac.evaluate(model, observations, receipts)
        self.assertEqual((result['required_verified'], result['required_total']), (2, 3))
        self.assertEqual(result['requirements']['R5']['status'], 'UNVERIFIED')
        self.assertEqual(result['verdict'], 'BLOCKED')

    def test_skipped_run_does_not_change_required_denominator(self):
        model, observations, receipts = fixture()
        observations['runs'] = observations['runs'][:1]
        self.assertEqual(ac.evaluate(model, observations, receipts)['required_verified'], 1)
        self.assertEqual(ac.evaluate(model, observations, receipts)['required_total'], 2)

    def test_behavior_mismatch_overrides_self_report(self):
        model, observations, receipts = fixture()
        observations['runs'][1]['output'] = {'result': 'confirmed'}
        receipts['receipts'][1]['sha256'] = ac.digest(ac.execution_payload(observations['runs'][1], ac.digest(model)))
        outcome = ac.evaluate(model, observations, receipts)
        self.assertEqual(outcome['transitions']['T2']['status'], 'FAILED')
        self.assertEqual(outcome['verdict'], 'BLOCKED')

    def test_missing_receipt_cannot_be_verified(self):
        model, observations, receipts = fixture()
        receipts['receipts'].pop()
        outcome = ac.evaluate(model, observations, receipts)
        self.assertEqual(outcome['transitions']['T2']['reason'], 'UNTRUSTED_EXECUTION')
        self.assertEqual(outcome['required_verified'], 1)

    def test_forged_or_corrupt_receipt_blocks(self):
        model, observations, receipts = fixture()
        observations['runs'][0]['output'] = {'result': 'confirmed', 'injected': True}
        outcome = ac.evaluate(model, observations, receipts)
        self.assertEqual(outcome['transitions']['T1']['status'], 'UNVERIFIED')
        self.assertEqual(outcome['verdict'], 'BLOCKED')

    def test_source_documentation_does_not_prove_reference_parity(self):
        model, observations, receipts = fixture()
        model['sources'][0]['kind'] = 'DOCUMENTED'
        observations['model_sha256'] = ac.digest(model)
        outcome = ac.evaluate(model, observations, receipts)
        self.assertEqual(outcome['transitions']['T1']['reason'], 'REFERENCE_NOT_OBSERVED')
        self.assertEqual(outcome['verdict'], 'BLOCKED')

    def test_inferred_backend_not_valid_oracle(self):
        model, observations, receipts = fixture()
        model['sources'][0]['kind'] = 'INFERRED'
        observations['model_sha256'] = ac.digest(model)
        self.assertEqual(ac.evaluate(model, observations, receipts)['required_verified'], 0)

    def test_unapproved_optional_exclusion_invalid(self):
        model, _, _ = fixture()
        model['requirements'][-1]['source_refs'] = ['REF1']
        with self.assertRaises(ac.ContractError):
            ac.validate_model(model)

    def test_agent_cannot_hide_required_feature_by_exclusion(self):
        model, observations, receipts = fixture()
        model['requirements'][1]['scope'] = 'EXCLUDED_BY_OWNER'
        with self.assertRaises(ac.ContractError):
            ac.validate_model(model)

    def test_unknown_source_reference_invalid(self):
        model, _, _ = fixture()
        model['transitions'][0]['source_refs'] = ['NOWHERE']
        with self.assertRaises(ac.ContractError):
            ac.validate_model(model)

    def test_unreachable_transition_invalid(self):
        model, _, _ = fixture()
        model['states'].append({'id': 'ORPHAN', 'description': 'Not reachable'})
        model['transitions'][1]['from_state'] = 'ORPHAN'
        with self.assertRaises(ac.ContractError):
            ac.validate_model(model)

    def test_duplicate_identifiers_invalid(self):
        model, _, _ = fixture()
        model['transitions'].append(copy.deepcopy(model['transitions'][0]))
        with self.assertRaises(ac.ContractError):
            ac.validate_model(model)

    def test_stale_model_hash_invalid(self):
        model, observations, receipts = fixture()
        model['scope'] = 'changed without replacing observations'
        with self.assertRaises(ac.ContractError):
            ac.evaluate(model, observations, receipts)

    def test_executor_cannot_self_assert_pass(self):
        model, observations, receipts = fixture()
        observations['runs'][0]['verdict'] = 'PASS'
        with self.assertRaises(ac.ContractError):
            ac.evaluate(model, observations, receipts)

    def test_untrusted_contradictory_run_prevents_cherrypicking(self):
        model, observations, receipts = fixture()
        observations['runs'].append({'id': 'EXEC3', 'transition_id': 'T1', 'from_state': 'FREE',
                                     'action': 'book', 'to_state': 'FREE', 'output': {'result': 'error'}})
        outcome = ac.evaluate(model, observations, receipts)
        self.assertEqual(outcome['transitions']['T1']['status'], 'UNVERIFIED')

    def test_cli_outputs_result_and_exit_codes(self):
        model, observations, receipts = fixture()
        with tempfile.TemporaryDirectory() as temp:
            paths = [Path(temp) / name for name in ('model.json', 'runs.json', 'trusted.json')]
            for path, obj in zip(paths, (model, observations, receipts)):
                path.write_text(json.dumps(obj), encoding='utf-8')
            cmd = [sys.executable, str(PATH), '--model', str(paths[0]), '--observations', str(paths[1]),
                   '--trusted-receipts', str(paths[2])]
            success = subprocess.run(cmd, capture_output=True, text=True)
            self.assertEqual(success.returncode, 0, success.stdout)
            self.assertEqual(json.loads(success.stdout)['verdict'], 'PASS')
            paths[2].write_text(json.dumps({'schema_version': ac.RECEIPT_VERSION, 'receipts': []}), encoding='utf-8')
            blocked = subprocess.run(cmd, capture_output=True, text=True)
            self.assertEqual(blocked.returncode, 1)
            self.assertEqual(json.loads(blocked.stdout)['verdict'], 'BLOCKED')
            paths[0].write_text('{', encoding='utf-8')
            invalid = subprocess.run(cmd, capture_output=True, text=True)
            self.assertEqual(invalid.returncode, 2)
            self.assertEqual(json.loads(invalid.stdout)['verdict'], 'INVALID')


if __name__ == '__main__':
    unittest.main()
