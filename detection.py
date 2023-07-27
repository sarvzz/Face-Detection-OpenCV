import cv2 as cv
import os

# read the images from dir
def load_images_from_folder(folder):
    images = []
    for filename in os.listdir(folder):
        img = cv.imread(os.path.join(folder,filename))
        if img is not None:
            images.append(img)
    return images


img = load_images_from_folder('Photos')

# read the input image
# img = cv.imread('Photos/LilyRoseDepp.jpeg')
# cv.imshow('Person', img)

# convert to grayscale of each frame
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray Person', gray)

# # read the haarcascade 
# haar_cascade = cv.CascadeClassifier('haar_face.xml')

# # detect the faces in an image, it returns the coordinates of detected faces in (x,yw,h) format
# faces = haar_cascade.detectMultiScale(gray, scaleFactor=2, minNeighbors=3)

# print(f'-> Number of faces found = {len(faces)}')

# # loop over all detected faces
# if len(faces)>0: 
#     for i, (x,y,w,h) in enumerate(faces):

#         # draw rectangle around the detected face:
#         cv.rectangle(img, (x,y), (x+w,y+h), (0,255,255), thickness=4)
#         face = img[y:y+h, x:x+w]
#         cv.imshow('Cropped Face', face)
#         cv.imwrite(f'faces{i}.jpeg',face)
#         print(f'face{i}.jpeg is saved')

# # display the image with detected faces
# cv.imshow('Detected Faces', img)

# press any key to close the images
cv.waitKey(0)
cv.destroyAllWindows()
