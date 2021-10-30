import json
import unittest
from main import socketio,app

def connect_client(user_id):
    client = socketio.test_client(app, query_string='?user_id=' + user_id)
    return client
    
class TestSocketIO(unittest.TestCase):
    def connect_client(self,user_id):
        client = socketio.test_client(app, query_string='?user_id=' + user_id)
        return client
    def test_connect(self):
        client = socketio.test_client(app, query_string='?user_id=test_user')
        # client.get_received()[0]['args'] == 'test_user has connected.'
        self.assertEqual(client.get_received()[0]['args'][0],'test_user has connected.')
        
    def test_emit(self):
        client = connect_client('test_user2')
        client.get_received()
        client.emit('my custom event', {'a': 'b'})
        received = client.get_received()
        self.assertEqual(received[0]['name'], 'my custom event')
        self.assertEqual(received[0]['args'][0]['a'], 'b')