# -*- coding:utf-8 -*-
import xlwt

# data = open("text2", "r", encoding="utf-8")
# data2 = open("相似内容.txt", "w", encoding="utf-8")
#
# all_data = []
# all_data_dict = {}
#
# for item in data.readlines():
#     all_data = eval(item)
#
# for item in all_data:
#     if item[0] not in all_data_dict.keys():
#         all_data_dict[item[0]] = item[1:]
#     else:
#         for id in item[1:]:
#             if id not in all_data_dict[item[0]]:
#                 all_data_dict[item[0]].append(id)
#
# print(all_data_dict)
# for item, value in all_data_dict.items():
#     data2.write(item)
#     data2.write(",")
#     for i in range(0, len(value)):
#         data2.write(value[i])
#         if i != len(value) - 1:
#             data2.write(",")
#     data2.write("\n"


import time

begin = time.time()


print(time.time()-begin)