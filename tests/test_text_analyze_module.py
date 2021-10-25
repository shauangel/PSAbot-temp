from . import SettingBase
from flask import url_for
import json
# ======================================== #
from views.TextAnalyze import TextAnalyze
# ======================================== #

class CheckTextAnalyzeModule(SettingBase):
    def test_call_method(self):
        textAnalyzer = TextAnalyze()
        with open('data/text-analyze-module/test_content_pre_process_input.json', 'r', encoding = 'utf-8') as file:
            text_input = json.load(file)
        
        self.assertEqual(textAnalyzer.contentPreProcess(text_input['text'])[0],'1')