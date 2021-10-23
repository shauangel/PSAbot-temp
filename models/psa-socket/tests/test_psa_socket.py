import json
import unittest
from main import socketio,app

class TestSocketIO(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_connect(self):
        client = socketio.test_client(app, auth={'foo': 'bar'})
        print(client.get_received())
        self.assertEqual('1','1')
        