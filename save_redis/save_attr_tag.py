#!/usr/bin/env python
# -*- coding: utf-8 -*-
import redis
import json
import redis
from django.conf import settings

REDIS_URL = "redis://redis.paas-test.env:6379/0"
redis_client = redis.StrictRedis.from_url(REDIS_URL)

suqiu_data = open("suqiu", "r", encoding="utf-8")
buwei_data = open("buwei", "r", encoding="utf-8")
fangshi_data = open("fangshi", "r", encoding="utf-8")

attr_key = "doris:save_attr_tag_by_name"

second_demands_tag = {}
first_demands_tag = {}
first_soultions_tag = {}
second_solutions_tag = {}
first_positions_tag = {}
second_positions_tag = {}

#
# for data in suqiu_data:
#     item = data.replace('"', '').strip().split(":")
#
#     if item[0] not in second_demands_tag.keys():
#         second_demands_tag[item[0]] = [item[1]]
#
#     else:
#         second_demands_tag[item[0]].append(item[1])
#
#     if item[1] not in first_demands_tag.keys():
#         first_demands_tag[item[1]] = [item[0]]
#
#     else:
#         first_demands_tag[item[1]].append(item[0])



# for data in buwei_data:
#     item = data.replace('"', '').strip().split(":")
#
#     if item[0] not in second_positions_tag.keys():
#         second_positions_tag[item[0]] = [item[1]]
#
#     else:
#         second_positions_tag[item[0]].append(item[1])
#
#     if item[1] not in first_positions_tag.keys():
#         first_positions_tag[item[1]] = [item[0]]
#
#     else:
#         first_positions_tag[item[1]].append(item[0])


for data in fangshi_data:
    item = data.replace('"', '').strip().split(":")

    if item[0] not in second_solutions_tag.keys():
        second_solutions_tag[item[0]] = [item[1]]

    else:
        second_solutions_tag[item[0]].append(item[1])

    if item[1] not in first_soultions_tag.keys():
        first_soultions_tag[item[1]] = [item[0]]

    else:
        first_soultions_tag[item[1]].append(item[0])

print(second_solutions_tag)
print(first_soultions_tag)



# ss = redis_client.hset(attr_key, "second_demands_tag", json.dumps(second_demands_tag))
# sss = redis_client.hset(attr_key, "first_demands_tag", json.dumps(first_demands_tag))
#
# first_soultions_tag = redis_client.hset(attr_key, "first_soultions_tag", json.dumps(first_soultions_tag))
# second_solutions_tags = redis_client.hset(attr_key, "second_solutions_tag", json.dumps(second_solutions_tag))
#
# first_positions_tag = redis_client.hset(attr_key, "first_positions_tag", json.dumps(first_positions_tag))
# second_positions_tag = redis_client.hset(attr_key, "second_positions_tag", json.dumps(second_positions_tag))

sss = redis_client.hget(attr_key,"second_solutions_tag")
# print(sss)
for item, values in sss.items():
    # print(item)
    # print(json.loads(values))
    values = json.loads(values)
    if values.get('祛痘', []):
        print(str(item, encoding="utf-8"))

# {"terms": {"first_demands": first_demands_name_list}},
# {"terms": {"second_demands": second_demands_name_list}},
# {"terms": {"first_solutions": first_solutions_name_list}},
# {"terms": {"second_solutions": second_solutions_name_list}},
# {"terms": {"positions": first_positions_name_list}},
# {"terms": {"second_positions": second_positions_name_list}}