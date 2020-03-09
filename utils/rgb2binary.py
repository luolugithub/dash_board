# -*- coding: utf-8 -*-
# @Time    : 2020/2/19 下午5:00
# @Author  : luolu
# @Email   : argluolu@gmail.com
# @File    : rgb2binary.py
# @Software: PyCharm

import cv2

img = cv2.imread('/home/luolu/Downloads/data/bopian/阿布扎比薄片照片/image/dy106_1374665.png', 0)
# cv2.imshow('Gray Image', img)
gray_img = cv2.cvtColor(img, cv2.COLOR_BAYER_GR2BGR)
ret, bw = cv2.threshold(gray_img, 224, 268, cv2.THRESH_BINARY)
# cv2.imshow('Binary', bw)
cv2.imwrite('/home/luolu/PycharmProjects/BONC Cloudiip/dy106_1374665.jpg', bw)

