# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging
import requests
import json

from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet

logger = logging.getLogger(__name__)


'''
# Constants set up for API
ZOMATO_API_KEY = 'YOUR_API_KEY_HERE'
API_URL = 'https://developers.zomato.com/api/v2.1/'
HEADERS = {
'User-agent': 'curl/7.43.0', 
'Accept': 'application/json',
'user_key': ZOMATO_API_KEY
}
'''
API_URL = 'http://127.0.0.1:5000/'
HEADERS = {
'User-agent': 'curl/7.43.0', 
'Accept': 'application/json'
}
class ActionDressSearch(Action):
	def name(self):
	# define the name of the action which can then be included in training stories
		return 'action_dress_search'
	'''
	def parse_search(self, restaurants):
		data = {
			'name' : [],
			'cuisines' : [],
			'address' : [],
			'rating' : [],
			'cost' : [],
		}

		for rest in restaurants:
			rt = rest['restaurant']
			data['name'].append(rt['name'])
			data['cuisines'].append(rt['cuisines'])
			data['address'].append(rt['location']['address'])
			data['rating'].append(rt['user_rating']['aggregate_rating'])
			data['cost'].append(str(rt['average_cost_for_two']))

		return data
	'''
	'''
	def get_location(self, location):
		# fetch location id
		req_url = API_URL + 'locations?query=' + location
		
		res = requests.get(req_url, headers=HEADERS)

		# default delhi lat and long
		latitude = 28.625789
		longitude = 77.210276

		if res.status_code == 200:
			latitude = res.json()['location_suggestions'][0]['latitude']
			longitude = res.json()['location_suggestions'][0]['longitude']

		return str(latitude), str(longitude)
	'''
	def run(self, dispatcher, tracker, domain):
		# what your action should do
		occasion = tracker.get_slot('occasion') or 'wedding'
		bodyshape = tracker.get_slot('bodyshape') or 'hourglass'

		dispatcher.utter_message(occasion+bodyshape)

		#latitude, longitude = self.get_location(location)

		req_url = API_URL + 'cust_sugg/' + 'red/' + occasion + '/' + bodyshape

		res = requests.get(req_url, headers=HEADERS)

		if res.status_code == 200:
			custom_recommendation = res.json()['custom_recommendation']
			out_greet_msg = '*Here are top results for {} for {} occasions*'.format(bodyshape, occasion)
			dispatcher.utter_message(out_greet_msg)
			print(len(custom_recommendation))
			# prepare the output to be sent out
			out_st=""

			if len(custom_recommendation) > 0:
				for dress in (custom_recommendation):
					out_st=out_st+dress+"\n"
					
				dispatcher.utter_message(out_st)
			else:
				dispatcher.utter_message('No Results found :( Please try again!')
		else:
			dispatcher.utter_message('FAILED.')
		# dispatcher.utter_message(output)
		return []
