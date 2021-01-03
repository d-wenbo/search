import numpy as np
import cv2
import random
import os
import sys
import glob
import pathlib
import pickle

with open('search.pickle', 'rb') as f:
    d = pickle.load(f)
    print (d['maxVal'])