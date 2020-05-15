# -*- coding:utf-8 -*-

file = open("suqiu", "r", encoding="utf-8")

word_dict = set()

for item in file.readlines():

    for item in item.split("\t"):
        word_dict.add(item.strip())

print(word_dict)

