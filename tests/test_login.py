from . import SettingBase
from flask import url_for

class CheckLoginAPI(SettingBase):
    
    def test_user_login_1(self):
        self.user_id = '123456789'
        self.name = '測試使用者'
        self.role = 'google_user'
        response = self.signin()
        self.assertEqual(response.status_code, 200)
        
    def test_user_login_2(self):
        self.user_id = '4257031614316957'
        self.name = '我很聰明'
        self.role = 'facebook_user'
        response = self.signin()
        self.assertEqual(response.status_code, 200)
        
    def test_user_login_3(self):
        self.user_id = 'PSABOTMANAGER'
        self.password = '123'
        self.role = 'manager'
        response = self.signin()
        self.assertEqual(response.json, {'_id': 'PSABOTMANAGER','role':'manager'})
        
    def test_user_login_4(self):
        self.user_id = 'PSABOTMANAGER'
        self.password = '456'
        self.role = 'manager'
        response = self.signin()
        self.assertEqual(response.json, {'_id': 'invalid.','role':''})
        
    def test_logout(self):
        self.user_id = 'PSABOTMANAGER'
        self.password = '123'
        self.role = 'manager'
        response = self.signin()
        response = self.client.get(url_for('login_api.logout'), follow_redirects=True)
        self.assertEqual(response.json, {"msg" : "user PSABOTMANAGER is logged out."})
        