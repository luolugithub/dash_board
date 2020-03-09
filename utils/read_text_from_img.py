# -*- coding: utf-8 -*-
# @Time    : 2019/12/26 下午5:13
# @Author  : luolu
# @Email   : argluolu@gmail.com
# @File    : read_text_from_img.py
# @Software: PyCharm
import glob
import cv2 as cv
import numpy as np
import csv

try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract


def ocr_core(filename):
    """
    This function will handle the core OCR processing of images.
    """
    text = pytesseract.image_to_string(Image.open(
        filename))  # We'll use Pillow's Image class to open the image and pytesseract to detect the string in the image
    return text.replace("\n", " ").strip()


# print(ocr_core('../images/gen.jpg'))
if __name__ == '__main__':
    f = open('/home/luolu/PycharmProjects/BONC Cloudiip/submit_bonc.csv', 'w')

    for filename in glob.glob('/home/luolu/PycharmProjects/BONC Cloudiip/label/*.jpg'):
        img = cv.imread(filename)
        # print(filename)
        base_name = cv.os.path.basename(filename)
        print(base_name)
        f.write(base_name + ';' + ocr_core(filename) + '\n')

    f.close()
