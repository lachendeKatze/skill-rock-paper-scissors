# Menu based clarifai imaing traing for Rock-Paper-Scissors

# clarifai libraries
from clarifai import rest
from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage

import json
from time import sleep
from picamera import PiCamera

clarifai_app = ClarifaiApp(api_key="YOUR_API_KEY_HERE")
model = clarifai_app.models.get('rockpaperscissors')
camera = PiCamera()
camera.resolution = (1024,768)

print (30 * '-')
print ("   RPS - TEST MODEL MENU")
print (30 * '-')
print ("0. Exit")
print ("1. Take Test picture")
print (30 * '-')


def takePic(imageName):
    sleep(2)
    # camera.start_preview()
    camera.capture(imageName)
    pass

def displayResponse(response):

    j = json.dumps(response['outputs'][0],separators=(',',': '),indent=3)
    jl = json.loads(j)

    # print type(jl0)
    index = 0

    for each in jl['data']['concepts']:
        myConcept 	= jl['data']['concepts'][index]['name']
        myValue 	= jl['data']['concepts'][index]['value']
        print(str(myConcept) + " : " + str(myValue))
        index = index +1
    pass


choice = 42
### Take action as per selected menu-option ###
while choice != 0:
    choice = raw_input('Enter your choice [0-1] : ')
    choice = int(choice)
    if choice == 1:
        print ("Taking a picture...")
        takePic('test.jpg')
        displayResponse(model.predict_by_filename('test.jpg'))
    else:    ## default ##
        print ("Invalid number. Try again...")

