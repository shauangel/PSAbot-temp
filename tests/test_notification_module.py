from . import SettingBase
from flask import url_for
import json
import pytest

class CheckNotificationModule(SettingBase):
    @pytest.mark.order1
    def test_check_notification_content(self):
        response = self.client.get(url_for('notification_api.check_notification_content') + 
                                   "?user_id=116287698501129823679&page=0",follow_redirects=True)
        with open('data/notification-module/check_notification_content_output.json', 'r', encoding = 'utf-8') as file:
            output = json.load(file)
        self.assertEqual(response.json,output)
        
    @pytest.mark.order2
    def test_add_post_notification(self):
        response = self.client.get(url_for('notification_api.add_post_notification') +
                                   "?user_id=4028146397302662&replier_id=116287698501129823679&post_id=000015",follow_redirects=True)
        with open('data/notification-module/add_post_notification_output.json', 'r', encoding = 'utf-8') as file:
            output = json.load(file)
        self.assertEqual(response.json,output)
        
    @pytest.mark.order3   
    def test_delete_notification(self):
        response = self.client.get(url_for('notification_api.delete_notification') +
                                   "?post_id=000059",follow_redirects=True)
        with open('data/notification-module/delete_notification_output.json', 'r', encoding = 'utf-8') as file:
            output = json.load(file)
        self.assertEqual(response.json,output)
        
    @pytest.mark.order4
    def test_add_discussion_invitation_notification(self):
        with open('data/notification-module/add_discussion_invitation_notification_input.json', 'r', encoding = 'utf-8') as file:
            text_input = json.load(file)
        with open('data/notification-module/add_discussion_invitation_notification_output.json', 'r', encoding = 'utf-8') as file:
            output = json.load(file)
        response = self.client.post(url_for('notification_api.add_discussion_invitation_notification') ,
                                    data = json.dumps(text_input), content_type="application/json")
        self.assertEqual(response.json,output)
        
    @pytest.mark.order5
    def test_disable_discussion_invatation(self):
        response = self.client.get(url_for('notification_api.delete_notification') +
                                   "?user_id=116287698501129823679&id=45",follow_redirects=True)
        with open('data/notification-module/disable_discussion_invatation_output.json', 'r', encoding = 'utf-8') as file:
            output = json.load(file)
        self.assertEqual(response.json,output)
        
    @pytest.mark.order6 
    def test_check_new_notification(self):
        response = self.client.get(url_for('notification_api.check_new_notification') +
                                   "?user_id=116287698501129823679",follow_redirects=True)
        with open('data/notification-module/check_new_notification_output.json', 'r', encoding = 'utf-8') as file:
            output = json.load(file)
        self.assertEqual(response.json,output)
        
        
    def test_set_notification_new(self):
        with open('data/notification-module/set_notification_new_input.json', 'r', encoding = 'utf-8') as file:
            text_input = json.load(file)
        with open('data/notification-module/set_notification_new_output.json', 'r', encoding = 'utf-8') as file:
            output = json.load(file)
        response = self.client.post(url_for('notification_api.set_notification_new') ,
                                    data = json.dumps(text_input), content_type="application/json")
        self.assertEqual(response.json,output)
        
        
    def test_set_notification_check(self):
        response = self.client.get(url_for('notification_api.set_notification_check') +
                                   "?user_id=116287698501129823679&id=49",follow_redirects=True)
        with open('data/notification-module/set_notification_check_output.json', 'r', encoding = 'utf-8') as file:
            output = json.load(file)
        self.assertEqual(response.json,output)