# -*- coding: utf-8 -*-
# @Time    : 2019/12/25 上午9:10
# @Author  : luolu
# @Email   : argluolu@gmail.com
# @File    : generate_white_img.py
# @Software: PyCharm

import numpy as np
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageDraw, ImageFont
import matplotlib.font_manager as fm


img = Image.new('RGB', (800, 800), color='white')
d = ImageDraw.Draw(img)
root = tk.Tk()
# get a font
fonts = list(set([f.name for f in fm.fontManager.ttflist]))
fonts.sort()
combo = ttk.Combobox(root, value=fonts)
combo.pack()
font_type_1 = ImageFont.truetype(fm.findfont(fm.FontProperties(family=combo.get())), 48)
# font = ImageFont.truetype('/usr/share/fonts/truetype/ubuntu/ubuntu-B.ttf', 28)
d.text((300, 380), text="(0, 3)", fill=(0, 0, 0), font=font_type_1)
img.save('/home/luolu/PycharmProjects/BONC Cloudiip/label/1_0034.jpg', format="JPEG")
