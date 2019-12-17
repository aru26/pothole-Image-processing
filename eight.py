#Thresholding with open cv
#simplification of an image using open cv
import cv2
import numpy as np
img = cv2.imread('potholethresholding.jpg')
gimg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
print('original image shape:', img.shape)
cv2.imshow('input image', img)
cv2.imshow('output image', gimg)
height = img.shape[0]
width = img.shape[1]
depth = img.shape[2]
print("height:",height)
print("width:",width)
print("depth:",depth)
retval,threshold=cv2.threshold(img,12,255,cv2.THRESH_BINARY)

grayscaled=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
retval2,threshold2=cv2.threshold(grayscaled,12,255,cv2.THRESH_BINARY)
gaus=cv2.adaptiveThreshold(grayscaled,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,115,1)
retval2,otsu=cv2.threshold(grayscaled,125,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
cv2.imshow('original',img)
cv2.imshow('threshold',threshold)
cv2.imshow('threshold',threshold2)
cv2.imshow('gaus',gaus)
cv2.imshow('otsu',otsu)
cv2.waitKey(0)
cv2.destroyAllWindows()

