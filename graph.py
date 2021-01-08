import numpy as np
import cv2
import sys
import matplotlib.pyplot as plt
import json


if __name__ == "__main__":
    
    json_name = sys.argv[1]

    with open(json_name) as f:
        dict_result = json.load(f)

    list_i = []
    list_maxValue = []
    for i, r in enumerate(dict_result["result"]):
        list_i.append(float(i))
        list_maxValue.append(r["maxVal"])

    i_selected = np.argmax(list_maxValue)
    print(f"{i_selected} is the best, maxVal = {list_maxValue[i_selected]}")
    
    plt.scatter(list_i,list_maxValue)
    plt.show()
    