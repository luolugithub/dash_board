# -*- coding: utf-8 -*-
# @Time : 2020/3/9 下午3:51
# @Author : LuoLu
# @FileName: extract_bboxes.py
# @Software: PyCharm
# @Github ：https://github.com/luolugithub
# @E-mail ：argluolu@gmail.com
import glob

import cv2
import cv2 as cv
import imutils
import numpy as np

from BCC import local_threshold, get_adaptive_circle

# im = cv2.imread('/home/luolu/PycharmProjects/BONC Cloudiip/result/ellipse_img732.jpg')
# gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
# contours, hierarchy = cv2.findContours(gray, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)[-2:]
# idx = 0
# for cnt in contours:
#     idx += 1
#     x, y, w, h = cv2.boundingRect(cnt)
#     roi = im[y:y + h, x:x + w]
#     # cv2.imwrite(str(idx) + '.jpg', roi)
#     # cv2.rectangle(im, (x, y), (x + w, y + h), (255, 0, 0), 4)
#     # print(x, y, w, h)
# print(x, y, w, h)
# crop_img = im[y:y+max(w, h), x:x+max(w, h)]
# cv2.imwrite("/home/luolu/PycharmProjects/BONC Cloudiip/result/crop_img_center732.jpg", crop_img)
# # cv2.imshow('img', im)
# # cv2.waitKey(0)

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
        contours, hierarchy = cv2.findContours(gray, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)[-2:]
        idx = 0
        for cnt in contours:
            idx += 1
            x, y, w, h = cv2.boundingRect(cnt)
            roi = img[y:y + h, x:x + w]
            # cv2.imwrite(str(idx) + '.jpg', roi)
            # cv2.rectangle(im, (x, y), (x + w, y + h), (255, 0, 0), 4)
            # print(x, y, w, h)
        print(x, y, w, h)
        crop_img = img[y:y + max(w, h), x:x + max(w, h)]
        cv2.imwrite("/home/luolu/PycharmProjects/BONC Cloudiip/crop_image/" + file_name, crop_img)