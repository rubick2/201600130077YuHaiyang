# -*- coding:utf-8 -*-
import os
import re


def collect():
    word_bag = {}
    f_stop = []
    word_dic = {}
    templine = []
    letters = re.compile(r'[a-zA-Z]+-?[a-zA-Z]+')

    ff_stop = open("stopword", "rb")
    for stop_line in ff_stop:
        str_stop = str(stop_line).strip()
        for sword in re.findall(letters, str_stop):
            f_stop.append(sword)

    root_1dir = r"D:\program\python\IRandDM\work1\20news-18828"
    for pack in os.listdir(root_1dir):
        root_dir = root_1dir + "\\" + pack

        for file in os.listdir(root_dir):
            file_name = root_dir + "\\" + file
            ff = open(file_name, "rb")
            for line in ff:
                str_line = str(line).strip().lower()
                for word in re.findall(letters, str_line):
                    if word not in f_stop:
                        if word in word_dic:
                            word_dic[word] += 1
                        else:
                            word_dic[word] = 1

    for k, v in word_dic.items():
        if v >= 3:
            word_bag[k] = v
            templine.append("%s\t%s\n" % (k, v))

    with open('wordbag.txt', 'w+') as file_two:
        file_two.writelines(templine)

    print(word_bag)
    print(len(word_bag))

    return word_bag


collect()
