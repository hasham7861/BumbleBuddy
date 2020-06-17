# '''
#     Author: Hasham Alam
#     Features: swipe right based on your user type, and then message them

#     How does this AI know when to swipe right
#     steps: given an image of person you like, then based on that swipe right
#         before swiping right, crop images to just detect the face. - face_recogniztion - find_faces_in_picture.py
#         then based on that determine how big is the difference. find the right distance number
#         Extra features can be for searching for extra attributes within the profile of what you like
#         for example. you went to same school. same hobbies to scan within the profile
# '''

import requests
from PIL import Image
from autocrop import Cropper

from config import config
# # Example posting a local image file:


cropper = Cropper()

# Crop every image you compare for getting an accurate comparsion


def CropFace(file_path):
    # Get a Numpy array of the cropped image
    cropped_array = cropper.crop(file_path)
    # Save the cropped image with PIL
    cropped_image = Image.fromarray(cropped_array)
    cropped_image.save('cropped_images/'+file_path)

# Based on face distance return true if person is your type or not


def SimilarFace(file_path1, file_path2):
    face_distance = requests.post(
        "https://api.deepai.org/api/image-similarity",
        files={
            'image1': open(file_path1, 'rb'),
            'image2': open(file_path2, 'rb'),
        },
        headers={'api-key': config["deepai"]["key"]}
    )
    # The lower the number for distance the similar the image is. I kept it as 28 for sharing attributes
    is_your_type = face_distance.json()["output"]["distance"] <= 28

    return is_your_type


# print("This person is your type: ", SimilarFace(
#     'cropped_images/hasham.jpg', 'cropped_images/shabaz.jpg'))


# CropFace("randomguy2.jpg")
