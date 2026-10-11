"""Regression checks for documentation validation; no game runtime required."""
import importlib.util
from pathlib import Path
import shutil
import tempfile
import unittest

REPO=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('checker',REPO/'tools/check_repository.py')
checker=importlib.util.module_from_spec(spec)
spec.loader.exec_module(checker)

class RepositoryChecks(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.temp=tempfile.TemporaryDirectory()
        cls.root=Path(cls.temp.name)/'repo'
        shutil.copytree(REPO,cls.root,ignore=shutil.ignore_patterns('__pycache__'))
        cls.version=(cls.root/'VERSION').read_text().strip()
    @classmethod
    def tearDownClass(cls):
        cls.temp.cleanup()
    def tearDown(self):
        for name in ['fixture.md','fixture.csv']:(self.root/name).unlink(missing_ok=True)
    def fixture(self,body,title='# Fixture',version=None):
        version=version or self.version
        (self.root/'fixture.md').write_text(title+f'\n\n> ADR document set: **v{version}**.\n\n'+body)
        return checker.check(self.root)['errors']
    def test_current_repository(self):
        self.assertEqual(checker.check(self.root)['errors'],[])
    def test_missing_target(self):
        self.assertTrue(any('missing target' in x for x in self.fixture('[bad](missing.md)')))
    def test_missing_anchor(self):
        self.assertTrue(any('missing anchor' in x for x in self.fixture('[bad](README.md#missing-anchor)')))
    def test_escape(self):
        self.assertTrue(any('escapes repository' in x for x in self.fixture('[bad](../escape.md)')))
    def test_stale_version(self):
        self.assertTrue(any('inconsistent document-set version' in x for x in self.fixture('',version='0.0.0')))
    def test_obsolete_forwarding(self):
        self.assertTrue(any('obsolete forwarding' in x for x in self.fixture('',title='# Moved: obsolete')))
    def test_malformed_csv(self):
        (self.root/'fixture.csv').write_text('one,two\nthree\n')
        self.assertTrue(any('CSV row width' in x for x in checker.check(self.root)['errors']))

if __name__=='__main__':unittest.main()
