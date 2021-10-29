from . import SettingBase
from flask import url_for
import json


class CheckTextAnalyzeModule(SettingBase):
    def test_insert_cache(self):
        with open('data/search-module/insert_cache_input.json', 'r', encoding = 'utf-8') as file:
            text_input = json.load(file)
        with open('data/search-module/insert_cache_output.json', 'r', encoding = 'utf-8') as file:
            output = json.load(file)
        response = self.client.post(url_for('outersearch_cache_api.insert_cache') ,
                                    data = json.dumps(text_input), content_type="application/json")
        self.assertEqual(response.json,output)
    
    def test_keywords(self):
        self.maxDiff = None
        response = self.client.get(url_for('rasa_api.keywords')+ "?sender_id=116287698501129823679&keywords=keywords_for_guided_QA,flask",follow_redirects=True)
        with open('data/search-module/keywords_output.json', 'r', encoding = 'utf-8') as file:
            output = json.load(file)
        self.assertEqual(response.json,output)
        
    def test_query_cache_by_id(self):
        with open('data/search-module/query_cache_by_id_input.json', 'r', encoding = 'utf-8') as file:
            text_input = json.load(file)
        with open('data/search-module/query_cache_by_id_output.json', 'r', encoding = 'utf-8') as file:
            output = json.load(file)
        response = self.client.post(url_for('outersearch_cache_api.query_cache_by_id') ,
                                    data = json.dumps(text_input), content_type="application/json")
        self.assertEqual(response.json,output)
        
    def test_query_hot_post(self):
        response = self.client.get(url_for('post_api.query_hot_post'),follow_redirects=True)
        with open('data/search-module/query_hot_post_output.json', 'r', encoding = 'utf-8') as file:
            output = json.load(file)
        self.assertEqual(response.json,output)
        
    def test_query_inner_search(self):
        with open('data/search-module/query_inner_search_input.json', 'r', encoding = 'utf-8') as file:
            text_input = json.load(file)
        with open('data/search-module/query_inner_search_output.json', 'r', encoding = 'utf-8') as file:
            output = json.load(file)
        response = self.client.post(url_for('post_api.query_inner_search') ,
                                    data = json.dumps(text_input), content_type="application/json")
        self.assertEqual(response.json,output)
        
    