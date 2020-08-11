# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/

from rasa_sdk import Action, Tracker
from typing import Any, Text, Dict, List
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
#from database_connectivity import DataRetrieve
import mysql.connector
#

#to retrieve event time using event name only
class ActionEvent(Action):
#
    def name(self) -> Text:
        return "action_event_time"
#
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        intent=tracker.latest_message['intent'].get('name')
        day=""
        time=""
        place=""
        for e in tracker.latest_message['entities']:
            if e['entity']=='day':
                day=e['value']
            if e['entity']=='time':
                time=e['value']
            if e['entity']=='place':
                place=e['value']   
            if e['entity']=='event_name':
                event_name=e['value']   


        if event_name=='chatbot':
            dispatcher.utter_message(text=f"Event on{ place} {day} {time} 12pm today at seminar hall".format(tracker.get_slot("place"),tracker.get_slot("day"),tracker.get_slot("time")))
        if event_name=='python':
            dispatcher.utter_message(text=f"Event on {place} {day} {time} 12pm today at lecture hall".format(tracker.get_slot("place"),tracker.get_slot("day"),tracker.get_slot("time")))
        if event_name=='regitration':
            dispatcher.utter_message(text=f"Registration on {place} {day} {time} 8am 2020-08-06 at auditorium".format(tracker.get_slot("place"),tracker.get_slot("day"),tracker.get_slot("time")))
        if event_name=='closing ceremony':
            dispatcher.utter_message(text=f"Ends on {place} {day} {time} 4:10pm 2020-08-07 at auditorium".format(tracker.get_slot("place"),tracker.get_slot("day"),tracker.get_slot("time")))
        if event_name=='keynote':
            dispatcher.utter_message(text=f"Event on {place} {day} {time}10am today at auditorium".format(tracker.get_slot("place"),tracker.get_slot("day"),tracker.get_slot("time")))
        if event_name=='artificial intelligence':
            dispatcher.utter_message(text=f"Event on {place} {day} {time} 5pm today at seminar hall".format(tracker.get_slot("place"),tracker.get_slot("day"),tracker.get_slot("time")))
        if event_name=='tango with django':
            dispatcher.utter_message(text=f"Event on {place} {day} {time}10:10am 2020-08-07 at seminar hall".format(tracker.get_slot("place"),tracker.get_slot("day"),tracker.get_slot("time")))

        return []

#to retrieve events based on relative time
class ActionEvent(Action):
#
    def name(self) -> Text:
        return "action_event_list"
#
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        intent=tracker.latest_message['intent'].get('name')
        day=""
        time=""
        place=""
        for e in tracker.latest_message['entities']:
            if e['entity']=='day':
                day=e['value']
            if e['entity']=='time':
                time=e['value']
            if e['entity']=='place':
                place=e['value']    
        
        dispatcher.utter_message(text=f"Events at {place} {day} {time} ".format(tracker.get_slot("place"),tracker.get_slot("day"),tracker.get_slot("time")))
        
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Password@123",
            database="sitebot" 
        )

        mycursor = mydb.cursor()
        sql="select * from Event where date='2020-08-06' and time < '16:10:00'"

        mycursor.execute(sql)

        records = mycursor.fetchall()

        print("\nPrinting each record events")
        for row in records:
            dispatcher.utter_message(row[1])
            dispatcher.utter_message(row[2])
            dispatcher.utter_message(row[3])
            dispatcher.utter_message(row[4])

        return []

#list the events on [tomorrow](day)
class ActionEvent(Action):
#
    def name(self) -> Text:
        return "action_event_list_tomorrow"
#
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        intent=tracker.latest_message['intent'].get('name')
        day=""
        time=""
        place=""
        for e in tracker.latest_message['entities']:
            if e['entity']=='day':
                day=e['value']
            if e['entity']=='time':
                time=e['value']
            if e['entity']=='place':
                place=e['value']    
        
        dispatcher.utter_message(text=f"Events at {place} {day} {time} ".format(tracker.get_slot("place"),tracker.get_slot("day"),tracker.get_slot("time")))
        
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Password@123",
            database="sitebot" 
        )

        mycursor = mydb.cursor()
        sql="select * from Event where date='2020-08-07'"

        mycursor.execute(sql)

        records = mycursor.fetchall()

        print("\nPrinting each record tomorrow")
        for row in records:
            dispatcher.utter_message(row[1])
            dispatcher.utter_message(row[2])
            dispatcher.utter_message(row[3])
            dispatcher.utter_message(row[4])

        return []

#What event is happening at place
class ActionEvent(Action):
#
    def name(self) -> Text:
        return "action_event_request_place"
#
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        intent=tracker.latest_message['intent'].get('name')
        day=""
        time=""
        place=""
        for e in tracker.latest_message['entities']:
            if e['entity']=='day':
                day=e['value']
            if e['entity']=='time':
                time=e['value']
            if e['entity']=='place':
                place=e['value']    
        
        dispatcher.utter_message(text=f"Events at {place} {day} {time} ".format(tracker.get_slot("place"),tracker.get_slot("day"),tracker.get_slot("time")))
        
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Password@123",
            database="sitebot" 
            )
        mycursor = mydb.cursor()
        if place=='lecture hall':

            sql="select * from Event where place='lecture hall'"
            mycursor.execute(sql)
            records = mycursor.fetchall()
            print("\nPrinting each record place")
            for row in records:
                dispatcher.utter_message(row[1])
                dispatcher.utter_message(row[2])
                dispatcher.utter_message(row[3])
                dispatcher.utter_message(row[4])

        if place=='seminar hall':

            sql="select * from Event where place='seminar hall'"
            mycursor.execute(sql)
            records = mycursor.fetchall()
            print("\nPrinting each record place")
            for row in records:
                dispatcher.utter_message(row[1])
                dispatcher.utter_message(row[2])
                dispatcher.utter_message(row[3])
                dispatcher.utter_message(row[4])   

        if place=='auditorium':

            sql="select * from Event where place='audi'"
            mycursor.execute(sql)
            records = mycursor.fetchall()
            print("\nPrinting each record place")
            for row in records:
                dispatcher.utter_message(row[1])
                dispatcher.utter_message(row[2])
                dispatcher.utter_message(row[3])
                dispatcher.utter_message(row[4])                             

            return []        


#What event is happening at [auditorium](place) [10am](time) [tomorrow](day)
class ActionEvent(Action):
#
    def name(self) -> Text:
        return "action_event_request_placetimeday"
#
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        intent=tracker.latest_message['intent'].get('name')
        day=""
        time=""
        place=""
        for e in tracker.latest_message['entities']:
            if e['entity']=='day':
                day=e['value']
            if e['entity']=='time':
                time=e['value']
            if e['entity']=='place':
                place=e['value']   
            if e['entity']=='event_name':
                event_name=e['value']   


        if place=='auditorium' and time=='10am' and day=='tomorrow':
            dispatcher.utter_message(text=f"Event on {place} {day} {time} is TANGO WITH DJANGO BY JAYSINH SHUKLA".format(tracker.get_slot("place"),tracker.get_slot("day"),tracker.get_slot("time")))
        if place=='lecture hall' and time=='2pm' and day=='tomorrow':
            dispatcher.utter_message(text=f"Event on {place} {day} {time} is CREATING IMAGE THUMBNAILS USING AWS LAMDA BY SIDRA EFFENDI".format(tracker.get_slot("place"),tracker.get_slot("day"),tracker.get_slot("time")))
        if place=='seminar hall' and time=='5pm' and day=='today':
            dispatcher.utter_message(text=f"Event on {place} {day} {time} is ARTIFICIAL INTELLIGENCE & PYTHON, OPENCV: L-INCUBATOR IIM".format(tracker.get_slot("place"),tracker.get_slot("day"),tracker.get_slot("time")))
        if place=='lecture hall' and time=='4pm' and day=='today':
            dispatcher.utter_message(text=f"Event on {place} {day} {time} is DEBUGGING: AN ART FOR SMART BY PUSHPLATA RANJAN".format(tracker.get_slot("place"),tracker.get_slot("day"),tracker.get_slot("time")))

        return []

#action_event_request_time only

class ActionEvent(Action):
#
    def name(self) -> Text:
        return "action_event_request_time"
#
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        intent=tracker.latest_message['intent'].get('name')
        day=""
        time=""
        place=""
        for e in tracker.latest_message['entities']:
            if e['entity']=='day':
                day=e['value']
            if e['entity']=='time':
                time=e['value']
            if e['entity']=='place':
                place=e['value']    
        
        dispatcher.utter_message(text=f"Events at {place} {day} {time} ".format(tracker.get_slot("place"),tracker.get_slot("day"),tracker.get_slot("time")))
        
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Password@123",
            database="sitebot" 
            )
        mycursor = mydb.cursor()
        if time=='5pm':

            sql="select * from Event where time='17:00:00'"
            mycursor.execute(sql)
            records = mycursor.fetchall()
            print("\nPrinting each record place")
            for row in records:
                dispatcher.utter_message(row[1])
                dispatcher.utter_message(row[2])
                dispatcher.utter_message(row[3])
                dispatcher.utter_message(row[4])

        if time=='9am':

            sql="select * from Event where time='09:00:00'"
            mycursor.execute(sql)
            records = mycursor.fetchall()
            print("\nPrinting each record place")
            for row in records:
                dispatcher.utter_message(row[1])
                dispatcher.utter_message(row[2])
                dispatcher.utter_message(row[3])
                dispatcher.utter_message(row[4])   

        if time=='10am':

            sql="select * from Event where time='10:00:00'"
            mycursor.execute(sql)
            records = mycursor.fetchall()
            print("\nPrinting each record place")
            for row in records:
                dispatcher.utter_message(row[1])
                dispatcher.utter_message(row[2])
                dispatcher.utter_message(row[3])
                dispatcher.utter_message(row[4])           
        
        if time=='now':

            sql="select * from Event where time > current_time - interval 30 minute and time < current_time + interval 30 minute and date='2020-08-06'"
            mycursor.execute(sql)
            records = mycursor.fetchall()
            print("\nPrinting each record place")
            for row in records:
                dispatcher.utter_message(row[1])
                dispatcher.utter_message(row[2])
                dispatcher.utter_message(row[3])
                dispatcher.utter_message(row[4]) 

        if time=='11am' or time=='12pm':
            dispatcher.utter_message(text=f"Sorry..! no events found")

            return [] 


#action_event_request_timeday only

class ActionEvent(Action):
#
    def name(self) -> Text:
        return "action_event_request_timeday"
#
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        intent=tracker.latest_message['intent'].get('name')
        day=""
        time=""
        place=""
        for e in tracker.latest_message['entities']:
            if e['entity']=='day':
                day=e['value']
            if e['entity']=='time':
                time=e['value']
            if e['entity']=='place':
                place=e['value']    
        
        dispatcher.utter_message(text=f"Events at {place} {day} {time} ".format(tracker.get_slot("place"),tracker.get_slot("day"),tracker.get_slot("time")))
        
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Password@123",
            database="sitebot" 
            )
        mycursor = mydb.cursor()
        if time=='1pm' and day=='today':

            sql="select * from Event where date='2020-08-06' and time='13:00:00'"
            mycursor.execute(sql)
            records = mycursor.fetchall()
            print("\nPrinting each record place")
            for row in records:
                dispatcher.utter_message(row[1])
                #dispatcher.utter_message(row[2])
                dispatcher.utter_message(row[3])
                #dispatcher.utter_message(row[4])

        if time=='9am' and day=='tomorrow':

            sql="select * from Event where date='2020-08-07' and time='09:00:00'"
            mycursor.execute(sql)
            records = mycursor.fetchall()
            print("\nPrinting each record place")
            for row in records:
                dispatcher.utter_message(row[1])
                #dispatcher.utter_message(row[2])
                dispatcher.utter_message(row[3])
                #dispatcher.utter_message(row[4])   

        if time=='10am' and day=='today':

            sql="select * from Event where date='2020-08-06' and time='10:00:00'"
            mycursor.execute(sql)
            records = mycursor.fetchall()
            print("\nPrinting each record place")
            for row in records:
                dispatcher.utter_message(row[1])
                #dispatcher.utter_message(row[2])
                dispatcher.utter_message(row[3])
                #dispatcher.utter_message(row[4])           

        if time=='2pm' and day=='tomorrow':

            sql="select * from Event where date='2020-08-07' and time='14:00:00'"
            mycursor.execute(sql)
            records = mycursor.fetchall()
            print("\nPrinting each record place")
            for row in records:
                dispatcher.utter_message(row[1])
                #dispatcher.utter_message(row[2])
                dispatcher.utter_message(row[3])
                #dispatcher.utter_message(row[4]) 

        if time=='same time' and day=='tomorrow':

            sql="select * from Event where time > current_time - interval 30 minute and time < current_time + interval 30 minute and date='2020-08-07'"
            mycursor.execute(sql)
            records = mycursor.fetchall()
            print("\nPrinting each record place")
            for row in records:
                dispatcher.utter_message(row[1])
                dispatcher.utter_message(row[2])
                dispatcher.utter_message(row[3])
                dispatcher.utter_message(row[4])                 

            return []            