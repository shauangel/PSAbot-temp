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
    
class CheckManagerFunctionModule(SettingBase):
    @pytest.mark.order1
    def test_delete_inner_post_response(self):
        post_testing(self,'post_api','manager-function-module','delete_inner_post_response')
    @pytest.mark.order2
    def test_delete_inner_post(self):
        post_testing(self,'post_api','manager-function-module','delete_inner_post')
    @pytest.mark.order3
    def test_query_faq_update(self):
        post_testing(self,'faq_api','manager-function-module','query_faq_update')
    @pytest.mark.order4
    def test_adjust_faq_update(self):
        post_testing(self,'faq_api','manager-function-module','adjust_faq_update')
    @pytest.mark.order5
    def test_query_faq_post(self):
        post_testing(self,'faq_api','manager-function-module','adjust_faq_update')
    @pytest.mark.order6
    def test_query_faq_list(self):
        write_testing(self,'faq_api','manager-function-module','query_faq_list')
    @pytest.mark.order7
    def test_query_faq_list_by_string(self):
        write_testing(self,'faq_api','manager-function-module','query_faq_list_by_string')
    @pytest.mark.order8
    def test_query_faq_list_by_tag(self):
        write_testing(self,'faq_api','manager-function-module','query_faq_list_by_tag')
    @pytest.mark.order9
    def test_insert_faq_post(self):
        post_testing(self,'faq_api','manager-function-module','insert_faq_post')
    @pytest.mark.order10
    def test_update_faq_post(self):
        post_testing(self,'faq_api','manager-function-module','update_faq_post')
    @pytest.mark.order11
    def test_insert_faq_answer(self):
        post_testing(self,'faq_api','manager-function-module','insert_faq_answer')
    @pytest.mark.order12
    def test_update_faq_answer(self):
        post_testing(self,'faq_api','manager-function-module','update_faq_answer')
    @pytest.mark.order13
    def test_delete_faq_answer(self):
        post_testing(self,'faq_api','manager-function-module','delete_faq_answer')
    @pytest.mark.order14
    def test_delete_faq_post(self):
        post_testing(self,'faq_api','manager-function-module','delete_faq_post')