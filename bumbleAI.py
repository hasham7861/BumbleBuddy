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

from PIL import Image
import face_recognition

# Load the jpg file into a numpy array
image = face_recognition.load_image_file("hasham.jpg")

# Find all the faces in the image using the default HOG-based model.
# This method is fairly accurate, but not as accurate as the CNN model and not GPU accelerated.
# See also: find_faces_in_picture_cnn.py
face_locations = face_recognition.face_locations(image)

print("I found {} face(s) in this photograph.".format(len(face_locations)))

for face_location in face_locations:

    # Print the location of each face in this image
    top, right, bottom, left = face_location
    print("A face is located at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}".format(
        top, left, bottom, right))

    # You can access the actual face itself like this:
    face_image = image[top:bottom, left:right]
    pil_image = Image.fromarray(face_image)
    pil_image.show()
