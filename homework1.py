# -*- coding:utf-8 -*-
import os
import re

word_list = list()
root_dir = r"D:\program\python\IRandDM\work1\alt.atheism"
for file in os.listdir(root_dir):
    file_name = root_dir + "\\" + file
    ff = open(file_name, "rb")

    letters = re.compile(r'[a-zA-Z]+-?[a-zA-Z]+')

    for line in ff:
        str_line = str(line).strip().lower()
        for word in re.findall(letters, str_line):
            if word not in word_list:
                word_list.append(word)
print(word_list)