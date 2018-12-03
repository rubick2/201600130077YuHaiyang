# -*- coding:utf-8 -*-
import re
import json
import math
from bs4 import BeautifulSoup
from hw3 import homework3

tweets = {}
q_list = {}
DF = {}
posting_list = {}
f = {}
sf = {}
cwd = {}
avdl = 30
b = 0.2
letters = re.compile(r'[a-zA-Z]+-?[a-zA-Z]+')


def get_q_list():
    with open('query171-225.txt', 'r', encoding='utf-8') as fp:
        t = BeautifulSoup(''.join(fp.readlines()), 'html.parser')

        for i in t.find_all('top'):
            # print(i.num.text[-4:-1], i.query.text)
            q_list.update({int(i.num.text[-4:-1]): i.query.text.strip().lower()})


def get_df():
    tweets_cnt = 0
    with open("tweets.json", 'r') as file:
        for line in file:
            res = json.loads(line)
            tweets.update({int(res['tweetId']): res, })
    for t_id in tweets:
        tweets_cnt += 1
        text = tweets[t_id]['text']
        str_text = text.replace('\n', ' ').strip().lower().split(' ')
        temp_list = []
        for word in str_text:
            if word not in temp_list:
                if word in DF:
                    DF[word] += 1
                else:
                    DF[word] = 1
                temp_list.append(word)
            try:
                cwd[word, t_id] += 1
            except Exception:
                cwd[word, t_id] = 1
    return tweets_cnt


def get_cwq(query_id: int):
    cwq = {}
    str_text = q_list[query_id].replace('\n', ' ').strip().lower().split(' ')
    for word in str_text:
        if word in cwq:
            cwq[word] += 1
        else:
            cwq[word] = 1
    q_words = q_list[query_id].replace('\n', ' ').strip().lower().split(' ')
    for word in q_words:
        if word not in cwq:
            cwq[word] = 0
    return cwq


def get_cwd(doc_id, query_id: int):
    cwd = get_cwq(query_id)
    for i in cwd:
        cwd[i] = 0
    str_text = tweets[doc_id]['text'].replace('\n', ' ').strip().lower().split(' ')
    for word in str_text:
        if word in cwd:
            cwd[word] += 1
    # print(cwd)
    q_words = q_list[query_id].replace('\n', ' ').strip().lower().split(' ')
    for word in q_words:
        if word not in cwd:
            cwd[word] = 0
    return cwd


def get_hw3(qq: str):
    hw3 = []
    pp = []
    haha = homework3.get_list()
    str_text = qq.replace('\n', ' ').strip().lower().split(' ')
    for word in str_text:
        ladd = []
        if word in haha:
            ladd += haha[word]
            ladd.pop(0)
            pp += ladd
    hw3 = list(set(pp))
    # print(hw3)
    return hw3


def get_long(t_id):
    ans = 0
    text = tweets[t_id]['text']
    str_text = text.replace('\n', ' ').strip().lower().split(' ')
    ans = len(str_text)
    return ans


def get_result():
    get_q_list()
    M = get_df()
    for q_id in q_list:
        cwq = get_cwq(q_id)
        rst_list = get_hw3(q_list[q_id])
        # print(rst_list)
        q_words = q_list[q_id].replace('\n', ' ').strip().lower().split(' ')
        # print(rst_list)
        f[q_id] = {}
        for i in range(len(rst_list)):
            # print(rst_list[i], "haha")
            tweet_l = get_long(rst_list[i])
            cwd = get_cwd(rst_list[i], q_id)
            ans = 0
            k = 8
            for word in q_words:
                if word not in DF:
                    DF[word] = math.e
            for q_word in q_words:
                ans += cwq[q_word]*(math.log(1+math.log(1+cwd[q_word]))/(1-b+b*(tweet_l/avdl)))*(math.log((M+1)/DF[q_word]))
                # vsm_f
                # ans += cwq[q_word]*((k+1)*cwd[q_word]/(cwd[q_word]+k*(1-b+b*(tweet_l/avdl))))*(math.log((M+1)/DF[q_word]))
                # bm
            f[q_id][rst_list[i]] = ans
        sf[q_id] = sorted(f[q_id].items(), key=lambda d: d[1], reverse=True)
    templine = []
    for s_id in sf:
        for i in range(len(sf[s_id])):
            templine.append("%s %s\n" % (s_id, sf[s_id][i][0]))
    with open('eval_hw4\\VSM_result.txt', 'w+') as file:
        file.writelines(templine)


get_result()
