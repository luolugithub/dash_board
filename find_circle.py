# -*- coding: utf-8 -*-
# @Time    : 2019/12/21 下午4:20
# @Author  : luolu
# @Email   : argluolu@gmail.com
# @File    : find_circle.py
# @Software: PyCharm
'''
此方法是一种动态自适应找圆方法
使用方法：
im_floodfill = get_adaptive_circle(crop_img)
输入原图crop_img
返回mask
'''

import os
import cv2
import numpy as np


# 求最大连通域的中心点坐标
# def centroid(max_contour):
#     moment = cv2.moments(max_contour)
#     if moment['m00'] != 0:
#         cx = int(moment['m10'] / moment['m00'])
#         cy = int(moment['m01'] / moment['m00'])
#         return cx, cy
#     else:
#         return None


def fillHole(im_in):
    im_floodfill = im_in.copy()
    im_floodfill = np.uint8(im_floodfill)
    row, col, dim = im_floodfill.shape

    # Mask used to flood filling
    # Notice the size needs to be 2 pixels than the image
    mask = np.zeros((row + 2, col + 2), np.uint8)

    # Floodfill from point int(row/2), int(col/2)
    cv2.floodFill(im_floodfill, mask, (int(row / 2), int(col / 2)), (255, 255, 255))
    # cv2.morphologyEx(im_floodfill, cv2.MORPH_ELLIPSE, mask)
    return im_floodfill


def get_adaptive_circle(crop_img):
    ori_row, ori_col, ori_dim = crop_img.shape
    print("crop_img shape:", crop_img.shape)
    # img = cv2.resize(crop_img, (240, 270))
    img = crop_img
    row, col, dim = img.shape
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 灰度图像

    edges = cv2.Canny(gray, 100, 200)

    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (15, 15))  # 圆形kernel
    closing = cv2.morphologyEx(edges, cv2.MORPH_CLOSE, kernel, 100)

    # 提取边缘
    contours, hierarchy = cv2.findContours(closing, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # 找到最大的contour
    area = []
    for j in range(len(contours)):
        area.append(cv2.contourArea(contours[j]))
    max_idx = np.argmax(area)

    # 求椭圆
    ellipse = cv2.fitEllipse(contours[max_idx])
    ellipse_img = np.zeros((row, col, dim))
    cv2.ellipse(ellipse_img, ellipse, (255, 255, 255), 2)

    # 填充椭圆
    ellipse_fill = fillHole(ellipse_img)
    # ellipse_fill = cv2.resize(ellipse_fill, (ori_row, ori_col))
    ret, ellipse_fill = cv2.threshold(ellipse_fill[:, :, 0], 0, 255, cv2.THRESH_BINARY | cv2.THRESH_TRIANGLE)

    # cv2.imshow('Canny', edges)
    # cv2.imshow('closing', closing)
    # cv2.imshow('ellipse_img', ellipse_img)
    # cv2.imshow('ellipse_fill', ellipse_fill)
    #
    # cv2.waitKey(0)
    # cv2.imwrite("/home/luolu/PycharmProjects/BONC Cloudiip/result/Canny.jpg", edges)
    # cv2.imwrite("/home/luolu/PycharmProjects/BONC Cloudiip/result/closing.jpg", closing)
    cv2.imwrite("/home/luolu/PycharmProjects/BONC Cloudiip/result/ellipse_img732.jpg", ellipse_img)
    # cv2.imwrite("/home/luolu/PycharmProjects/BONC Cloudiip/result/ellipse_fill.jpg", ellipse_fill)

    return ellipse_fill


if __name__ == '__main__':
    img = cv2.imread("/home/luolu/PycharmProjects/BONC Cloudiip/result/binary_local732.jpg")
    # crop_img = img
    print("img shape:", img.shape)
    ellipse = get_adaptive_circle(img)
    print("ellipse img shape:", ellipse.shape)

    # save_img_path = os.path.join("/home/luolu/PycharmProjects/BONC Cloudiip/result", ellipse)
    # cv2.imwrite(save_img_path, ellipse)

