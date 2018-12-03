# -*- coding:utf-8 -*-
import os
import re
import math

letters = re.compile(r"\w+")
p_word = {}
test_set = []
train_set = []


def cal_word():
    word_sum = 0
    word_bag = open("word_bag.txt", "r")
    for line in word_bag:
        word_sum = word_sum + int(line.split()[1])
        p_word[line.split()[0]] = line.split()[1]
    return word_sum


def cal_word_class():
    class_word_num = {}
    root_dir = r"20news-18828"
    for pack in os.listdir(root_dir):
        class_dir = root_dir + "\\" + pack
        word_num = 0
        for file in os.listdir(class_dir):
            file_name = class_dir + "\\" + file
            ff = open(file_name, "rb")
            for line in ff:
                str_line = str(line).strip().lower()
                for word in re.findall(letters, str_line):
                    if word in p_word:
                        word_num += 1
        class_word_num[pack] = word_num
    return class_word_num


def get_set():
    train_num = {}
    file_list = []
    root_1dir = r"20news-18828"
    for pack in os.listdir(root_1dir):
        class_dir = root_1dir + "\\" + pack
        for file in os.listdir(class_dir):
            file_list.append(file)
        len_class_doc = len(file_list)
        train_num[pack] = len_class_doc
        file_list.clear()
        num_doc = 0
        for file in os.listdir(class_dir):
            file_name = class_dir + "\\" + file
            num_doc += 1
            if num_doc <= train_num[pack]/5:
                test_set.append(file_name)
                train_set.append(file_name)
            else:
                train_set.append(file_name)


def get_word_class():
    word_class = {}
    root_dir = r"20news-18828"
    for pack in os.listdir(root_dir):
        class_dir = root_dir + "\\" + pack
        for file in os.listdir(class_dir):
            file_name = class_dir + "\\" + file
            ff = open(file_name, "rb")
            for line in ff:
                str_line = str(line).strip().lower()
                for word in re.findall(letters, str_line):
                    if word in p_word:
                        if (pack, word) not in word_class:
                            word_class[pack, word] = 1
                        else:
                            word_class[pack, word] += 1
    return word_class


def get_result():
    global c
    p_doc = {}
    word_sum = cal_word()
    class_word_num = cal_word_class()
    word_class = get_word_class()
    doc_word = []
    cnt = 0
    all_cnt = len(test_set)
    root_1dir = r"20news-18828"
    for test_file in test_set:
        test_ff = open(test_file, "rb")
        for line in test_ff:
            str_line = str(line).strip().lower()
            for word in re.findall(letters, str_line):
                if word in p_word:
                    doc_word.append(word)
        for pack in os.listdir(root_1dir):
            p_doc[test_file, pack] = 0
            for test_word in doc_word:
                if (pack, test_word) in word_class:
                    p_doc[test_file, pack] += math.log((word_class[pack, test_word]+4)/class_word_num[pack]+1)
                    p_doc[test_file, pack] -= math.log(int(p_word[test_word])/word_sum)
                else:
                    p_doc[test_file, pack] += math.log(4/class_word_num[pack]+1)
                    p_doc[test_file, pack] -= math.log(int(p_word[test_word])/word_sum)
        # result = max(p_doc, key=p_doc.get())
        a = -999999
        for p_key in p_doc:
            if p_doc[p_key] > a:
                a = p_doc[p_key]
                c = str(p_key).split(',')[1]
        if c.split('\'')[1] == str(test_file).split('\\')[1]:
            cnt += 1.0
        doc_word.clear()
        p_doc.clear()
    rate = cnt / all_cnt
    print('%.2f%%' % (rate * 100))


get_set()
get_result()
