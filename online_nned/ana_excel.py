# -*- coding: utf-8 -*-

data = open("excel", "r", encoding="utf-8")

data_list = []
for item in data.readlines():
    data_list.append(item.strip())

print(data_list)