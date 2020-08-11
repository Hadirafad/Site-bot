## story_001
* greet
     - utter_ask_howcanhelp
* event_request_time{"time": "now"}
     - slot{"time": "now"}
     - action_event_request_time
* thanks
     - utter_welcome

## story_002
* greet
     - utter_ask_howcanhelp
* event_request_placetimeday{"place": "lecture hall", "time": "4pm", "day": "today"}
	 - slot{"place": "lecture hall", "time": "4pm", "day": "today"}
	 - action_event_request_placetimeday 
* goodbye
	 - utter_goodbye 

## story_003
* greet
     - utter_ask_howcanhelp
* event_request_timeday{"time": "10am", "day": "today"}
	 - slot{"time": "10am", "day": "today"}
	 - action_event_request_timeday 
* goodbye
	 - utter_goodbye

## story_004
* greet
     - utter_ask_howcanhelp
* event_request_placetimeday{"place": "auditorium", "day": "tomorrow", "time": "10am"}
	 - slot{"place": "auditorium", "day": "tomorrow", "time": "10am"}
	 - action_event_request_placetimeday
* thanks
     - utter_welcome	
* goodbye
	 - utter_goodbye 

## story_005
* greet
     - utter_ask_howcanhelp
* event_request_placetimeday{"place": "lecture hall", "time": "2pm", "day": "tomorrow"}
	 - slot{"place": "lecture hall", "time": "2pm", "day": "tomorrow"}
	 - action_event_request_placetimeday 
* thanks
     - utter_welcome

## story_006
* greet
     - utter_ask_howcanhelp
* event_request_placetimeday{"place": "seminar hall", "time": "5pm", "day": "today"}
	 - slot{"place": "seminar hall", "time": "5pm", "day": "today"}
	 - action_event_request_placetimeday 
* thanks
     - utter_welcome

## story_007
* greet
     - utter_ask_howcanhelp
* event_request_timeday{"time": "1pm", "day": "today"}
	 - slot{"time": "1pm", "day": "today"}
	 - action_event_request_timeday
* thanks
     - utter_welcome

## story_007
* greet
     - utter_ask_howcanhelp
* event_request_timeday{"time": "9am", "day": "tomorrow"}
	 - slot{"time": "9am", "day": "tomorrow"}
	 - action_event_request_timeday
* thanks
     - utter_welcome

## story_008
* greet
     - utter_ask_howcanhelp
* event_request_time{"time": "5pm"}
	 - slot{"time": "5pm"}
	 - action_event_request_time 
* thanks
     - utter_welcome

## story_009
* greet
     - utter_ask_howcanhelp
* event_request_time{"time": "9am"}
	 - slot{"time": "9am"}
	 - action_event_request_time
* thanks
     - utter_welcome

## story_010
* greet
     - utter_ask_howcanhelp
* event_list{"relative_time": "before", "time": "12pm"}
	 - slot{"relative_time": "before", "time": "12pm"}
	 - action_event_list 
* thanks
     - utter_welcome

## story_011
* greet
     - utter_ask_howcanhelp
* event_list{"relative_time": "after", "time": "5pm"}
	 - slot{"relative_time": "after", "time": "5pm"}
	 - action_event_list 
* thanks
     - utter_welcome

## story_012
* greet
     - utter_ask_howcanhelp
* event_time{"event_name": "chatbot"}
	 - slot{"event_name": "chatbot"}
	 - action_event_time 
* thanks
     - utter_welcome

## story_013
* greet
     - utter_ask_howcanhelp
* event_time{"event_name": "python"}
	 - slot{"event_name": "python"}
	 - action_event_time
* thanks
     - utter_welcome

## story_014
* greet
     - utter_ask_howcanhelp
* event_request_timeday{"time": "2pm", "day": "tomorrow"}
	 - slot{"time": "2pm", "day": "tomorrow"}
	 - action_event_request_timeday 
* thanks
     - utter_welcome    

## story_015
* greet
     - utter_ask_howcanhelp
* event_request_place{"place": "lecture hall"}
	 - slot{"place": "lecture hall"}
	 - action_event_request_place
* thanks
     - utter_welcome

## story_016
* greet
     - utter_ask_howcanhelp
* event_list_tomorrow{"day": "tomorrow"}
	 - slot{"day": "tomorrow"}
	 - action_event_list_tomorrow
* thanks
     - utter_welcome

## story_017
* greet
     - utter_ask_howcanhelp
* event_request_place{"place": "seminar hall"}
	 - slot{"place": "seminar hall"}
	 - action_event_request_place
* thanks
     - utter_welcome  

## story_018
* greet
     - utter_ask_howcanhelp
* event_request_place{"place": "auditorium"}
	 - slot{"place": "auditorium"}
	 - action_event_request_place
* thanks
     - utter_welcome          


## story_019
* greet
     - utter_ask_howcanhelp
* event_request_time{"time": "10am"}
	 - slot{"time": "10am"}
	 - action_event_request_time
* thanks
     - utter_welcome

## story_020
* greet
     - utter_ask_howcanhelp
* event_request_time{"time": "10am"}
	 - slot{"time": "11am"}
	 - action_event_request_time
* thanks
     - utter_welcome

## story_021
* greet
     - utter_ask_howcanhelp
* event_request_time{"time": "12pm"}
	 - slot{"time": "12pm"}
	 - action_event_request_time
* thanks
     - utter_welcome          


## story_022
* greet
     - utter_ask_howcanhelp
* event_time{"event_name": "registration"}
	 - slot{"event_name": "registration"}
	 - action_event_time
* thanks
     - utter_welcome


## story_023
* greet
     - utter_ask_howcanhelp
* event_time{"event_name": "closing ceremony"}
	 - slot{"event_name": "closing ceremony"}
	 - action_event_time
* thanks
     - utter_welcome


## story_024
* greet
     - utter_ask_howcanhelp
* event_time{"event_name": "keynote"}
	 - slot{"event_name": "keynote"}
	 - action_event_time
* thanks
     - utter_welcome


## story_025
* greet
     - utter_ask_howcanhelp
* event_time{"event_name": "artificial intelligence"}
	 - slot{"event_name": "artificial intelligence"}
	 - action_event_time
* thanks
     - utter_welcome


## story_026
* greet
     - utter_ask_howcanhelp
* event_time{"event_name": "tango with django"}
	 - slot{"event_name": "tango with django"}
	 - action_event_time
* thanks
     - utter_welcome


## story_027
* greet
     - utter_ask_howcanhelp
* event_request_timeday{"time": "same time", "day": "tomorrow"}
	 - slot{"time": "same time", "day": "tomorrow"}
	 - action_event_request_timeday 
* goodbye
	 - utter_goodbye
