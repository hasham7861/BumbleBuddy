'''
    Author: Hasham Alam
    Features: swipe right based on your user type, and then message them

    How does this AI know when to swipe right
    steps: given an image of person you like, then based on that swipe right
        before swiping right, crop images to just detect the face. - face_recogniztion - find_faces_in_picture.py
        then based on that determine how big is the difference. find the right distance number
        Note: use face_recognition - face_distance api
        Extra features can be for searching for extra attributes within the profile of what you like
        for example. you went to same school. same hobbies to scan within the profile
'''

import requests
from PIL import Image
from autocrop import Cropper

from config import config
# Example posting a local image file:

face_distance = requests.post(
    "https://api.deepai.org/api/image-similarity",
    files={
        'image1': open('cropped.png', 'rb'),
        'image2': open('cropped2.png', 'rb'),
    },
    headers={'api-key': config["deepai"]["key"]}
)

print(face_distance.json())


cropper = Cropper()
# Get a Numpy array of the cropped image
cropped_array = cropper.crop('hasham.jpg')

# Save the cropped image with PIL
cropped_image = Image.fromarray(cropped_array)
cropped_image.save('cropped2.png')
