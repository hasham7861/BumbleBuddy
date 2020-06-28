# '''
#     Author: Hasham Alam
#     Features: swipe right based on your user type, and then message them

#     How does this AI know when to swipe right
#     steps: given an image of person you like, then based on that swipe right
#         before swiping right, crop images to just detect the face. - face_recogniztion - find_faces_in_picture.py
#         then based on that determine how big is the difference. find the right distance number
#         Extra features can be for searching for extra attributes within the profile of what you like
#         for example. you went to same school (UofT). same hobbies to scan within the profile ()
# '''

import requests
from PIL import Image
from autocrop import Cropper
import time

import configparser
config = configparser.ConfigParser()
config.read('config.INI')

cropper = Cropper()

# Crop every image you compare for getting an accurate comparsion


def crop_face(file_path):
    time.sleep(2)
    # Get a Numpy array of the cropped image
    cropped_array = cropper.crop(file_path)
    # Save the cropped image with PIL
    cropped_image = Image.fromarray(cropped_array)

    cropped_image_path = 'images/crop/'+file_path.split("/download/")[1]
    cropped_image.save(cropped_image_path)
    return cropped_image_path

# Based on face distance return true if person is your type or not


def similar_face(your_type_image_path, candidate_image_path):
    time.sleep(2)
    try:
        face_distance = requests.post(
            "https://api.deepai.org/api/image-similarity",
            files={
                'image1': open(your_type_image_path, 'rb'),
                'image2': open(candidate_image_path, 'rb'),
            },
            headers={'api-key': config["deepai"]["key"]}
        )
        # The lower the number for distance the similar the image is. I kept it as 28 for sharing attributes
        is_your_type = face_distance.json()["output"]["distance"] <= 28

        return is_your_type
    except Exception as e:
        print(e)
        return
