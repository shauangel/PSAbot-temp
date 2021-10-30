from . import SettingBase
from flask import url_for
import json
import pytest

def post_testing(self,api_name,data_folder,function_name):
    with open('data/' + data_folder + '/' + function_name + '_input.json', 'r', encoding = 'utf-8') as file:
            text_input = json.load(file)
    with open('data/' + data_folder + '/' + function_name + '_output.json', 'r', encoding = 'utf-8') as file:
        output = json.load(file)
    response = self.client.post(url_for(api_name +'.' + function_name) ,
                                data = json.dumps(text_input), content_type="application/json")
    self.assertEqual(response.json,output)

def write_testing(self,api_name,data_folder,function_name):
    with open('data/' + data_folder + '/' + function_name + '_input.json', 'r', encoding = 'utf-8') as file:
            text_input = json.load(file)
    response = self.client.post(url_for(api_name +'.' + function_name) ,
                                data = json.dumps(text_input), content_type="application/json")
    with open('data/' + data_folder + '/' + function_name + '_output.json', 'w', encoding = 'utf-8') as file:
        json.dump(response.json,file)
    with open('data/' + data_folder + '/' + function_name + '_output.json', 'r', encoding = 'utf-8') as file:
        output = json.load(file)
    self.assertEqual(response.json,output)
    
class CheckRealtimeDiscussionModule(SettingBase):
    @pytest.mark.order1
    def test_discussion_recommand_user(self):
        write_testing(self, 'discussion_api', 'realtime-discussion-module', 'discussion_recommand_user')
    @pytest.mark.order2
    def test_query_chat(self):
        post_testing(self,'discussion_api', 'realtime-discussion-module', 'query_chat')
    @pytest.mark.order3
    def test_query_chat_list(self):
        write_testing(self,'discussion_api', 'realtime-discussion-module', 'query_chat_list')
    @pytest.mark.order4
    def test_check_discussion_is_full(self):
        post_testing(self,'discussion_api', 'realtime-discussion-module', 'check_discussion_is_full')
    @pytest.mark.order5
    def test_check_member_is_incognito(self):
        post_testing(self,'discussion_api', 'realtime-discussion-module', 'check_member_is_incognito')
    @pytest.mark.order6
    def test_query_chat_tag(self):
        post_testing(self,'discussion_api', 'realtime-discussion-module', 'query_chat_tag')
    @pytest.mark.order7
    def test_change_chat_state(self):
        post_testing(self,'discussion_api', 'realtime-discussion-module', 'change_chat_state')
    @pytest.mark.order8
    def test_create_psabot_chat(self):
        post_testing(self,'discussion_api', 'realtime-discussion-module', 'create_psabot_chat')
    @pytest.mark.order9
    def test_insert_psabot_message(self):
        post_testing(self,'discussion_api', 'realtime-discussion-module', 'insert_psabot_message')
    @pytest.mark.order10
    def test_remove_chat(self):
        post_testing(self,'discussion_api', 'realtime-discussion-module', 'insert_psabot_message')