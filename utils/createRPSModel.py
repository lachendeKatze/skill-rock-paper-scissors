# basic & crude script to add images and crate the Rock-Paper-Scissors Model

# clarifai libraries
from clarifai import rest
from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage

clarifai_app = ClarifaiApp(api_key="YOUR_API_KEY_HERER")

# training images positve for Rock-Paper-Scissors
# Rock
# ** WILL ONLY WORK IF YOUR FILES ARE NAMED THE SAME AND IN THE SAME DIRECTORY AS THIS SCRIPT ***
clarifai_app.inputs.create_image_from_filename(filename="rock1.jpg", concepts=['rock'], not_concepts=['paper','scissors'])
clarifai_app.inputs.create_image_from_filename(filename="rock2.jpg", concepts=['rock'], not_concepts=['paper','scissors'])
clarifai_app.inputs.create_image_from_filename(filename="rock3.jpg", concepts=['rock'], not_concepts=['paper','scissors'])
clarifai_app.inputs.create_image_from_filename(filename="rock4.jpg", concepts=['rock'], not_concepts=['paper','scisosrs'])
clarifai_app.inputs.create_image_from_filename(filename="rock5.jpg", concepts=['rock'], not_concepts=['paper','scissors'])
clarifai_app.inputs.create_image_from_filename(filename="rock6.jpg", concepts=['rock'], not_concepts=['paper','scissors'])
clarifai_app.inputs.create_image_from_filename(filename="rock7.jpg", concepts=['rock'], not_concepts=['paper','scissors'])
clarifai_app.inputs.create_image_from_filename(filename="rock8.jpg", concepts=['rock'], not_concepts=['paper','scissors'])
clarifai_app.inputs.create_image_from_filename(filename="rock9.jpg", concepts=['rock'], not_concepts=['paper','scissors'])
clarifai_app.inputs.create_image_from_filename(filename="rock10.jpg", concepts=['rock'], not_concepts=['paper','scissors'])

# Paper
clarifai_app.inputs.create_image_from_filename(filename="paper1.jpg", concepts=['paper'], not_concepts=['rock','scissors'])
clarifai_app.inputs.create_image_from_filename(filename="paper2.jpg", concepts=['paper'], not_concepts=['rock','scissors'])
clarifai_app.inputs.create_image_from_filename(filename="paper3.jpg", concepts=['paper'], not_concepts=['rock','scissors'])
clarifai_app.inputs.create_image_from_filename(filename="paper4.jpg", concepts=['paper'], not_concepts=['rock','scissors'])
clarifai_app.inputs.create_image_from_filename(filename="paper5.jpg", concepts=['paper'], not_concepts=['rock','scissors'])
clarifai_app.inputs.create_image_from_filename(filename="paper6.jpg", concepts=['paper'], not_concepts=['rock','scissors'])
clarifai_app.inputs.create_image_from_filename(filename="paper7.jpg", concepts=['paper'], not_concepts=['rock','scissors'])
clarifai_app.inputs.create_image_from_filename(filename="paper8.jpg", concepts=['paper'], not_concepts=['rock','scissors'])
clarifai_app.inputs.create_image_from_filename(filename="paper9.jpg", concepts=['paper'], not_concepts=['rock','scissors'])
clarifai_app.inputs.create_image_from_filename(filename="paper10.jpg", concepts=['paper'], not_concepts=['rock','scissors'])

# Scissors
clarifai_app.inputs.create_image_from_filename(filename="scissors1.jpg", concepts=['scissors'], not_concepts=['rock','paper'])
clarifai_app.inputs.create_image_from_filename(filename="scissors2.jpg", concepts=['scissors'], not_concepts=['rock','paper'])
clarifai_app.inputs.create_image_from_filename(filename="scissors3.jpg", concepts=['scissors'], not_concepts=['rock','paper'])
clarifai_app.inputs.create_image_from_filename(filename="scissors4.jpg", concepts=['scissors'], not_concepts=['rock','paper'])
clarifai_app.inputs.create_image_from_filename(filename="scissors5.jpg", concepts=['scissors'], not_concepts=['rock','paper'])
clarifai_app.inputs.create_image_from_filename(filename="scissors6.jpg", concepts=['scissors'], not_concepts=['rock','paper'])
clarifai_app.inputs.create_image_from_filename(filename="scissors7.jpg", concepts=['scissors'], not_concepts=['rock','paper'])
clarifai_app.inputs.create_image_from_filename(filename="scissors8.jpg", concepts=['scissors'], not_concepts=['rock','paper'])
clarifai_app.inputs.create_image_from_filename(filename="scissors9.jpg", concepts=['scissors'], not_concepts=['rock','paper'])
clarifai_app.inputs.create_image_from_filename(filename="scissors10.jpg", concepts=['scissors'], not_concepts=['rock','paper'])

model = clarifai_app.models.create('rockpaperscissors', concepts=['rock','paper','scissors'])
