# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


import datetime as dt
from typing import Any, Text, Dict, List
from rasa_sdk import Tracker, FormValidationAction, Action
from rasa_sdk.events import EventType
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict
from rasa_sdk.events import SlotSet

class ValidateAddContactForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_add_contact_form"
    def validate_contact_name(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        
        if slot_value is None:    
            user_input = tracker.latest_message.get('text')
            dispatcher.utter_message(f"Okay! You want to create a contact named {user_input}.")
            return {"contact_name": user_input}
        else:
            dispatcher.utter_message(text=f"Okay! You want to create a contact named {slot_value}.")
            return {"contact_name": slot_value}


    def validate_company_name(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:

        if slot_value is None:    
            user_input = tracker.latest_message.get('text')
            dispatcher.utter_message(f"Okay! You want to create a contact named {user_input}.")
            return {"contact_name": user_input}
        else:
            dispatcher.utter_message(text=f"Okay! You want to create a contact named {slot_value}.")
            return {"contact_name": slot_value}

    def validate_role(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:

        if slot_value is None:    
            user_input = tracker.latest_message.get('text')
            dispatcher.utter_message(f"Okay! You want to set the role to {user_input}.")
            return {"role": user_input}
        else:
            dispatcher.utter_message(text=f"Okay! You want to set the role to {slot_value}.")
            return {"role": slot_value}
    
    def validate_contact_num(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        if slot_value is None:
            user_input = tracker.latest_message.get('text')
            dispatcher.utter_message(f"Okay! You want to set contact number to {user_input}.")
            # Set the slot using the SlotSet event
            return [SlotSet("contact_num", user_input)]
        else:
            dispatcher.utter_message(text=f"Okay! You want to set contact number to {slot_value}.")
            return [SlotSet("contact_num", slot_value)]

    def validate_contact_email(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:

        if slot_value is None:    
            user_input = tracker.latest_message.get('text')
            dispatcher.utter_message(f"Okay! You want to set the contact email to {user_input}.")
            return {"contact_email": user_input}
        else:
            dispatcher.utter_message(text=f"Okay! You want to set the contact email to {slot_value}.")
            return {"contact_email": slot_value}

    def validate_street(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:

        if slot_value is None:    
            user_input = tracker.latest_message.get('text')
            dispatcher.utter_message(f"Okay! You want to set the street to {user_input}.")
            return {"street": user_input}
        else:
            dispatcher.utter_message(text=f"Okay! You want to set the street to {slot_value}.")
            return {"street": slot_value}


    def validate_city(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:

        if slot_value is None:    
            user_input = tracker.latest_message.get('text')
            dispatcher.utter_message(f"Okay! You want to set the city to {user_input}.")
            return {"city": user_input}
        else:
            dispatcher.utter_message(text=f"Okay! You want to set the city to {slot_value}.")
            return {"city": slot_value}

    def validate_country(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        if slot_value is None:    
            user_input = tracker.latest_message.get('text')
            dispatcher.utter_message(f"Okay! You want to set the country to {user_input}.")
            return {"country": user_input}
        else:
            dispatcher.utter_message(text=f"Okay! You want to set the country to {slot_value}.")
            return {"country": slot_value}


    def validate_contact_type(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:

        if slot_value is None:    
            user_input = tracker.latest_message.get('text')
            dispatcher.utter_message(f"Okay! You want to set the contact type to {user_input}.")
            return {"contact_type": user_input}
        else:
            dispatcher.utter_message(text=f"Okay! You want to set the contact type to {slot_value}.")
            return {"contact_type": slot_value}



# Shows Current time


class ActionShowTime(Action):

    def name(self) -> Text:
        return "action_show_time"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text=f"{dt.datetime.now()}")

        return []


#   Prototype on how add contact would work in future 

# class ActionAddContact(Action):
#     def name(self) -> Text:
#         return "action_add_contact"

#     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#         contact_name = "Hamid"
#         company_name = "Techflo"
#         role = "Developer"
#         phone_no = "+123456789"
#         contact_email = "hamid@example.com"
#         street_address = "E11"
#         city = "Islamabad"
#         country = "Pakistan"
        
#         response = f"The contact '{contact_name}' from '{company_name}' has been added successfully!\n"
#         response += f"Contact Name: {contact_name}\n"
#         response += f"Company Name: {company_name}\n"
#         response += f"Role: {role}\n"
#         response += f"Phone Number: {phone_no}\n"
#         response += f"Contact Email: {contact_email}\n"
#         response += f"Street Address: {street_address}\n"
#         response += f"City: {city}\n"
#         response += f"Country: {country}\n"
        
#         response += "Contact Added successfully!"
#         dispatcher.utter_message(text=response)
#         return []


