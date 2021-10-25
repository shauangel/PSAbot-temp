from . import SettingBase
from flask import url_for
import json

class CheckChatbotModule(SettingBase):
    def test_discussion_recommand_user(self):
        response = self.client.post(url_for('discussion_api.discussion_recommand_user') ,
                                    data = json.dumps({"tags" : ["00000"]}), content_type="application/json")
        with open('data/realtime-discussion-module/discussion_recommand_user_output.json', 'r', encoding = 'utf-8') as file:
            output = json.load(file)
        self.assertEqual(response.json,output)