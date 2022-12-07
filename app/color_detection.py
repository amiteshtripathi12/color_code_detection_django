import os
from collections import Counter

import cv2
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import colors
from sklearn.cluster import KMeans

# image = Image.objects.all()
image = cv2.imread(r"C:\colour\color_finder\media\uploads\photos")
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
plt.imshow(image)
a = plt.imshow(image)

print(a)


def rgb_to_hex(rgb_color):
    hex_color = "#"
    for i in rgb_color:
        i = int(i)
        hex_color += ("{:02x}".format(i))
        a = hex_color
        # print("hello",a)
    return hex_color


def prep_image(raw_img):
    modified_img = cv2.resize(raw_img, (900, 600), interpolation=cv2.INTER_AREA)
    modified_img = modified_img.reshape(modified_img.shape[0] * modified_img.shape[1], 3)
    return modified_img


def color_analysis(img):
    clf = KMeans(n_clusters=5)
    color_labels = clf.fit_predict(img)
    center_colors = clf.cluster_centers_
    counts = Counter(color_labels)
    ordered_colors = [center_colors[i] for i in counts.keys()]
    hex_colors = [rgb_to_hex(ordered_colors[i]) for i in counts.keys()]
    plt.figure(figsize=(12, 8))
    # plt.pie(counts.values(), color_labels = hex_colors, colors = hex_colors)
    # plt.savefig(r'F:\New folder\blue1.png')
    hexn = hex_colors
    return render(request, 'index.html', {'hexn': hexn})
    # print(hex_colors)


modified_image = prep_image(image)
color_analysis(modified_image)
