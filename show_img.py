import numpy as np
import cv2
import random
import os
import sys
import glob
import pathlib
import pickle
import matplotlib.pyplot as plt
import csv

def binarize (img):
    img_blur = cv2.GaussianBlur(img,(31,31),0,0)
    img_sub = cv2.subtract(img_blur,img)
    _, binary = cv2.threshold(img_sub,15,255,cv2.TM_SQDIFF)
    return binary

def change_imgsize(img):
    height = img.shape[0]
    width = img.shape[1]
    ratio = 0.29/0.15
    resized_img = cv2.resize(img , (int(width*ratio), int(height*ratio)))
    return resized_img

def template_match(img,temp):
    w, h = temp.shape[::-1]
    result = cv2.matchTemplate(img, temp, cv2.TM_CCOEFF)
    minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(result)
    top_left = maxLoc
    btm_right = (top_left[0] + w, top_left[1] + h)
    return maxVal,top_left,btm_right
args = sys.argv
number = int(args[1])
filename = 'img_search'
imgs = glob.glob(filename + "/*.png")
imgs.sort()
img_ori = cv2.imread('img_ori.png', 0)

if __name__ == "__main__":
    img = cv2.imread(imgs[number], 0)
    niti = binarize(img)
    niti_ori = binarize(img_ori)
        
    resized_niti_ori = change_imgsize(niti_ori)
    resized_img_ori = change_imgsize(img_ori) 

    maxVal , top_left,btm_right = template_match(niti,niti_ori)
    print(maxVal)
    cv2.rectangle(img,top_left, btm_right, 255, 2)
    cv2.imshow('resized',img_ori)
    cv2.imshow(str(251),img)
    cv2.waitKey(0)    