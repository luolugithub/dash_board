# -*- coding: utf-8 -*-
# @Time    : 2019/12/21 下午3:20
# @Author  : luolu
# @Email   : argluolu@gmail.com
# @File    : get_centre_binary_img.py
# @Software: PyCharm
import composite as composite
import cv2
import numpy as np

img = cv2.imread('/home/luolu/PycharmProjects/BONC Cloudiip/result/binary_local732.jpg')

ret, thresh = cv2.threshold(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY), 127, 255, 0)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)  # 得到轮廓信息
cnt = contours[0]  # 取第一条轮廓
M = cv2.moments(cnt)  # 计算第一条轮廓的矩

imgnew = cv2.drawContours(img, contours, -1, (0, 255, 0), 3)  # 把所有轮廓画出来
print(M)
# 这两行是计算中心点坐标
cx = int(M['m10'] / M['m00'])
cy = int(M['m01'] / M['m00'])
print(cx, cy)

# 计算轮廓所包含的面积
area = cv2.contourArea(cnt)

# 计算轮廓的周长
perimeter = cv2.arcLength(cnt, True)

# 轮廓的近似
epsilon = 0.02 * perimeter
approx = cv2.approxPolyDP(cnt, epsilon, True)
imgnew1 = cv2.drawContours(img, approx, -1, (255, 0, 0), 3)

# cv2.imshow('lunkuo', imgnew)
# cv2.imshow('approx_lunkuo', imgnew1)
cv2.imwrite("/home/luolu/PycharmProjects/BONC Cloudiip/result/lunkuo732.jpg", imgnew)
cv2.imwrite("/home/luolu/PycharmProjects/BONC Cloudiip/result/approx_lunkuo732.jpg", imgnew1)

# im = cv2.imread('/home/luolu/PycharmProjects/BONC Cloudiip/result/binary_local.jpg')
# imgray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
# ret, thresh = cv2.threshold(imgray, 127, 255, 0)
# contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#
# for c in contours:
#     if cv2.contourArea(c) <= 50:
#         continue
#     x, y, w, h = cv2.boundingRect(c)
#     cv2.rectangle(im, (x, y), (x + w, y + h), (0, 255, 0), 2)
#     center = (x, y)
#     print(center)
#
# while True:
#     cv2.imshow('test', im)
#     if cv2.waitKey(20) & 0xFF == 27:
#         break
# cv2.destroyAllWindows()
