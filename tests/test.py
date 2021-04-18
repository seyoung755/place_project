import unittest
from app import create_app

class CIExampleTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app
        self.app.config['WTF_CSRF_ENABLED'] = False
        self.app = self.app.test_client ()

    def test_index(self):
        rv = self.app.get('/')
        assert 'Hello ,Python!' in rv.data.decode('utf8')