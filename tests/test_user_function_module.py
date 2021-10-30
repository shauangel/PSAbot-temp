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
        json.dump(response.data,file)
    with open('data/' + data_folder + '/' + function_name + '_output.json', 'r', encoding = 'utf-8') as file:
        output = json.load(file)
    
    self.assertEqual(response.json,output)

class CheckUserFunctionModule(SettingBase):
    @pytest.mark.order1
    def test_query_user_profile(self):
        with open('data/user-function-module/query_user_profile_input.json', 'r', encoding = 'utf-8') as file:
            text_input = json.load(file)
        with open('data/user-function-module/query_user_profile_output.json', 'r', encoding = 'utf-8') as file:
            output = json.load(file)
        response = self.client.post(url_for('user_api.query_user_profile') ,
                                    data = json.dumps(text_input), content_type="application/json")
        self.assertEqual(response.json,output)
    @pytest.mark.order2
    def test_query_user_skill(self):
        with open('data/user-function-module/query_user_skill_input.json', 'r', encoding = 'utf-8') as file:
            text_input = json.load(file)
        response = self.client.post(url_for('user_api.query_user_skill') ,
                                    data = json.dumps(text_input), content_type="application/json")
        with open('data/user-function-module/query_user_skill_output.json', 'w', encoding = 'utf-8') as file:
            output = json.dump(response.json,file)
        with open('data/user-function-module/query_user_skill_output.json', 'r', encoding = 'utf-8') as file:
            output = json.load(file)
        
        self.assertEqual(response.json,output)
    @pytest.mark.order3
    def test_update_user_profile(self):
        with open('data/user-function-module/update_user_profile_input.json', 'r', encoding = 'utf-8') as file:
            text_input = json.load(file)
        with open('data/user-function-module/update_user_profile_output.json', 'r', encoding = 'utf-8') as file:
            output = json.load(file)
        response = self.client.post(url_for('user_api.update_user_profile') ,
                                    data = json.dumps(text_input), content_type="application/json")
        self.assertEqual(response.json,output)
    @pytest.mark.order4
    def test_update_user_interest(self):
        with open('data/user-function-module/update_user_interest_input.json', 'r', encoding = 'utf-8') as file:
            text_input = json.load(file)
        with open('data/user-function-module/update_user_interest_output.json', 'r', encoding = 'utf-8') as file:
            output = json.load(file)
        response = self.client.post(url_for('user_api.update_user_interest') ,
                                    data = json.dumps(text_input), content_type="application/json")
        self.assertEqual(response.json,output)
    @pytest.mark.order5
    def test_update_user_score(self):
        with open('data/user-function-module/update_user_score_input.json', 'r', encoding = 'utf-8') as file:
            text_input = json.load(file)
        with open('data/user-function-module/update_user_score_output.json', 'r', encoding = 'utf-8') as file:
            output = json.load(file)
        response = self.client.post(url_for('user_api.update_user_score') ,
                                    data = json.dumps(text_input), content_type="application/json")
        self.assertEqual(response.json,output)
    @pytest.mark.order6
    def test_query_user_post_list(self):
        with open('data/user-function-module/query_user_post_list_input.json', 'r', encoding = 'utf-8') as file:
            text_input = json.load(file)
        with open('data/user-function-module/query_user_post_list_output.json', 'r', encoding = 'utf-8') as file:
            output = json.load(file)
        response = self.client.post(url_for('user_api.query_user_post_list') ,
                                    data = json.dumps(text_input), content_type="application/json")
        self.assertEqual(response.json,output)
    @pytest.mark.order7
    def test_query_user_response_list(self):
        with open('data/user-function-module/query_user_response_list_input.json', 'r', encoding = 'utf-8') as file:
            text_input = json.load(file)
        with open('data/user-function-module/query_user_response_list_output.json', 'r', encoding = 'utf-8') as file:
            output = json.load(file)
        response = self.client.post(url_for('user_api.query_user_response_list') ,
                                    data = json.dumps(text_input), content_type="application/json")
        self.assertEqual(response.json,output)
    @pytest.mark.order8
    def test_query_inner_post_list(self):
        write_testing(self,'post_api','user-function-module','query_inner_post_list')
    @pytest.mark.order9
    def test_query_inner_post_list_by_title(self):
        write_testing(self,'post_api','user-function-module','query_inner_post_list_by_title')
    @pytest.mark.order10
    def test_query_inner_post_list_by_tag(self):
        write_testing(self,'post_api','user-function-module','query_inner_post_list_by_tag')
    @pytest.mark.order11
    def test_query_inner_post(self):
        post_testing(self,'post_api','user-function-module','query_inner_post')
    @pytest.mark.order12
    def test_insert_inner_post(self):
        post_testing(self,'post_api','user-function-module','insert_inner_post')
    @pytest.mark.order13
    def test_update_inner_post(self):
        post_testing(self,'post_api','user-function-module','update_inner_post')
    @pytest.mark.order14
    def test_insert_inner_post_response(self):
        post_testing(self,'post_api','user-function-module','insert_inner_post_response')
    @pytest.mark.order15
    def test_update_inner_post_response(self):
        post_testing(self,'post_api','user-function-module','update_inner_post_response')
    @pytest.mark.order16
    def test_like_inner_post(self):
        post_testing(self,'post_api','user-function-module','like_inner_post')
    @pytest.mark.order17
    def test_dislike_inner_post(self):
        post_testing(self,'post_api','user-function-module','dislike_inner_post')
    @pytest.mark.order18
    def test_like_faq_post(self):
        post_testing(self,'faq_api','user-function-module','like_faq_post')
    @pytest.mark.order19
    def test_dislike_faq_post(self):
        post_testing(self,'faq_api','user-function-module','dislike_faq_post')
    # @pytest.mark.order20
    # def test_save_user_img(self):
    # @pytest.mark.order21
    # def test_read_image(self):