from . import SettingBase
from flask import url_for
import json

class CheckTagMaintenanceModule(SettingBase):
    def test_query_all_languages(self):
        response = self.client.get(url_for('tag_api.query_all_languages'),follow_redirects=True)
        with open('data/tag-maintenance-module/query_all_languages_output.json', 'r', encoding = 'utf-8') as file:
            output = json.load(file)
        self.assertEqual(response.json,output)
        
    def test_query_all_offspring_tag(self):
        response = self.client.get(url_for('tag_api.query_all_offspring_tag') + "?tag_id=00000",follow_redirects=True)
        with open('data/tag-maintenance-module/query_all_offspring_tag_output.json', 'r', encoding = 'utf-8') as file:
            output = json.load(file)
        self.assertEqual(response.json,output)
        
    def test_query_tag_child(self):
        response = self.client.get(url_for('tag_api.query_tag_child') + "?tag_id=00000",follow_redirects=True)
        with open('data/tag-maintenance-module/query_tag_child_output.json', 'r', encoding = 'utf-8') as file:
            output = json.load(file)
        self.assertEqual(response.json,output)
        
    def test_query_tag_name(self):
        response = self.client.get(url_for('tag_api.query_tag_name') + "?tag_id=00000",follow_redirects=True)
        with open('data/tag-maintenance-module/query_tag_name_output.json', 'r', encoding = 'utf-8') as file:
            output = json.load(file)
        self.assertEqual(response.json,output)
        
    def test_query_user_tag(self):
        response = self.client.get(url_for('tag_api.query_user_tag') + "?user_id=4257031614316957",follow_redirects=True)
        with open('data/tag-maintenance-module/query_user_tag_output.json', 'r', encoding = 'utf-8') as file:
            output = json.load(file)
        self.assertEqual(response.json,output)