# -*- coding: utf-8 -*-
# @Time    : 2020/2/19 下午5:45
# @Author  : luolu
# @Email   : argluolu@gmail.com
# @File    : rgb2binaryimg.py
# @Software: PyCharm

import cv2 as cv
import numpy as np

# #[82, 167, 202]
#  [26, 184, 238]

def color_seperate(image):
        hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)   #对目标图像进行色彩空间转换
        lower_hsv = np.array([100, 43, 46])          #设定蓝色下限
        upper_hsv = np.array([124, 255, 255])        #设定蓝色上限
        mask = cv.inRange(hsv, lowerb=lower_hsv, upperb=upper_hsv)  #依据设定的上下限对目标图像进行二值化转换
        dst = cv.bitwise_and(src, src, mask=mask)    #将二值化图像与原图进行“与”操作；实际是提取前两个frame 的“与”结果，然后输出mask 为1的部分
                                                     #注意：括号中要写mask=xxx
        # cv.imshow('result', dst)                     #输出
        cv.imwrite('/home/luolu/PycharmProjects/BONC Cloudiip/dy106_1374665.jpg', dst)


src = cv.imread('/home/luolu/Downloads/data/bopian/阿布扎比薄片照片/image/dy106_1374665.png')   #导入目标图像，获取图像信息
color_seperate(src)
