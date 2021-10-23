from . import SettingBase
from flask import url_for
import json

class CheckChatbotModule(SettingBase):
    def test_session_start(self):
        self.user_id = '116287698501129823679'
        self.name = '慈慈Cihcih'
        self.role = 'facebook_user'
        self.signin()
        response = self.client.get(url_for('rasa_api.session_start') 
                                   + "?sender_id=116287698501129823679", follow_redirects=True)
        with open('/data/chatbot-module/session_start_output.json', 'r', encoding = 'utf-8') as file:
            output = json.load(file)
        self.assertEqual(response.json,output)
        
    def test_welcome(self):
        self.user_id = '116287698501129823679'
        self.name = '慈慈Cihcih'
        self.role = 'facebook_user'
        self.signin()
        response = self.client.get(url_for('rasa_api.welcome') 
                                   + "?sender_id=116287698501129823679", follow_redirects=True)
        with open('/data/chatbot-module/welcome_output.json', 'r', encoding = 'utf-8') as file:
            output = json.load(file)
        self.assertEqual(response.json,output)
        
    def test_base_flow_rasa(self):
        self.user_id = '116287698501129823679'
        self.name = '慈慈Cihcih'
        self.role = 'facebook_user'
        self.signin()
        response = self.client.get(url_for('base_flow_rasa_api.base_flow_rasa') 
                                   + "?message=%E5%BC%95%E5%B0%8E%E5%BC%8F%E5%95%8F%E7%AD%94&sender_id=116287698501129823679", follow_redirects=True)
        with open('/data/chatbot-module/base_flow_rasa_output.json', 'r', encoding = 'utf-8') as file:
            output = json.load(file)
        self.assertEqual(response.json,output)
        
        
    
