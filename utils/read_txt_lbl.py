# -*- coding: utf-8 -*-
# @Time    : 2019/12/26 下午4:09
# @Author  : luolu
# @Email   : argluolu@gmail.com
# @File    : read_txt_lbl.py
# @Software: PyCharm

with open("/home/luolu/PycharmProjects/BONC Cloudiip/label.txt") as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content]
for file in content:
    print(file)
    file_name = file.split("____")[0]
    print("file_name: ", file_name)
    file_content = file.split("____")[1]
    print("file_content: ", file_content)
