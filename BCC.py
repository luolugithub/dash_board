# -*- coding: utf-8 -*-
# @Time    : 2019/12/21 下午4:59
# @Author  : luolu
# @Email   : argluolu@gmail.com
# @File    : BCC.py
# @Software: PyCharm
import os

import cv2
import cv2 as cv
import numpy as np
import imutils
import glob
from PIL import Image


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


def rgb2gray(rgb):
    return np.dot(rgb[..., :3], [0.2989, 0.5870, 0.1140])


# 局部阈值
def local_threshold(image):
    gray = cv.cvtColor(image, cv.COLOR_RGB2GRAY)  # 把输入图像灰度化
    # 自适应阈值化能够根据图像不同区域亮度分布，改变阈值
    binary = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 25, 10)
    # cv.namedWindow("binary1", cv.WINDOW_NORMAL)
    # cv.imshow("binary1", binary)
    # cv.imwrite("/home/luolu/PycharmProjects/BONC Cloudiip/result/binary_local.jpg", binary)
    return binary


def get_adaptive_circle(image):
    ori_row, ori_col, ori_dim = image.shape
    # img = cv2.resize(crop_img, (240, 270))
    img = image
    row, col, dim = img.shape
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)  # 灰度图像

    edges = cv.Canny(gray, 100, 200)

    kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, (15, 15))  # 圆形kernel
    closing = cv.morphologyEx(edges, cv.MORPH_CLOSE, kernel, 100)

    # 提取边缘
    contours, hierarchy = cv.findContours(closing, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    # 找到最大的contour
    area = []
    for j in range(len(contours)):
        area.append(cv.contourArea(contours[j]))
    max_idx = np.argmax(area)

    # 求椭圆
    ellipse = cv.fitEllipse(contours[max_idx])
    ellipse_img = np.zeros((row, col, dim))
    cv2.ellipse(ellipse_img, ellipse, (255, 255, 255), 2)

    # 填充椭圆
    ellipse_fill = fillHole(ellipse_img)
    # ellipse_fill = cv2.resize(ellipse_fill, (ori_row, ori_col))
    ret, ellipse_fill = cv2.threshold(ellipse_fill[:, :, 0], 0, 255, cv2.THRESH_BINARY | cv2.THRESH_TRIANGLE)
    return ellipse_img


if __name__ == '__main__':
    image_path = '/home/luolu/PycharmProjects/BONC Cloudiip/image/*.jpg'
    for filename in glob.glob(image_path):
        img = cv.imread(filename)
        print(filename.split("/")[-1])
        file_name = filename.split("/")[-1]
        bin_img = local_threshold(img)
        backtorgb = cv2.cvtColor(bin_img, cv2.COLOR_GRAY2RGB)
        print("bin_img shape:", backtorgb.shape)
        circle_img = get_adaptive_circle(backtorgb)
        # cv2.imwrite('/home/luolu/PycharmProjects/BONC Cloudiip/result/img_tmp.jpg', circle_img)
        print("circle_img shape:", circle_img.shape)
        # load the image, convert it to grayscale, blur it slightly,
        # and threshold it
        circle_img = np.asarray(circle_img, dtype=np.uint8)
        gray = cv2.cvtColor(circle_img, cv2.COLOR_BGR2GRAY)
        # gray = rgb2gray(circle_img)
        blurred = cv.GaussianBlur(gray, (5, 5), 0)
        thresh = cv.threshold(blurred, 60, 255, cv.THRESH_BINARY)[1]

        # find contours in the thresholded image
        cnts = cv.findContours(thresh.copy(), cv.RETR_EXTERNAL,
                               cv.CHAIN_APPROX_SIMPLE)
        cnts = imutils.grab_contours(cnts)

        # loop over the contours
        for c in cnts:
            # compute the center of the contour
            M = cv.moments(c)
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])

            # draw the contour and center of the shape on the image
            cv.drawContours(circle_img, [c], -1, (0, 255, 0), 2)
            cv.circle(circle_img, (cX, cY), 7, (255, 255, 255), -1)
            cv.putText(circle_img, "center" + "(" + str(cX) + ", " + str(cY) + ")", (cX - 20, cY - 20),
                       cv.FONT_HERSHEY_SIMPLEX, 1.5, (255, 255, 255), 2)

            # show the image
            # cv2.imshow("Image", image)
            # cv2.waitKey(0)
            print("circle_center: " + "(" + str(cX) + ", " + str(cY) + ")")
            with open('/home/luolu/PycharmProjects/BONC Cloudiip/result/bonc_center.txt', 'a') as the_file:
                the_file.write(file_name + "    circle_center: " + "(" + str(cX) + ", " + str(cY) + ")" + '\n')
            cv.imwrite('/home/luolu/PycharmProjects/BONC Cloudiip/center_result/' + file_name, circle_img)

print("Finish!!")
