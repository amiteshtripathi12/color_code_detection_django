import os
from collections import Counter
from typing import List
import cv2
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import colors
from sklearn.cluster import KMeans

def rgb_to_hex(rgb_color) -> str:
    hex_color = "#"
    for i in rgb_color:
        i = int(i)
        hex_color += ("{:02x}".format(i))
        a = hex_color
    return hex_color


def color_analysis(img:np.ndarray) -> List[str]:
    """ Function accepts an image of type np.ndarray and outputs a list of strings """
    modified_img = cv2.resize(img, (900, 600), interpolation=cv2.INTER_AREA)
    modified_img = modified_img.reshape(modified_img.shape[0] * modified_img.shape[1], 3)

    clf = KMeans(n_clusters=5)
    color_labels = clf.fit_predict(modified_img)
    center_colors = clf.cluster_centers_
    counts = Counter(color_labels)
    ordered_colors = [center_colors[i] for i in counts.keys()]
    hex_colors = [rgb_to_hex(ordered_colors[i]) for i in counts.keys()]
    plt.figure(figsize=(12, 8))
    return hex_colors


def get_image_hexcolors(image_path:str) -> List[str]:
    """ 
    Accepts an image path and calculate colors present 
    in image then returns a list of those colors in 
    hexadecimal format
    """
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    hex_colors = color_analysis(image)
    return hex_colors

