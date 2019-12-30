# -*- coding: utf-8 -*-
# @Time    : 2019/12/25 上午10:35
# @Author  : luolu
# @Email   : argluolu@gmail.com
# @File    : get_filename.py
# @Software: PyCharm
import glob
import os

if __name__ == '__main__':
    with open('/home/luolu/PycharmProjects/BONC Cloudiip/label.txt', 'w') as f:
        for filename in glob.glob('/home/luolu/PycharmProjects/BONC Cloudiip/image/*.jpg'):
            print(filename)
            base_name = os.path.basename(filename)
            print(base_name, file=f)
