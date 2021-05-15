# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionHelloWorld(Action):
    def name(self) -> Text:
        return "ActionHelloWorld"

    def run(self, dispatcher, tracker, domain) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="hello test")
        return []

class exchange(Action):
    # return 要放 action的名稱 「一定要一模一樣」
    def name(self) -> Text:
        return "exchange"

    def run(self, dispatcher, tracker, domain) -> List[Dict[Text, Any]]:
        NT = int(tracker.get_slot("NT"))
        NT = NT*0.035
        dispatcher.utter_message(
            text="美金是"+str(NT),
            json_message = {"res_after": NT, "res_before": tracker.get_slot("NT")}
        )
        return []
        
class ask_question_or_message(Action):
    # return 要放 action的名稱 「一定要一模一樣」
    def name(self) -> Text:
        return "ask_question_or_message"

    def run(self, dispatcher, tracker, domain) -> List[Dict[Text, Any]]:
        chosen = tracker.get_slot("function")
        if "錯誤訊息" in chosen:
            reply = "請貼上您的錯誤訊息"
        elif "引導式" in chosen:
            reply = "請描述您遇到的問題"
        else:
            reply = "你的function抓不到"
        
        dispatcher.utter_message(text=reply)
        return []
