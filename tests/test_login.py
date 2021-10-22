from . import SettingBase
from flask import url_for
class CheckLoginAPI(SettingBase):
    def facebook_sign_in(self):
        self.user_id = '4257031614316957'
        self.name = '謝宛蓉'
        response = self.signin()
        print(response.data)
        self.assertEqual(response.status_code, 200)