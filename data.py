# OpenCV

import cv2 as cv 
import sys 
import random

def writeImage():
    img = cv.imread("./image.png") #read image from path

    gray_image = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    if img is None:
        sys.exit("Could not read image")
 
    cv.imshow('gray',gray_image)
    cv.waitKey(0)

def readImage():
    img = cv.imread("./image.png") #read image from path
    if img is None:
        sys.exit("Could not read image")

    tag = img[50:100, 20:50]

    img[150:200, 50:80] = tag

    img[200:215, 100:150] = 0

    img[100:150, 200:225] = 255
    img[100:150, 250:275] = 255
    img[175:200, 200:275] = 255
    for i in range(5):
        for j in range(img.shape[1]):
            img[i][j] = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
    cv.imshow('img', img)
    cv.waitKey(0)
    writeImage()

if __name__ == '__main__':
    readImage()