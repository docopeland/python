# The Assignment
# Take a ZIP file of images and process them, using a library built into python that you need to learn how to use. A ZIP
# file takes several different files and compresses them, thus saving space, into one single file. The files in the ZIP
# file we provide are newspaper images (like you saw in week 3). Your task is to write python code which allows one to
# search through the images looking for the occurrences of keywords and faces. E.g. if you search for "pizza" it will
# return a contact sheet of all of the faces which were located on the newspaper page which mentions "pizza". This will
# test your ability to learn a new (library), your ability to use OpenCV to detect faces, your ability to use tesseract
# to do optical character recognition, and your ability to use PIL to composite images together into contact sheets.
#
# Each page of the newspapers is saved as a single PNG image in a file called images.zip. These newspapers are in
# english, and contain a variety of stories, advertisements and images. Note: This file is fairly large (~200 MB) and
# may take some time to work with, I would encourage you to use small_img.zip for testing.

import zipfile

from PIL import Image
import pytesseract
import cv2 as cv

# loading the face detection classifier
face_cascade = cv.CascadeClassifier('readonly/haarcascade_frontalface_default.xml')

# the rest is up to you!
def faceCrop(image):
    gray = cv.cvtColor(image,cv.COLOR_RGB2GRAY)
    faces = face_cascade.detectMultiScale(gray,1.35)
    pilImg = Image.fromarray(gray)
    return [pilImg.crop((face[0],face[1],face[0]+face[2],face[1]+face[3])) for face in faces]

def showFace(faces):
    if len(faces) < 1:
        print("But there were no faces in that file!")
    elif len(faces) > 5:
        facepage = Image.new("L",(500,200))
        for i in range(len(faces)):
            faces[i] = faces[i].resize((100,100),Image.NEAREST)
            if i < 5:
                facepage.paste(faces[i],(i*100,0))
            else:
                facepage.paste(faces[i],((i-5)*100,100))
    else:
        facepage = Image.new("L",(500,100))
        for i in range(len(faces)):
            faces[i] = faces[i].resize((100,100),Image.NEAREST)
            facepage.paste(faces[i],(i*100,0))
    facepage.show()

def search(word,zipf):
    zip = zipfile.ZipFile(zipf,"r")
    for name in zip.namelist():
        if word in pytesseract.image_to_string(name):
            print("Results found in file {}".format(name))
            image = cv.imread(name)
            showFace(faceCrop(image))
        else:
            continue