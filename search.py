import numpy as np
import cv2
import os
import glob
import json
import argparse


def binarize (img, ksize=31, threshold=15):
    img_blur = cv2.GaussianBlur(img, (ksize, ksize), 0, 0)
    img_sub = cv2.subtract(img_blur,img)
    _, binary = cv2.threshold(img_sub, threshold, 255, cv2.THRESH_BINARY)
    return binary

def change_imgsize(img, ratio):
    height = img.shape[0]
    width = img.shape[1]
    resized_img = cv2.resize(img , (int(width*ratio), int(height*ratio)))
    return resized_img

def template_match(img, template):
    w, h = template.shape[::-1]
    result = cv2.matchTemplate(img, template, cv2.TM_CCORR_NORMED)
    _, maxVal, _, maxLoc = cv2.minMaxLoc(result)
    top_left = maxLoc
    btm_right = (top_left[0] + w, top_left[1] + h)
    return maxVal, top_left, btm_right


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('--dir_name', help='directory name which contains x50 image', default='img_search')    # 必須の引数を追加
    parser.add_argument('--original_img_name', help='name of x20 image', default='img_ori.png')
    parser.add_argument('--ratio', default=0.29/0.15)
    parser.add_argument('--display', default=False)
    parser.add_argument('--output_name', default="search.json")
    args = parser.parse_args()

    dir_name = args.dir_name
    list_img_name = glob.glob(f'{dir_name}/*.png')
    list_img_name.sort()

    original_img_name = args.original_img_name
    img_original = cv2.imread(original_img_name, cv2.IMREAD_GRAYSCALE)

    ratio = args.ratio

    dict_result = {"result":[], "dir_name": dir_name, "original_img_name": original_img_name}
    for i in list_img_name:
        this_basename = os.path.basename(i)
        img = cv2.imread(i, cv2.IMREAD_GRAYSCALE)
        img_binalized = binarize(img)
        img_binalized_ori = binarize(img_original)
        
        img_resized_binalized_ori = change_imgsize(img_binalized_ori, ratio)
        maxVal, top_left, btm_right = template_match(img_binalized, img_resized_binalized_ori)
        
        result = {}
        result["img_name"] = this_basename
        result["maxVal"] = maxVal
        result["top_left"] = top_left
        result["btm_right"] = btm_right
        dict_result["result"].append(result)

        print(f'{this_basename}: done. maxVal: {maxVal:.3f}')
        if args.display:
            cv2.rectangle(img, top_left, btm_right, 255, 2)
            cv2.imshow('img_resized_binalized_ori', img_resized_binalized_ori)
            cv2.imshow('img', img)
            cv2.waitKey(0)    

    with open('search.json', 'w') as f:
        json.dump(dict_result, f, indent=2, ensure_ascii=False)
    