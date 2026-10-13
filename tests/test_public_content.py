import importlib.util,unittest
from pathlib import Path
spec=importlib.util.spec_from_file_location('public_content',Path(__file__).resolve().parents[1]/'tools/check_public_content.py')
guard=importlib.util.module_from_spec(spec);spec.loader.exec_module(guard)
class PublicContent(unittest.TestCase):
    def test_public_source_identity_is_allowed(self):
        self.assertEqual(guard.violations('ENGINE1011 source SHA-256: `'+('a'*64)+'`; src/xrGame/example.cpp'),[])
    def test_private_path_and_log_names_are_rejected(self):
        name='xray_'+'fixture'+'(20000101-010203).log'
        win='C:'+chr(92)+'Users'+chr(92)+'fixture'
        scratch='/'.join(['','workspace','scratch','fixture'])
        for text in [name,win,scratch]:self.assertTrue(guard.violations(text))
    def test_private_fingerprint_is_rejected(self):
        self.assertTrue(guard.violations('| PRIVATE-LOG | `'+('a'*64)+'` |'))
        self.assertTrue(guard.violations('Reported executable SHA-256: `'+('a'*64)+'`'))
