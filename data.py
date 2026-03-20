# OpenCV

import cv2 as cv 
import sys 


def writeImage():
    img = cv.imread("./image.png") #read image from path

    gray_image = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    cv.imshow('gray',gray_image)
    cv.waitKey(0)

def readImage():
    img = cv.imread("./image.png") #read image from path
    cv.imshow('img', img)
    cv.waitKey(0)
    writeImage()

if __name__ == '__main__':
    readImage()