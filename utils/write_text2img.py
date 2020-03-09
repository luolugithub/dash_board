# -*- coding: utf-8 -*-
# @Time    : 2019/12/26 下午4:19
# @Author  : luolu
# @Email   : argluolu@gmail.com
# @File    : write_text2img.py
# @Software: PyCharm
import numpy as np
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageDraw, ImageFont
import matplotlib.font_manager as fm


with open("/home/luolu/PycharmProjects/BONC Cloudiip/label.txt") as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content]

if __name__ == '__main__':
    for file in content:
        print(file)
        file_name = file.split("____")[0]
        print("file_name: ", file_name)
        file_content = file.split("____")[1]
        print("file_content: ", file_content)
        img = Image.new('RGB', (800, 800), color='white')
        d = ImageDraw.Draw(img)                                                                   
        root = tk.Tk()
        font = ImageFont.truetype('../91bold.ttf', 180)
        # get a font
        # fonts = list(set([f.name for f in fm.fontManager.ttflist]))
        # fonts.sort()
        # combo = ttk.Combobox(root, value=fonts)
        # combo.pack()
        # font_type_1 = ImageFont.truetype(fm.findfont(fm.FontProperties(family=combo.get())), 420)
        # font = ImageFont.truetype('/usr/share/fonts/truetype/ubuntu/ubuntu-B.ttf', 28)
        d.text((0, 300), text=file_content, fill=(0, 0, 0), font=font)
        img.save('/home/luolu/PycharmProjects/BONC Cloudiip/label/' + file_name, format="JPEG")
