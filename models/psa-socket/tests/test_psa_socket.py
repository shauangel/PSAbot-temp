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
        client.emit('get_chat', {
            '_id':"000001",
            'user_id':'test_user2'
            })
        received = client.get_received()
        self.assertEqual(received[0]['name'], 'received_message')
        # self.assertEqual(received[0]['name'], 'test_user2')
        self.assertEqual(received[0]['args'][0], {"_id":"000001","tags":[{"tag_id":"00000","tag_name":"Python"}],"keywords":[],"question":"耶","time":{"$date":"2021-10-14T13:55:29.000Z"},"members":[{"user_id":"116287698501129823679","incognito":False},{"user_id":"4168365173258689","incognito":False}],"chat_logs":[{"user_id":"PSAbot","time":{"$date":"2021-10-14T13:55:29.000Z"},"type":"string","content":"等待回答者加入..."},{"user_id":"PSAbot","time":{"$date":"2021-10-14T13:57:44.000Z"},"type":"string","content":"本次共同討論的問題是「 耶」，可以開始討論了。討論結束後請發問者輸入「結束討論」完成本次討論。"},{"user_id":"116287698501129823679","time":{"$date":"2021-10-14T13:57:59.000Z"},"type":"string","content":"小小小可愛"},{"user_id":"4168365173258689","time":{"$date":"2021-10-14T13:58:05.000Z"},"type":"string","content":"小小小飛機"},{"user_id":"116287698501129823679","time":{"$date":"2021-10-14T13:58:10.000Z"},"type":"string","content":"開心開心"},{"user_id":"4168365173258689","time":{"$date":"2021-10-14T13:58:17.000Z"},"type":"string","content":"好累好累。"},{"user_id":"116287698501129823679","time":{"$date":"2021-10-14T13:58:26.000Z"},"type":"string","content":"結束討論"},{"user_id":"PSAbot","time":{"$date":"2021-10-14T13:58:26.000Z"},"type":"string","content":"請為「回答者」這次的回答評分（滿意/不滿意）。"},{"user_id":"116287698501129823679","time":{"$date":"2021-10-14T13:58:30.000Z"},"type":"string","content":"滿意"},{"user_id":"PSAbot","time":{"$date":"2021-10-14T13:58:31.000Z"},"type":"string","content":"請問你願意回報此問題嗎？（僅限提問者回覆）"},{"user_id":"116287698501129823679","time":{"$date":"2021-10-14T13:58:35.000Z"},"type":"string","content":"願意"}],"end_flag":True,"enabled":False})