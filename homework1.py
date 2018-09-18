# -*- coding:utf-8 -*-
import os
import re

word_list = list()
root_1dir = r"D:\program\python\IRandDM\work1\20news-18828"
for pack in os.listdir(root_1dir):
    root_dir = root_1dir + "\\" + pack

    for file in os.listdir(root_dir):
        file_name = root_dir + "\\" + file
        ff = open(file_name, "rb")

        letters = re.compile(r'[a-zA-Z.@0-9]+-?[a-zA-Z0-9]+')

        for line in ff:
            str_line = str(line).strip().lower()
            for word in re.findall(letters, str_line):
                word_list.append(word)

print(word_list)
print(len(set(word_list)))