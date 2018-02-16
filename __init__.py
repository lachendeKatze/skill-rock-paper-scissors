# Copyright 2016 Mycroft AI, Inc.
#
# This file is part of Mycroft Core.
#
# Mycroft Core is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Mycroft Core is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Mycroft Core.  If not, see <http://www.gnu.org/licenses/>.

# Mycroft libraries
from os.path import dirname
from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger

# clarifai libraries
from clarifai import rest
from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage

#required libraries
import json
import picamera
from time import sleep
from random import *

__author__ = 'GregV', '@lachendeKatze'

LOGGER = getLogger(__name__)

class RockPaperScissorsSkill(MycroftSkill):
    def __init__(self):
        super(RockPaperScissorsSkill, self).__init__(name="RockPaperScissorsSkill")
        self.gameChoices = ['rock','paper','scissors']

    def initialize(self):
        self.load_data_files(dirname(__file__))
        self.clarifai_app = ClarifaiApp(api_key=self.settings["api_key"])
        self.rpsModel = self.clarifai_app.models.get('rockpaperscissors')
	self.register_intent_file('rps.intent',self.handle_rps)

    def handle_rps(self,message):
        rpsRound = []
        rpsRound.append(self.mycroftChoice())
        self.speak("O K lets play")
        self.speak("rock paper scissors go")
	
	rpsRound.append(self.playerChoice())

        self.speak("i chose " + rpsRound[0])
	self.speak("you chose " + rpsRound[1])

	self.gameLogic(rpsRound)	
       
    def take_picture(self):
    	sleep(2)
       	with picamera.PiCamera() as camera:

        	try:
                	camera.resolution = (1280,720)
                       	camera.start_preview()
                       	camera.capture(self.settings["img_location"] + 'rps.jpg')
                       	self.speak("picture taken")
			LOGGER.info('picture taken')
               	finally:
                       	camera.close()



    def mycroftChoice(self):
    	return self.gameChoices[randint(0,2)]

    def playerChoice(self):
	self.take_picture()
	resp = self.rpsModel.predict_by_filename(self.settings["img_location"] + 'rps.jpg')
	return self.parseResponse(resp)	
	
    def parseResponse(self,response):
	
	playerChoices = []
	j = json.dumps(response['outputs'][0],separators=(',',': '),indent=3)
    	jl = json.loads(j)

    	# print type(jl0)
    	index = 0

    	for each in jl['data']['concepts']:
        	myConcept = jl['data']['concepts'][index]['name']
        	playerChoices.append(myConcept)
		myValue = jl['data']['concepts'][index]['value']
        	LOGGER.info('ROCK PAPER SCISSORS:' +  str(myConcept) + " : " + str(myValue))
     		index = index + 1
	return playerChoices[0]


    def gameLogic(self,choices):

	if choices[0] == choices[1]:
	# tie
		self.speak("this is a tie")
	elif ('rock' in choices) and ('paper' in choices):
	# paper covers rock
		self.speak("paper covers rock")
	elif ('rock' in choices) and ('scissors' in choices):
		self.speak("rock breaks scissors")
        # rock breaks scissors
	elif ('paper' in choices) and ('scissors' in choices):
		self.speak("scissors cut paper")
	# scissors cut paper	


    def stop(self):
    	pass


def create_skill():
    return RockPaperScissorsSkill()
