# -*- coding:utf-8 -*-
import os
import re

m = []
root_dir = r"D:\program\python\IRandDM\work1\alt.atheism"

for file in os.listdir(root_dir):
    file_name = root_dir + "\\" + file
    ff = open(file_name, "rb")

    str_a = ff.read()
    dic_a = str_a.split()

    for word in dic_a:
        word_a = re.sub(r'\D', "", word.decode())
        if word_a not in m:
            m.append(word_a)
        print(word_a)