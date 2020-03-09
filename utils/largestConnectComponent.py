# -*- coding: utf-8 -*-
# @Time : 2020/3/9 下午3:04
# @Author : LuoLu
# @FileName: largestConnectComponent.py
# @Software: PyCharm
# @Github ：https://github.com/luolugithub
# @E-mail ：argluolu@gmail.com
import cv2
import numpy as np
from PIL import Image


def undesired_objects(image):
    image = image.astype('uint8')
    nb_components, output, stats, centroids = cv2.connectedComponentsWithStats(image, connectivity=8)
    sizes = stats[:, -1]

    max_label = 1
    max_size = sizes[1]
    for i in range(2, nb_components):
        if sizes[i] > max_size:
            max_label = i
            max_size = sizes[i]

    img2 = np.zeros(output.shape)
    img2[output == max_label] = 255
    cv2.imshow("Biggest component", img2)
    cv2.waitKey()

if __name__ == '__main__':
    img = Image.open('/home/luolu/PycharmProjects/BONC Cloudiip/center_result/1_0028.jpg')
    img = np.array(img)
    undesired_objects(img)
