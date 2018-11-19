# -*- coding:utf-8 -*-
import os
import re
import math

f_stop = []
templine = []
IDF = {}
TF = {}
DF = {}
w = {}
letters = re.compile(r'[a-zA-Z]+-?[a-zA-Z]+')


def get_df(file):

    tdic = {}
    ff = open(file, "rb")
    for line in ff:
        str_line = str(line).strip().lower()
        for word in re.findall(letters, str_line):
            if word not in f_stop:
                if word in tdic:
                    tdic[word] += 1
                else:
                    tdic[word] = 1
    for word in tdic:
        if word in DF:
            DF[word] += 1
        else:
            DF[word] = 1
    return tdic


def get_tf():
    num_doc = 0
    root_1dir = r"20news-18828"
    for pack in os.listdir(root_1dir):
        root_dir = root_1dir + "\\" + pack
        for file in os.listdir(root_dir):
            file_name = root_dir + "\\" + file
            num_doc += 1
            cword = get_df(file_name)
            for k in cword:
                if cword[k] > 0:
                    TF[k, pack + "\\" + file] = 1.0 + math.log(cword[k])
                else:
                    TF[k, pack + "\\" + file] = 0
    return num_doc


def get_idf():
    N = get_tf()
    for word in DF:
        IDF[word] = math.log(N / DF[word])


def get_w():
    for k1, k2 in TF:
        w[k1, k2] = TF[k1, k2] * IDF[k1]
        templine.append("%s\t%s\t%s\n" % (k1, k2, w[k1, k2]))
    with open('vsm.txt', 'w+') as file:
        file.writelines(templine)


def get_stop():
    ff_stop = open("stopword", "rb")
    for stop_line in ff_stop:
        str_stop = str(stop_line).strip()
        for sword in re.findall(letters, str_stop):
            f_stop.append(sword)


get_stop()
get_idf()
get_w()
