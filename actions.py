# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

# class ActionHelloWorld(Action):

#     def name(self) -> Text:
#         return "action_hello_world"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#         dispatcher.utter_message(text="Hello World!")

#         return []



class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Hello World! i am Tapendra Baduwal from Nepal.")

        return []


""" Next we have to search different project according to there fields"""
class ActionSearchProjects(Action):

    def name(self) -> Text:
        return "action_about_projects"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        entities = tracker.latest_message["entities"]
        print(entities)

        for e in entities:
            if e["entity"] == "projects":
                name = e["value"]
            
            if name == "artificial intelligence":
                message = "At NIC, we are working on different AI based projects some of them are  Blindspot Detection,AI based Robot,Rasa Chatbot,AI based Rocket"
            if name == "agriculture":
                message = "At NIC, we are working on different agriculture based projects some of them are Black Soldier Fly,Monkey Repellent System,Ginger Drink,Sabji Kothi"
            if name == "healthcare":
                message = "At NIC, we are working on different healthcare based projects some of them are Baby Warmer,Oxygen Mini Plant"
            if name == "household":
                message = "At NIC, we are working on different household based projects some of them are Solar Water Heater,Incense Making Machine,Cooking Stove,Grass Cutter"



        dispatcher.utter_message(text=message)

        return []
