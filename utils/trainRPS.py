# Menu based clarifai imaing traing for Rock-Paper-Scissors

# clarifai libraries
from clarifai import rest
from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage

from time import sleep
from picamera import PiCamera

clarifai_app = ClarifaiApp(api_key="YOUR_API_KEY_HERE")
model = clarifai_app.models.get('rockpaperscissors')
camera = PiCamera()
camera.resolution = (1024,768)

print (30 * '-')
print ("   RPS - TRAIN MODEL MENU")
print (30 * '-')
print ("0. Exit")
print ("1. Rock")
print ("2. Paper")
print ("3. Scissors")
print (30 * '-')


def takePic(imageName):
    sleep(2)
    camera.start_preview()
    camera.capture(imageName)
    pass

def trainOnPic():
    sleep(2)	
    model.train()
    pass

## Get input ###
# choice = raw_input('Enter your choice [1-3] : ')

### Convert string to int type ##
# choice = int(choice)
choice = 42
### Take action as per selected menu-option ###
while choice != 0:
    choice = raw_input('Enter your choice [0-3] : ')
    choice = int(choice)
    if choice == 1:
        print ("Rock, taking a picture...")
        takePic('rock.jpg')
        clarifai_app.inputs.create_image_from_filename(filename="rock.jpg", concepts=['rock'], not_concepts=['paper','scissors'])
        print ("Rock, training...")
	trainOnPic()
    elif choice == 2:
        print ("Paper, taking a picture...")
        takePic('paper.jpg')
        clarifai_app.inputs.create_image_from_filename(filename="paper.jpg", concepts=['paper'], not_concepts=['rock','scissors'])
        print ("Paper, training...")
	trainOnPic()
    elif choice == 3:
        print ("Scissors, taking a picture...")
        takePic('scissors.jpg')
        clarifai_app.inputs.create_image_from_filename(filename="scissors.jpg", concepts=['scissors'], not_concepts=['rock','paper'])
        print ("Scissors, training...")
	trainOnPic()
    else:    ## default ##
        print ("Invalid number. Try again...")
