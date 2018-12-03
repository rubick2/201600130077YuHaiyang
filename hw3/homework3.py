# -*- coding:utf-8 -*-
import os
import json

tweets = {}
word_doc = {}


def get_list():
    with open("tweets.json", 'r') as file:
        for line in file:
            res = json.loads(line)
            tweets.update({int(res['tweetId']): res, })
    for t_id in tweets:
        text = tweets[t_id]['text']
        str_text = text.replace('\n', ' ').strip().lower().split(' ')
        for word in str_text:
            if word in word_doc.keys():
                word_doc[word].append(t_id)
                word_doc[word][0] += 1
            else:
                word_doc[word] = [1, t_id, ]
    return word_doc
    # print(word_doc['happy'])
    # print(tweets)


def get_query():
    get_list()
    result_list = []
    q_word = input("Input 'A and B' or 'A not B':").strip().lower().split(' ')
    if q_word[1] == "and":
        print("and")
        a_list = word_doc[q_word[0]]
        b_list = word_doc[q_word[2]]
        a_num = a_list[0]
        b_num = b_list[0]
        i = 0
        j = 0
        while i <= a_num and j <= b_num:
            if a_list[i] > b_list[j]:
                j += 1
            elif a_list[i] < b_list[j]:
                i += 1
            elif a_list[i] == b_list[j]:
                result_list.append(a_list[i])
                i += 1
                j += 1
    elif q_word[1] == "not":
        a_list = word_doc[q_word[0]]
        b_list = word_doc[q_word[2]]
        a_num = a_list[0]
        b_num = b_list[0]
        i = 1
        j = 1
        while i <= a_num and j <= b_num:
            if a_list[i] > b_list[j]:
                j += 1
            elif a_list[i] < b_list[j]:
                result_list.append(a_list[i])
                i += 1
            elif a_list[i] == b_list[j]:
                i += 1
                j += 1
        if j > b_num and i <= a_num:
            k = i
            while k <= a_num:
                result_list.append(a_list[k])
                k += 1
    print("Number of query is ", len(result_list), "\nID list is:", result_list)


# get_query()

