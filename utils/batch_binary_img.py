# -*- coding: utf-8 -*-
# @Time    : 2019/12/21 下午2:55
# @Author  : luolu
# @Email   : argluolu@gmail.com
# @File    : binary_img.py
# @Software: PyCharm
import glob
import os

import cv2 as cv
import numpy as np


# 全局阈值
from PIL import Image


def threshold_binary(image, base_name):
    gray = cv.cvtColor(image, cv.COLOR_RGB2GRAY)  # 把输入图像灰度化
    # 直接阈值化是对输入的单通道矩阵逐像素进行阈值分割。
    ret, binary = cv.threshold(gray, 125, 255, cv.THRESH_BINARY_INV)
    print("threshold value %s" % ret)
    # cv.namedWindow("binary_all", cv.WINDOW_NORMAL)
    # cv.imshow("binary0", binary)
    cv.imwrite("/home/luolu/PycharmProjects/BONC Cloudiip/center_result/" + base_name, binary)


# 局部阈值
def local_threshold(image):
    gray = cv.cvtColor(image, cv.COLOR_RGB2GRAY)  # 把输入图像灰度化
    # 自适应阈值化能够根据图像不同区域亮度分布，改变阈值
    binary = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 25, 10)
    # cv.namedWindow("binary1", cv.WINDOW_NORMAL)
    # cv.imshow("binary1", binary)
    cv.imwrite("/home/luolu/PycharmProjects/BONC Cloudiip/result/binary_local732.jpg", binary)
    return binary


# 用户自己计算阈值
def custom_threshold(image):
    gray = cv.cvtColor(image, cv.COLOR_RGB2GRAY)  # 把输入图像灰度化
    h, w = gray.shape[:2]
    m = np.reshape(gray, [1, w * h])
    mean = m.sum() / (w * h)
    print("mean:", mean)
    ret, binary = cv.threshold(gray, mean, 255, cv.THRESH_BINARY)
    # cv.namedWindow("binary2", cv.WINDOW_NORMAL)
    # cv.imshow("binary2", binary)
    cv.imwrite("/home/luolu/PycharmProjects/BONC Cloudiip/result/binary_custom.jpg", binary)


src = cv.imread('/home/luolu/PycharmProjects/BONC Cloudiip/image/1_0732.jpg')
if __name__ == '__main__':
    for filename in glob.glob('/home/luolu/PycharmProjects/BONC Cloudiip/image/*.jpg'):
        img = cv.imread(filename)
        print(filename)
        base_name = os.path.basename(filename)
        print(base_name)
        threshold_binary(img, base_name)



