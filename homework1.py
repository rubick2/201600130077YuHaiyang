# -*- coding:utf-8 -*-
import os

m = {}
f = open('49960', 'rb')
str_a = f.read()
dic_a = str_a.split()

for word in dic_a:
    if word in m:
        m[word] = m[word]+1
    else:
        m[word] = 1
for i in m:
    print(i, ":", m[i])