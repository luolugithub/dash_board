# -*- coding: utf-8 -*-
# @Time    : 2019/12/25 上午8:47
# @Author  : luolu
# @Email   : argluolu@gmail.com
# @File    : crop_img.py
# @Software: PyCharm
import glob
import os

import cv2

# crop single image
# img = cv2.imread("/home/luolu/PycharmProjects/BONC Cloudiip/result/binary_all732.jpg")
# crop_img = img[190:990, 420:1220]
# # cv2.imshow("cropped", crop_img)
# # cv2.waitKey(0)
# cv2.imwrite("/home/luolu/PycharmProjects/BONC Cloudiip/result/cropped_binary.jpg", crop_img)

# batch crop image
if __name__ == '__main__':
    for filename in glob.glob('/home/luolu/PycharmProjects/BONC Cloudiip/center_result/*.jpg'):
        img = cv2.imread(filename)
        print(filename)
        base_name = os.path.basename(filename)
        print(base_name)
        crop_img = img[190:990, 420:1220]
        cv2.imwrite("/home/luolu/PycharmProjects/BONC Cloudiip/crop_image/" + base_name, crop_img)
