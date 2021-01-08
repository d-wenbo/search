import numpy as np
import cv2
import random
import os
import sys
import glob
import itertools
import matplotlib.pyplot as plt
import math
import csv


#new_dir_path_graph = 'hough_para_rms/'
#os.makedirs(new_dir_path_graph,exist_ok = True)


def rms(list):
    np_list = np.array(list)
    np_list = np.square(np_list)
    mse = np.sum(np_list)/(np_list.size-1)
    return mse

def search_max(list):
    max_list = max(list)
    for i in range(len(list)):
        test = list[i]
        if test == max_list:
            i_sele = i
        else: 
            continue
    return i_sele
if __name__ == "__main__":
    
    
    
    
    list_i = []
    list_maxValue = []
    list_top_left = []
    list_btm_right = []


    with open('search.csv') as f:
        reader = csv.reader(f)
        for row in reader:
            list_i.append(row[0])
            list_maxValue.append(row[1])
            list_top_left.append(row[2])
            list_btm_right.append(row[3])
    f.close

    del list_i[0]
    del list_maxValue[0]
    del list_top_left[0]
    del list_btm_right[0]
    
    
    

    list_i = [float(i) for i in list_i ]
    list_maxValue = [float(i) for i in list_maxValue ]
    #list_top_left = [float(i) for i in list_top_left ]
    #list_btm_right = [float(i) for i in list_btm_right]
    
    i_sele = search_max(list_maxValue) 

    print(i_sele)
    
    plt.scatter(list_i,list_maxValue)
    plt.show()
    
    
                