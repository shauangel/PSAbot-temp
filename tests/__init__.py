from flask_testing import TestCase
from flask import url_for
from main import create_app
from views.TextAnalyze import TextAnalyze
import json

#這邊是測試的基礎設置，先不要動
class SettingBase(TestCase):
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    def create_app(self):

        return create_app()
        
    def signin(self):
        if self.role != 'manager':
            response = self.client.post(url_for('login_api.facebook_sign_in'),
                                         follow_redirects=True,
                                        data=json.dumps({
                                            'id': self.user_id,
                                            'name': self.name
                                        }),content_type="application/json")
        else:
            response = self.client.post(url_for('login_api.password_sign_in'),
                                         follow_redirects=True,
                                        data=json.dumps({
                                            '_id': self.user_id,
                                            'password': self.password
                                        }),content_type="application/json")
        return response
        
    def logout(self):
        response = self.client.get(url_for('login_api.logout'))
        return response