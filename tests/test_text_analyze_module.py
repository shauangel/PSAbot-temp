from . import SettingBase
from flask import url_for
import json
# ======================================== #
from views.TextAnalyze import TextAnalyze
# ======================================== #

class CheckTextAnalyzeModule(SettingBase):
    def test_user_login_4(self):
        self.user_id = 'PSABOTMANAGER'
        self.password = '456'
        self.role = 'manager'
        response = self.signin()
        self.assertEqual(response.json, {'_id': 'invalid.','role':''})