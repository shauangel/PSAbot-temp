from . import SettingBase
from flask import url_for
import json
# ======================================== #
from views.TextAnalyze import TextAnalyze
# ======================================== #

class CheckTextAnalyzeModule(SettingBase):
    def test_call_method(self):
        textAnalyzer = TextAnalyze()
        textAnalyzer.contentPreProcess('I will use this sentence to test the Text Analyze Module.')[0]
        self.assertEqual('1','1')