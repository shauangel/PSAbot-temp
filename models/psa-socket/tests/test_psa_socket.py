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
        client = socketio.test_client(app, query_string='?user_id=test_user')
        # client.get_received()[0]['args'] == 'test_user has connected.'
        self.assertEqual(client.get_received()[0]['args'][0],'test_user has connected.')
        