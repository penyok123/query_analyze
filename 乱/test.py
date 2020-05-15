# # # q = {}
# # #
# # # q["query"] = {
# # #     "bool": {
# # #         "must": [{
# # #             "term": {
# # #                 "is_online": False
# # #             }
# # #         }, {
# # #             "term": {
# # #                 "is_deleted": False
# # #             }
# # #         }, {
# # #             "range": {
# # #                 "topic_id_list": {
# # #                     "gte": 0
# # #                 }
# # #
# # #             }
# # #         }]
# # #     }
# # # }
# # # should_list = []
# # # all_tag = [1, 2, 3, 4, 5]
# # # for tag_name in all_tag:
# # #     should_list.append({
# # #         "multi_match": {
# # #             "query": tag_name,
# # #             "type": "best_fields",
# # #             "operator": "and",
# # #             "fields": ["edit_tag_name"],
# # #         }
# # #     })
# # #
# # # q["query"]["bool"]["should"] = should_list
# # #
# # # print(q)
# # import datetime
# # import time
# #
# # # days2 = 7
# # #
# # # now = datetime.datetime.now()
# # # yesterday2 = now - datetime.timedelta(days=days2)
# # #
# # # yesterday_begin_time = "%s-%s-%s %s:%s:%s" % (
# # #     yesterday2.year, yesterday2.month, yesterday2.day, yesterday2.hour, yesterday2.minute, yesterday2.second)
# # # yesterday_end_time = "%s-%s-%s %s:%s:%s" % (
# # #     now.year, now.month, now.day, now.hour, now.minute, now.second)
# # #
# # # print(yesterday_begin_time)
# # # print(yesterday_end_time)
# # #
# # # formatStr = "%Y-%m-%d %H:%M:%S"
# # # tm_begin = time.strptime(yesterday_begin_time, formatStr)
# # # tm_end = time.strptime(yesterday_end_time, formatStr)
# # # yesterday_begintime = time.mktime(tm_begin)
# # # yesterday_endtime = time.mktime(tm_end)
# # #
# # # print(yesterday_begintime)
# # # print(yesterday_endtime)
# #
# # import math
# #
# # expert_pv_30 = 1113
# # expert_exposure_pv_30 = 4460
# # expert_message_num_30 = 143
# #
# # organization_pv_30 = 6678
# # expert_pv_30 = 222
# # service_pv_30 = 7583
# # doctor_discount_30_days = 130340
# # doctor_ad_money_30_days = 29470
# #
# # consult = 1.0 * expert_message_num_30 / (service_pv_30 + expert_pv_30 + organization_pv_30)
# # ctr = 1.0 * expert_pv_30 / expert_exposure_pv_30
# # commission = 1.0 * doctor_ad_money_30_days / (service_pv_30 + expert_pv_30 + organization_pv_30)
# # cpt = 1.0 * doctor_discount_30_days / (service_pv_30 + expert_pv_30 + organization_pv_30)
# # ss = math.sqrt(consult) * math.sqrt(ctr) * (commission + 0.7 * cpt)
# #
# # print(ss)
# #
# #
# # def time_conv_minute(minutest, minutest2):
# #     try:
# #         now = datetime.datetime.now()
# #         minute = datetime.datetime.now().minute
# #         yes_time = now - datetime.timedelta(minutes=minutest)
# #         yes_time2 = now - datetime.timedelta(minutes=minutest2)
# #         return yes_time, yes_time2, minute
# #     except:
# #         return None
# #
# #
# # s, m, l = time_conv_minute(240, 0)         "refs/remotes/origin/test", but not yet merged to HEAD.
# # print(s)
# # print(m)
# # print(l)
# #
# # "SELECT  pictorial_id ,count(*) as count FROM community_pictorial_topic WHERE is_online=1 and create_time >= "2019-09-17 14:00:00.240806" and create_time < "2019-09-17 18:00:00.240806" group by pictorial_id "
#
# #
# # import math
# #
# # print(math.sqrt(-100)
# # # im)
# # import redis
# # import json
# #
# # REDIS_URL = "redis://127.0.0.1:6379/1"
# # redis_client = redis.StrictRedis.from_url(REDIS_URL)
# # redis_key1 = "cybertron:set_reply_id:three"
# # have_reply1 = redis_client.get(redis_key1)
# # print(have_reply1)
# # result = json.loads(str(have_reply1, encoding="utf-8"))
#
# #
# # user_portrait = [{"tag_score": 831.6111111111107, "tag2": 37, "weight": 41.86278046720529},
# #                  {"tag_score": 190.73888888888888, "tag2": 66, "weight": 9.601675741736653},
# #                  {"tag_score": 153.205, "tag2": 1055, "weight": 7.712243374080259},
# #                  {"tag_score": 140.22222222222217, "tag2": 221, "weight": 7.058698503522356},
# #                  {"tag_score": 106.46666666666664, "tag2": 893, "weight": 5.359465060281397},
# #                  {"tag_score": 89.97222222222221, "tag2": 22, "weight": 4.529145097644397},
# #                  {"tag_score": 54.26166666666666, "tag2": 1233, "weight": 2.731498183587687},
# #                  {"tag_score": 53.89444444444444, "tag2": 2663, "weight": 2.71301244780786},
# #                  {"tag_score": 47.63333333333333, "tag2": 117, "weight": 2.3978320510776823},
# #                  {"tag_score": 43.25388888888889, "tag2": 15, "weight": 2.1773735712707616}]
# #
# # all_score = 0
# # for item in user_portrait:
# #     tag_score = item.get("tag_score", 0)
# #     all_score += tag_score
# #
# # tag_id_size = dict()
# #
# # all_size = 0
# # for item in user_portrait:
# #     if round(item.get("tag_score", None) / all_score * 20) > 8:
# #         tag_id_size[item.get("tag2", None)] = 8
# #         all_size += 8
# #     else:
# #         tag_id_size[item.get("tag2", None)] = round(item.get("tag_score", None) / all_score * 20)
# #         all_size += round(item.get("tag_score", None) / all_score * 20)
# #
# # print(all_size)
# # print(all_score)
# # print(tag_id_size)
#
# import itertools
# from itertools import chain
#
# #
# # string = chain.from_iterable("ABCD")
# # print(string.next())
# # print(string.next())
# # print(string.next())
# #
# #
# # from itertools import izip
# #
# # for item in izip("ABCD", "xy"):
# #     print(item)
# #
# # for item in izip([1, 2, 3], ["a", "b", "c", "d", "e"]):
# #     print(item)
#
# # ss =filter(lambda a: itertools.chain.from_iterable(itertools.izip_longest("1234")))
# # print(ss)
# from collections import deque, OrderedDict
#
#
# def variousness(items, variety_size):
#     src = deque(items)
#     dst = []
#     while len(src) > 0:
#         pos, temp, recover, dup = 0, [], [], []
#         while pos < variety_size:
#             try:
#                 item = src.popleft()
#                 if item.get("group") in dup:
#                     recover.append(item)
#                 else:
#                     temp.append(item)
#                     dup.append(item.get("group"))
#                     pos += 1
#             except IndexError:
#                 diff = variety_size - pos
#                 diff, remain = recover[:diff], recover[diff:]
#                 temp.extend(diff)
#                 recover = remain
#                 break
#         multi = OrderedDict()
#         for key in dup:
#             multi[key] = []
#         for item in temp:
#             multi[item.get("group")].append(item)
#         temp = filter(lambda a: a != None, itertools.chain.from_iterable(itertools.izip_longest(*multi.values())))
#
#         dst.extend(temp)
#         src.extendleft(reversed(recover))
#
#     return dst
# #
# import hashlib
#
#
# #
# def recommed_service_category_device_id(device_id):
#     try:
#
#         categroy_select_cary = ["0", "1", "2", "3", "4", "a", "b", "c"]
#         if not device_id:
#             return False
#
#         hd_id = hashlib.md5(str(device_id).encode()).hexdigest()
#         print(hd_id)
#         return hd_id[-1] in categroy_select_cary
#     except:
#         return False
#
#
# s = recommed_service_category_device_id("867961035707277")
# print(s)
# #
# ss = [{"tag_score": 159.9986111111111, "tag2": 15, "weight": 22.311205280364426},
#       {"tag_score": 88.80326388888889, "tag2": 221, "weight": 12.383281557459604},
#       {"tag_score": 88.1664947089947, "tag2": 1055, "weight": 12.294486487363887},
#       {"tag_score": 83.10277777777777, "tag2": 2663, "weight": 11.588370183294344},
#       {"tag_score": 48.810972222222226, "tag2": 22, "weight": 6.8065067166607305},
#       {"tag_score": 33.84733796296296, "tag2": 873, "weight": 4.719884130501027},
#       {"tag_score": 28.09193452380952, "tag2": 117, "weight": 3.9173147412386817},
#       {"tag_score": 21.069444444444443, "tag2": 38, "weight": 2.938054879843821},
#       {"tag_score": 19.017407407407408, "tag2": 872, "weight": 2.651906023561252},
#       {"tag_score": 17.83611111111111, "tag2": 154, "weight": 2.487178692613998}]
#
# count = 0
#
# for item in ss:
#     count += item.get("tag_score", 0)
# print(88 / count * 20)
# s = sorted(sss, key=lambda k: (k.get("tag2", 0)), reverse=False)
#
#
# print(sss)
#
# print("----------------")
# print(s)

# ls = [1, 2, 3, 4, 5]
# print(ls[-1])
# query="ssss"
# q={"bool":{
#     "should":[]
# }}
# nested_fields = {
#     "services.name": 2.5,
# }
# service_fields = ["^".join((k, str(v))) for (k, v) in nested_fields.iteritems()]
#
# print(service_fields)
# for  sf in service_fields:
#     q["bool"]["should"].append({
#         "vest": {
#             "path": sf.split(".")[0],
#             "score_mode": "sum",
#             "query": {
#                 "multi_match": {
#                     "query": query,
#                     "fields": sf,
#                     "operator": "and",
#                     "type": "best_fields"
#                 }
#             },
#             "boost": 5,
#
#         },
#     })
#
# print(q)
# print("\xe5\x90\xb8\xe8\x84\x82")
#
# print("\xe4\xbd\x95")
# ss = {"6144": 554.09999999999980003, "2033": 117.79478874883287, "61": 61.95844615624026, "2059": 75.78333333333332,
#       "66": 48.55833333333333, "187": 66.91111111111111, "15": 176.0999553142936, "21": 49.92738095238094,
#       "221": 82.12395541549952, "1055": 135.68497474747474, "117": 6}
#
# count = 0
#
# for item in ss.items():
#     count += item[1]
#
# for item in ss.items():
#     print(item[0])
#
#     print(round(item[1] / count * 20))
#     print("------------")
#
# print(count)
#
#
# print("\xe5\x81\x87\xe4\xbd\x93\xe9\x9a\x86\xe8\x83\xb8")

# offset = 20
# size = 10
#
# weight_dic = {  # 权重字典，类型：(日记本，专栏，回答, 用户帖)
#     "diary": {
#         "diary": {"diary_real_size": 3, "diary_real_offset": int(offset / 5 + offset / 10)},
#         "qa": {"answer_real_size": 2, "answer_real_offset": int(offset / 5)},
#         "article": {"article_real_size": 2, "article_real_offset": int(offset / 5)},
#         "tractate": {"tractate_real_size": 3, "tractate_real_offset": int(offset / 5 + offset / 10)},
#     },
#     "topic": {
#         "diary": {"diary_real_size": 2, "diary_real_offset": int(offset / 5)},
#         "qa": {"answer_real_size": 2, "answer_real_offset": int(offset / 5)},
#         "article": {"article_real_size": 3, "article_real_offset": int(offset / 5 + offset / 10)},
#         "tractate": {"tractate_real_size": 3, "tractate_real_offset": int(offset / 5 + offset / 10)},
#     },
#     "question": {
#         "diary": {"diary_real_size": 2, "diary_real_offset": int(offset / 5)},
#         "qa": {"answer_real_size": 3, "answer_real_offset": int(offset / 5 + offset / 10)},
#         "article": {"article_real_size": 2, "article_real_offset": int(offset / 5)},
#         "tractate": {"tractate_real_size": 3, "tractate_real_offset": int(offset / 5 + offset / 10)},
#     },
#     "tractate": {
#         "diary": {"diary_real_size": 3, "diary_real_offset": int(offset / 5 + offset / 10)},
#         "qa": {"answer_real_size": 2, "answer_real_offset": int(offset / 5)},
#         "article": {"article_real_size": 2, "article_real_offset": int(offset / 5)},
#         "tractate": {"tractate_real_size": 3, "tractate_real_offset": int(offset / 5 + offset / 10)},
#     },
#     "dilute_rate": 2  # 放大比例
# }
#
# card_type = "question"
# weight_size = weight_dic.get(card_type, None)
#
# answer_weight_size = weight_size.get("qa", None)
# diary_weight_size = weight_size.get("diary", None)
# tractate_weight_size = weight_size.get("tractate", None)
# article_weight_size = weight_size.get("article", None)
#
#
# answer_real_size = answer_weight_size.get("answer_real_size", None)
# diary_real_size = diary_weight_size.get("diary_real_size", None)
# tractate_real_size = tractate_weight_size.get("tractate_real_size", None)
# article_real_size = article_weight_size.get("article_real_size", None)
#
# answer_real_offset =answer_weight_size.get("answer_real_offset", None)
# diary_real_offset =diary_weight_size.get("diary_real_offset", None)
# tractate_real_offset =tractate_weight_size.get("tractate_real_offset", None)
# article_real_offset =article_weight_size.get("article_real_offset", None)
#
#
# print(answer_weight_size)
# print(diary_weight_size)
# print(tractate_weight_size)
# print(article_weight_size)
#
# print(answer_real_size)
# print(diary_real_size)
# print(tractate_real_size)
# print(article_real_size)
#
#
# print(answer_real_offset)
# print(diary_real_offset)
# print(tractate_real_offset)
# print(article_real_offset)
#


# weight_dic = {  # 权重字典，类型：(日记本，专栏，回答, 用户帖)
#     "diary": {
#         "diary": [0, 3, 7],
#         "qa": [2, 5],
#         "article": [6, 9],
#         "tractate": [1, 4, 8],
#     },
#     "topic": {
#         "diary": [2, 5],
#         "qa": [6, 9],
#         "article": [0, 3, 7],
#         "tractate": [1, 4, 8],
#     },
#     "question": {
#         "diary": [2, 5],
#         "qa": [0, 3, 7],
#         "article": [6, 9],
#         "tractate": [1, 4, 8],
#     },
#     "tractate": {
#         "diary": [1, 4, 8],
#         "qa": [2, 5],
#         "article": [6, 9],"[\"\\u53cc\\u773c\\u76ae\"]"
#         "tractate": [0, 3, 7],
#     },
#     "dilute_rate": 2  # 放大比例
# }
# iary_ids = [1, 2, 3, 4, 5, 6]
# print(iary_ids[:10])

# tag = {"new_tags": [], "tags": [{"type": "4", "id": 1801}, {"type": "2", "id": 5147}, {}]}
#
# for key, val in tag.items():
#     if len(val) > 0:
#         if key == "tags":
#             print(val)
#             print([item["id"] for item in val if len(item) > 0])
#         if key == "new_tags":
#             new_all_tags = [item["id"] for item in val if len(item) > 0]
#
# # print(all_tags)
# # print(new_all_tags)


# s = {"diary": {
#     "diary": [0, 3, 7],
#     "qa": [2, 5],
#     "article": [6, 9],
#     "tractate": [1, 4, 8],
# # }}
# tag_data = [1, 2, 3, 4, 5]
# office_data = [6, 7, 8, 9, 10]
# have_office_tag_data = [21, 22, 23, 24, 25]
# have_office_data = [26, 27, 28, 29, 30, 1, 2, 3, 4, 4, 55, 6, 7]
#
# for item in range(0, len(have_office_data), 4):
#     if item == 4:
#         print(have_office_data[0:item])
#     else:
#         print(have_office_data[item - 4:item])
# == == == == == == == == == == == == == == ==
# for item in range(0, len(ids), 1000):
#     if item == 1000 or item == 0:
#         write_to_es("service", ids[0:item], None, es_config=False)
#     else:
#         write_to_es("service", ids[item-1000:item], None, es_config=False)
# == == == == == == == == == == == == == == ==

# import random
#
# random.shuffle(have_office_data)
# print(have_office_data[:100])
# two_type_tags = []
# san_type_tags = []
# all_tags = []
# val = [{"id": 1, "type": 2}, {"id": 23, "tag_type": 3}, {"id": 3424, "tag_type": 2}, {"id": 33, "type": 3}]
# for item in val:
#     if "tag_type" in item.keys() and item.get("tag_type", None) == 2:
#         two_type_tags.append(item["id"])
#     if "type" in item.keys() and item.get("type", None) == 2:
#         two_type_tags.append(item["id"])
#     if "tag_type" in item.keys() and item.get("tag_type", None) == 3:
#         san_type_tags.append(item["id"])
#     if "type" in item.keys() and item.get("type", None) == 3:
#         san_type_tags.append(item["id"])
#     if "tag_type" in item.keys() and item.get("tag_type", None) != 4:
#         all_tags.append(item["id"])
#     if "type" in item.keys() and item.get("type", None) != 4:
#         all_tags.append(item["id"])
#
# print(two_type_tags)
# print(san_type_tags)
# print(all_tags)
import datetime
from pytz import timezone
#
# TIME_ZONE = "UTC"
#
#
# def tzlc(dt, truncate_to_sec=False):
#     if dt is None:
#         return None
#     if truncate_to_sec:
#         dt = dt.replace(microsecond=0)
#     return timezone(TIME_ZONE).localize(dt)
# import datetime
#
# now = datetime.now().getMillis()

import datetime, time

#
# now = int(time.time())  # 1533952277
# print(now)
# timeArray = time.localtime(now)
# print(timeArray)
# otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
# print(otherStyleTime)
#
# query = {
#     "sort": {
#         "_script": {
#             "order": "desc",
#             "type": "number",
#             "script": {
#                 "lang": "painless",
#                 "source":
#                     "def can_sold=False; if (doc[\u0027start_time\u0027].size() > 0 && doc[\u0027is_can_be_sold\u0027].value == can_sold ){if (doc[\u0027start_time\u0027].value.toInstant().toEpochMilli() <= params.now &&  params.now < doc[\u0027end_time\u0027].value.toInstant().toEpochMilli() ) {return 1111}else{return 0}}else{return 0}",
#                 "params": timeArray
#             }
#         }
#     }
# }
#
# print(query)
#
# timeStamp =int(time.time())
# print(timeStamp)
# # timeArray = time.localtime(timeStamp)
# # otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
# # print(otherStyleTime)


# or_filters = [{"tag_ids": []}]
#
# if or_filters:
#     tag_ids = [item.get("tag_ids", []) for item in or_filters][0]
#
# print(tag_ids)
#
# sss = []
#
# s = [{"sku_id": v, "pos": s} for val in sss for v, s in val.items()]
#
# print(s)

# import base64
#
# name = "北京精艺吉美整形"
# query_base64 = base64.b64encode(name.encode('utf8')).decode('utf8')
# print(
#     query_base64
# )
#
# import math
#
# print(math.log(1 + 2609.5 / 466.5))
#
# print(math.log(1 + ((3074 - 255 + 0.5) / 255.5)))
#
#
# print(8.0*7.3109827*0.012449548)
# print(7.3484693*7.3109827*1)
#
# print(8.0*2.4878378* 1.9411767)

import redis
import json
#
# REDIS_URL = 'redis://redis.paas-test.env:6379'
# tractate_user_id = [32270075, 32270029, 32270036, 32270040, 32270051, 32270061, 32270065, 32270071, 32270081, 32270085,
#                     32269972, 32269979, 32269983, 32269988, 32269995, 32270002, 32270005, 32270011, 32270016, 32270022,
#                     32269913, 32269918, 32269920, 32269927, 32269933, 32269939, 32269943, 32269948, 32269957, 32269965,
#                     32270003, 32270004, 32270007, 32270012, 32270015, 32270017, 32270020, 32270024, 32270027, 32270031,
#                     32269952, 32269956, 32269962, 32269966, 32269973, 32269978, 32269980, 32269982, 32269987, 32269989]
#
# redis_client = redis.StrictRedis.from_url(REDIS_URL)
# key = "good_tractate_user_id"
# redis_client.set(key, tractate_user_id)

# user_ids = json.loads(redis_client.get(key))
# print(user_ids)
# print(type(user_ids))

# sss = {"hits": {"total": {"value": 10000}}}
#
# if "value" in sss["hits"]["total"].keys():
#     print(sss['hits']["total"]['value'])

# print("get action:comment,card_id:%s,redis_data:%s" % (key, user_ids))
from dateutil import rrule
from datetime import datetime
import time

# 计算日期差
# untilYear = 2018
# untilMonth = 5
# untilDay = 1
#
# # 2018年第一天
# firstDay = datetime(untilYear, 1, 1)
# endDay = datetime(untilYear, untilMonth, untilDay)
#
# # rrule.DAILY计算天差，此外还有  星期(WEEKLY)，年（YEARLY）
# days = rrule.rrule(freq=rrule.DAILY, dtstart=firstDay, until=endDay)
#
# print('相差:', days.count(), '天')
#
#
# import random
# action_num = random.randint(1, 3)
# print(action_num)
# res = {"took": 5, "timed_out": False, "_shards": {"total": 8, "successful": 8, "failed": 0},
#        "hits": {"total": {"value": 1, "action": "gt"}, "max_score": 3.8578942, "hits": [
#            {"_index": "gm_test-service", "_type": "service", "_id": "5740426", "_score": 3.8578942,
#             "_source": {"query_pv": [], "rating": 0, "smart_rank_v4": 0,
#                         "short_description_by_standard_analyzer": "牙齿冷光美白", "is_online": False,
#                         "closure_tag_ids": [5099, 1098, 11, 5098, 917, 54, 1079, 761, 5802, 2363, 662],
#                         "start_time_long": 1572835852, "is_sink": False, "sku_list": [
#                     {"sku_id": 10378, "sku_rank": 0, "end_time": "2029-11-04T10:50:52+08:00", "price_type": 0,
#                      "start_time": "2019-11-04T10:50:52+08:00", "name_by_standard_analyzer": "牙齿冷光美白---1", "price": 500,
#                      "name": "牙齿冷光美白---1"},
#                     {"sku_id": 10379, "sku_rank": 0, "end_time": "2029-11-04T10:50:52+08:00", "price_type": 0,
#                      "start_time": "2019-11-04T10:50:52+08:00", "name_by_standard_analyzer": "牙齿冷光美白---2", "price": 500,
#                      "name": "牙齿冷光美白---2"},
#                     {"sku_id": 10380, "sku_rank": 0, "end_time": "2029-11-04T10:50:52+08:00", "price_type": 0,
#                      "start_time": "2019-11-04T10:50:52+08:00", "name_by_standard_analyzer": "牙齿冷光美白---3", "price": 500,
#                      "name": "牙齿冷光美白---3"},
#                     {"sku_id": 10381, "sku_rank": 0, "end_time": "2029-11-04T10:50:52+08:00", "price_type": 0,
#                      "start_time": "2019-11-04T10:50:52+08:00", "name_by_standard_analyzer": "牙齿冷光美白---4", "price": 500,
#                      "name": "牙齿冷光美白---4"},
#                     {"sku_id": 10382, "sku_rank": 0, "end_time": "2029-11-04T10:50:52+08:00", "price_type": 0,
#                      "start_time": "2019-11-04T10:50:52+08:00", "name_by_standard_analyzer": "牙齿冷光美白---5", "price": 500,
#                      "name": "牙齿冷光美白---5"},
#                     {"sku_id": 10383, "sku_rank": 0, "end_time": "2029-11-04T10:50:52+08:00", "price_type": 0,
#                      "start_time": "2019-11-04T10:50:52+08:00", "name_by_standard_analyzer": "牙齿冷光美白---6", "price": 500,
#                      "name": "牙齿冷光美白---6"},
#                     {"sku_id": 10384, "sku_rank": 0, "end_time": "2029-11-04T10:50:52+08:00", "price_type": 0,
#                      "start_time": "2019-11-04T10:50:52+08:00", "name_by_standard_analyzer": "牙齿冷光美白---7", "price": 500,
#                      "name": "牙齿冷光美白---7"}], "periodic_price": [
#                     {"price": 500, "start_time": "2000-01-01T00:00:00+08:00", "end_time": "2038-01-18T00:00:00+08:00"},
#                     {"price": 500, "start_time": "2000-01-01T00:00:00+08:00", "end_time": "2038-01-18T00:00:00+08:00"},
#                     {"price": 500, "start_time": "2000-01-01T00:00:00+08:00", "end_time": "2038-01-18T00:00:00+08:00"},
#                     {"price": 500, "start_time": "2000-01-01T00:00:00+08:00", "end_time": "2038-01-18T00:00:00+08:00"},
#                     {"price": 500, "start_time": "2000-01-01T00:00:00+08:00", "end_time": "2038-01-18T00:00:00+08:00"},
#                     {"price": 500, "start_time": "2000-01-01T00:00:00+08:00", "end_time": "2038-01-18T00:00:00+08:00"},
#                     {"price": 500, "start_time": "2000-01-01T00:00:00+08:00", "end_time": "2038-01-18T00:00:00+08:00"},
#                     {"price": 500, "start_time": "2000-01-01T00:00:00+08:00", "end_time": "2019-11-01T00:00:00+08:00"},
#                     {"price": 108, "start_time": "2019-11-01T00:00:00+08:00", "end_time": "2019-12-28T10:50:28+08:00"},
#                     {"price": 500, "start_time": "2019-12-28T10:50:28+08:00", "end_time": "2038-01-18T00:00:00+08:00"},
#                     {"price": 500, "start_time": "2000-01-01T00:00:00+08:00", "end_time": "2019-11-01T00:00:00+08:00"},
#                     {"price": 134, "start_time": "2019-11-01T00:00:00+08:00", "end_time": "2019-12-28T10:50:28+08:00"},
#                     {"price": 500, "start_time": "2019-12-28T10:50:28+08:00", "end_time": "2038-01-18T00:00:00+08:00"},
#                     {"price": 500, "start_time": "2000-01-01T00:00:00+08:00", "end_time": "2019-11-01T00:00:00+08:00"},
#                     {"price": 130, "start_time": "2019-11-01T00:00:00+08:00", "end_time": "2019-12-28T10:50:28+08:00"},
#                     {"price": 500, "start_time": "2019-12-28T10:50:28+08:00", "end_time": "2038-01-18T00:00:00+08:00"},
#                     {"price": 500, "start_time": "2000-01-01T00:00:00+08:00", "end_time": "2019-11-01T00:00:00+08:00"},
#                     {"price": 120, "start_time": "2019-11-01T00:00:00+08:00", "end_time": "2019-12-28T10:50:28+08:00"},
#                     {"price": 500, "start_time": "2019-12-28T10:50:28+08:00", "end_time": "2038-01-18T00:00:00+08:00"},
#                     {"price": 500, "start_time": "2000-01-01T00:00:00+08:00", "end_time": "2019-11-01T00:00:00+08:00"},
#                     {"price": 198, "start_time": "2019-11-01T00:00:00+08:00", "end_time": "2019-12-28T10:50:28+08:00"},
#                     {"price": 500, "start_time": "2019-12-28T10:50:28+08:00", "end_time": "2038-01-18T00:00:00+08:00"},
#                     {"price": 500, "start_time": "2000-01-01T00:00:00+08:00", "end_time": "2019-11-01T00:00:00+08:00"},
#                     {"price": 176, "start_time": "2019-11-01T00:00:00+08:00", "end_time": "2019-12-28T10:50:28+08:00"},
#                     {"price": 500, "start_time": "2019-12-28T10:50:28+08:00", "end_time": "2038-01-18T00:00:00+08:00"},
#                     {"price": 500, "start_time": "2000-01-01T00:00:00+08:00", "end_time": "2019-11-01T00:00:00+08:00"},
#                     {"price": 154, "start_time": "2019-11-01T00:00:00+08:00", "end_time": "2019-12-28T10:50:28+08:00"},
#                     {"price": 500, "start_time": "2019-12-28T10:50:28+08:00", "end_time": "2038-01-18T00:00:00+08:00"}],
#                         "can_sold_time_range": [
#                             {"start_time": "2019-11-04T10:50:52+08:00", "end_time": "2029-11-04T10:50:52+08:00"}],
#                         "case_count": 0,
#                         "nearby_city_tags": [{"name": "合肥", "tag_id": 430}, {"name": "南京", "tag_id": 542},
#                                              {"name": "桂林", "tag_id": 411}, {"name": "南宁", "tag_id": 543},
#                                              {"name": "恩施", "tag_id": 387}, {"name": "鄂州", "tag_id": 388},
#                                              {"name": "黄冈", "tag_id": 447}, {"name": "黄石", "tag_id": 450},
#                                              {"name": "荆门", "tag_id": 473}, {"name": "荆州", "tag_id": 474},
#                                              {"name": "潜江", "tag_id": 567}, {"name": "神农架", "tag_id": 602},
#                                              {"name": "十堰", "tag_id": 608}, {"name": "随州", "tag_id": 621},
#                                              {"name": "天门", "tag_id": 639}, {"name": "襄阳", "tag_id": 676},
#                                              {"name": "咸宁", "tag_id": 680}, {"name": "仙桃", "tag_id": 681},
#                                              {"name": "孝感", "tag_id": 683}, {"name": "宜昌", "tag_id": 711},
#                                              {"name": "岳阳", "tag_id": 724}, {"name": "长沙", "tag_id": 343},
#                                              {"name": "南昌", "tag_id": 538}, {"name": "西安", "tag_id": 675},
#                                              {"name": "六安市", "tag_id": 517}, {"name": "跳跳", "tag_id": 1784},
#                                              {"name": "襄樊", "tag_id": 676}, {"name": "重庆", "tag_id": 359}],
#                         "is_fenqi": False, "id": 5740426, "special": [], "ordered_user_ids": [], "pv": 0,
#                         "smart_rank2": 0, "detail_description": "", "doctor": {"name": "武汉大学同仁医院", "title": "0",
#                                                                                "hospital": {
#                                                                                    "city_province_country_tag_id": 259,
#                                                                                    "area_count": 0,
#                                                                                    "officer_name": "武汉大学同仁医院",
#                                                                                    "city_province_name_by_standard_analyzer": "湖北",
#                                                                                    "is_high_quality": False,
#                                                                                    "city_province_name": "湖北",
#                                                                                    "city_province_tag_id": 275,
#                                                                                    "city_name": "武汉", "id": "whtr",
#                                                                                    "name": "武汉大学同仁医院", "chain_count": 0,
#                                                                                    "city_name_by_standard_analyzer": "武汉",
#                                                                                    "hospital_type2": "0",
#                                                                                    "city_tag_id": 662,
#                                                                                    "officer_name_by_standard_analyzer": "武汉大学同仁医院",
#                                                                                    "name_by_standard_analyzer": "武汉大学同仁医院",
#                                                                                    "hospital_type": "0",
#                                                                                    "city_count": 0},
#                                                                                "famous_doctor": False,
#                                                                                "name_by_standard_analyzer": "武汉大学同仁医院",
#                                                                                "id": "WHDXTRYY"}, "ordering": 10000,
#                         "is_can_be_sold": False, "new_sku_special": [
#                     {"item_id": 17802, "position": 0, "sku_id": 10384, "has_pos": False, "id": 1056}], "tip": "",
#                         "seckill_time": [], "advertise_info": [], "location": {"lat": 30.54573, "lon": 114.30866},
#                         "closure_tags_by_standard_analyzer": ["手术二级", "口唇圈", "口腔齿科", "手术", "牙齿冷光美白", "牙齿美容", "美容嫩肤圈",
#                                                               "牙齿口腔", "牙科", "公立医院", "武汉"], "short_description": "牙齿冷光 ",
#                         "lowest_price": [{"price": 500, "start_time": "2000-01-01T00:00:00+08:00",
#                                           "end_time": "2019-11-01T00:00:00+08:00", "start_time_long": 946656000,
#                                           "end_time_long": 1572537600},
#                                          {"price": 108, "start_time": "2019-11-01T00:00:00+08:00",
#                                           "end_time": "2019-12-28T10:50:28+08:00", "start_time_long": 1572537600,
#                                           "end_time_long": 1577501428},
#                                          {"price": 500, "start_time": "2019-12-28T10:50:28+08:00",
#                                           "end_time": "2038-01-18T00:00:00+08:00", "start_time_long": 1577501428,
#                                           "end_time_long": 2147356800}], "special_rank": [], "channel": "1",
#                         "recommend_rank": {"is_recommend": False, "rank": 999999}, "short_description_pre": "牙齿冷光美白",
#                         "service_type": 0, "start_time": "2019-11-04T10:50:52+08:00", "advertise_position": [],
#                         "is_insurance": False, "gift_rank": 1, "is_promote": False, "max_query_pv": [],
#                         "is_stage": False, "merchant_doctor_id": "WHDXTRYY", "is_floor_price": False, "smart_rank": 0,
#                         "name": "【武汉@武汉大学同仁医院】牙齿冷光美白", "discount": 0.5, "doctor_customize_sort": 9223372036854776000,
#                         "hospital_customize_sort": 9223372036854776000, "end_time_long": 1888455052,
#                         "closure_tags": ["手术二级", "口唇圈", "口腔齿科", "手术", "牙齿冷光美白", "牙齿美容", "美容嫩肤圈", "牙齿口腔", "牙科", "公立医院",
#                                          "武汉"], "advertise_searchwords": [], "end_time": "2029-11-04T10:50:52+08:00",
#                         "sales_count": 0, "fresh_closure_tags": ["嫩肤", "口腔", "美白", "牙齿", "冷光美白"],
#                         "share_get_cashback": False, "new_sku_list": [
#                     {"sku_id": 10378, "name": "牙齿冷光美白---1", "price_type": 0, "price": 500, "sku_rank": 0,
#                      "end_time": "2029-11-04T10:50:52+08:00", "start_time": "2019-11-04T10:50:52+08:00"},
#                     {"sku_id": 10379, "name": "牙齿冷光美白---2", "price_type": 0, "price": 500, "sku_rank": 0,
#                      "end_time": "2029-11-04T10:50:52+08:00", "start_time": "2019-11-04T10:50:52+08:00"},
#                     {"sku_id": 10380, "name": "牙齿冷光美白---3", "price_type": 0, "price": 500, "sku_rank": 0,
#                      "end_time": "2029-11-04T10:50:52+08:00", "start_time": "2019-11-04T10:50:52+08:00"},
#                     {"sku_id": 10381, "name": "牙齿冷光美白---4", "price_type": 0, "price": 500, "sku_rank": 0,
#                      "end_time": "2029-11-04T10:50:52+08:00", "start_time": "2019-11-04T10:50:52+08:00"},
#                     {"sku_id": 10382, "name": "牙齿冷光美白---5", "price_type": 0, "price": 500, "sku_rank": 0,
#                      "end_time": "2029-11-04T10:50:52+08:00", "start_time": "2019-11-04T10:50:52+08:00"},
#                     {"sku_id": 10383, "name": "牙齿冷光美白---6", "price_type": 0, "price": 500, "sku_rank": 0,
#                      "end_time": "2029-11-04T10:50:52+08:00", "start_time": "2019-11-04T10:50:52+08:00"},
#                     {"sku_id": 10384, "name": "牙齿冷光美白---7", "price_type": 0, "price": 500, "sku_rank": 0,
#                      "end_time": "2029-11-04T10:50:52+08:00", "start_time": "2019-11-04T10:50:52+08:00"},
#                     {"sku_id": 10393, "name": "", "price_type": 4, "price": 108, "parent_id": 10384, "sku_rank": 0,
#                      "end_time": "2019-12-28T10:50:28+08:00", "start_time": "2019-11-01T00:00:00+08:00"},
#                     {"sku_id": 10393, "name": "", "price_type": 0, "price": 500, "parent_id": 10384, "sku_rank": 0,
#                      "end_time": "2029-11-04T10:50:52+08:00", "start_time": "2019-12-28T10:50:28+08:00"},
#                     {"sku_id": 10394, "name": "", "price_type": 4, "price": 134, "parent_id": 10383, "sku_rank": 0,
#                      "end_time": "2019-12-28T10:50:28+08:00", "start_time": "2019-11-01T00:00:00+08:00"},
#                     {"sku_id": 10394, "name": "", "price_type": 0, "price": 500, "parent_id": 10383, "sku_rank": 0,
#                      "end_time": "2029-11-04T10:50:52+08:00", "start_time": "2019-12-28T10:50:28+08:00"},
#                     {"sku_id": 10395, "name": "", "price_type": 4, "price": 130, "parent_id": 10382, "sku_rank": 0,
#                      "end_time": "2019-12-28T10:50:28+08:00", "start_time": "2019-11-01T00:00:00+08:00"},
#                     {"sku_id": 10395, "name": "", "price_type": 0, "price": 500, "parent_id": 10382, "sku_rank": 0,
#                      "end_time": "2029-11-04T10:50:52+08:00", "start_time": "2019-12-28T10:50:28+08:00"},
#                     {"sku_id": 10396, "name": "", "price_type": 4, "price": 120, "parent_id": 10381, "sku_rank": 0,
#                      "end_time": "2019-12-28T10:50:28+08:00", "start_time": "2019-11-01T00:00:00+08:00"},
#                     {"sku_id": 10396, "name": "", "price_type": 0, "price": 500, "parent_id": 10381, "sku_rank": 0,
#                      "end_time": "2029-11-04T10:50:52+08:00", "start_time": "2019-12-28T10:50:28+08:00"},
#                     {"sku_id": 10397, "name": "", "price_type": 4, "price": 198, "parent_id": 10380, "sku_rank": 0,
#                      "end_time": "2019-12-28T10:50:28+08:00", "start_time": "2019-11-01T00:00:00+08:00"},
#                     {"sku_id": 10397, "name": "", "price_type": 0, "price": 500, "parent_id": 10380, "sku_rank": 0,
#                      "end_time": "2029-11-04T10:50:52+08:00", "start_time": "2019-12-28T10:50:28+08:00"},
#                     {"sku_id": 10398, "name": "", "price_type": 4, "price": 176, "parent_id": 10379, "sku_rank": 0,
#                      "end_time": "2019-12-28T10:50:28+08:00", "start_time": "2019-11-01T00:00:00+08:00"},
#                     {"sku_id": 10398, "name": "", "price_type": 0, "price": 500, "parent_id": 10379, "sku_rank": 0,
#                      "end_time": "2029-11-04T10:50:52+08:00", "start_time": "2019-12-28T10:50:28+08:00"},
#                     {"sku_id": 10399, "name": "", "price_type": 4, "price": 154, "parent_id": 10378, "sku_rank": 0,
#                      "end_time": "2019-12-28T10:50:28+08:00", "start_time": "2019-11-01T00:00:00+08:00"},
#                     {"sku_id": 10399, "name": "", "price_type": 0, "price": 500, "parent_id": 10378, "sku_rank": 0,
#                      "end_time": "2029-11-04T10:50:52+08:00", "start_time": "2019-12-28T10:50:28+08:00"}],
#                         "floor_id": []}, "inner_hits": {"sku_list": {"hits": {"total": 7, "max_score": False, "hits": [
#                {"_index": "gm_test-service", "_type": "service", "_id": "5740426",
#                 "_nested": {"field": "sku_list", "offset": 6}, "_score": False,
#                 "_source": {"sku_id": 10384, "sku_rank": 0, "end_time": "2029-11-04T10:50:52+08:00", "price_type": 0,
#                             "start_time": "2019-11-04T10:50:52+08:00", "name_by_standard_analyzer": "牙齿冷光美白---7",
#                             "price": 500, "name": "牙齿冷光美白---7"}, "sort": [1.4142135, 500]}]}}}}]}}
#
# print(type(res))
# print(type(res['hits']['total']))
# if "value" in res['hits']['total']:
#     print(res['hits']['total']['value'])
# query = '绿植'
#
# query_ret_list = [
#     {'results_num': 87, 'ori_name': '绿植', 'id': None, 'is_online': True, 'offline_score': 0, 'type_flag': 'unknown',
#      'highlight_name': '<ems>绿植</ems>', 'describe': '约87个结果'},
#     {'results_num': 0, 'ori_name': '发财树', 'id': None, 'is_online': True, 'offline_score': 0, 'type_flag': 'unknown',
#      'highlight_name': '发财树', 'describe': ''},
#     {'results_num': 0, 'ori_name': '绿萝', 'id': None, 'is_online': True, 'offline_score': 0, 'type_flag': 'unknown',
#      'highlight_name': '绿萝', 'describe': ''},
#     {'results_num': 0, 'ori_name': '虎皮兰', 'id': None, 'is_online': True, 'offline_score': 0, 'type_flag': 'unknown',
#      'highlight_name': '虎皮兰', 'describe': ''},
#     {'results_num': 0, 'ori_name': '吊篮', 'id': None, 'is_online': True, 'offline_score': 0, 'type_flag': 'unknown',
#      'highlight_name': '吊篮', 'describe': ''},
#     {'results_num': 0, 'ori_name': '富贵树', 'id': None, 'is_online': True, 'offline_score': 0, 'type_flag': 'unknown',
#      'highlight_name': '富贵树', 'describe': ''}]
#
# print("----------------------")
#
# for ret in query_ret_list:
#     query2 = ret["ori_name"]
#
#     for item in range(0, len(query)):
#
#         ss = query2.find(query[item])
#         high_query = None
#         if ss >= 0:
#             highlight_marks = u'<ems>%s</ems>' % query[item]
#             high_query = query2.replace(query[item], highlight_marks)
#             query2 = high_query
#             print(query2)
#
#         if high_query == None:
#             ret["highlight_name"] = query2
#
#         else:
#             ret["highlight_name"] = high_query
# print(query_ret_list)

# fanti_query = [{"痩脸针": "瘦脸针"}, {"瘦腿针": "瘦腿针"}, {"痩脸针": "瘦脸针"}]
#
# ret_list = [{"results_num": 100, "ori_name": "瘦脸"}, {"results_num": 23, "ori_name": "痩脸针"}]
#
# for item in ret_list:
#     result_num = [[item['results_num'], list(ret.values())[0], list(ret.keys())[0]] for ret in fanti_query if
#                   list(ret.keys())[0] == item['ori_name']]
#
#     print(result_num)
#     if len(result_num) > 0:
#         ret_list.remove(item)
#         print(ret_list)
#         for item in ret_list:
#             if item['ori_name'] == result_num[0][1]:
#                 item['results_num'] += result_num[0][0]
#
# print(ret_list)
# second_demands_set = ['线条流畅', '拔牙', '耳部手术']
# first_demands_set = ['线条']
#
# REDIS_URL = "redis://redis.paas-test.env:6379/0"
# redis_client = redis.StrictRedis.from_url(REDIS_URL)
# operator_category = "doris:save_second_solutions_isoperator_to_redis"
# all_data = redis_client.get(operator_category)
# all_operator_list = []
# if all_data:
#     all_operator_list = json.loads(all_data)
#
# if len([True for item in list(second_demands_set) if item in all_operator_list]) > 0:
#     is_operative_class = True
# else:
#     lens = len([True for item in list(first_demands_set) if item in ['手术']])
#     if lens:
#         is_operative_class = True
#     else:
#         is_operative_class = False
#
# print(is_operative_class)


# user_portrait_redis = {b'837': b'0.5', b'7117': b'9.0', b'1055': b'39.13173061151046', b'15': b'2.8720157488723124',
#                        b'203': b'3.0', b'18': b'1.7645546090204478', b'6231': b'0.5', b'909': b'0.5',
#                        b'2417': b'19.678239462296006', b'982': b'0.5', b'28': b'27.19621187724544',
#                        b'38': b'76.64195407198201', b'933': b'12.06432062790152', b'821': b'1.8420727202483786',
#                        b'201': b'3.0', b'1233': b'83.35422658868859', b'69': b'1.5', b'229': b'0.5', b'840': b'0.5',
#                        b'6148': b'3.0', b'812': b'0.5', b'775': b'1.9322703059979607', b'842': b'0.5', b'204': b'3.0',
#                        b'102': b'3.0', b'900': b'1.0', b'898': b'0.5', b'235': b'1.0', b'1136': b'0.5',
#                        b'30': b'13.789166500707456', b'6144': b'1.0', b'81': b'2.5', b'21': b'40.537176443409535',
#                        b'221': b'77.19763262068057', b'911': b'0.5', b'5060': b'1.0', b'66': b'13.919982720355883',
#                        b'117': b'133.7906265423949', b'766': b'0.5', b'237': b'0.5', b'836': b'0.5', b'187': b'0.5',
#                        b'841': b'0.5', b'906': b'0.5', b'225': b'3.0', b'37': b'13.83641146901177', b'29': b'8.0',
#                        b'253': b'1.875721119690349', b'213': b'0.5', b'1370': b'5.521132259288034',
#                        b'955': b'3.7723404302232657', b'200': b'3.0', b'70': b'2.0', b'5724': b'0.5',
#                        b'45': b'67.82998142430212', b'17': b'249.98324279903085', b'926': b'1.8870793413614013',
#                        b'46': b'12.764554609020447', b'3285': b'12.87393416079308', b'1032': b'27.184950331476777',
#                        b'230': b'0.5', b'2938': b'7.368290880993515', b'2112': b'15.5', b'2935': b'1.8369458721073477'}
#
# user_portrait = [{"tag_score": float(score), "tag_id": int(tag)} for tag, score in
#                  user_portrait_redis.items()]
#
# user_portrait_desc = sorted(user_portrait, key=lambda k: (k.get('tag_score', 0)), reverse=True)[:10]
#
# all_ids = []
# for item in user_portrait_desc:
#     all_ids.append(item.get("tag_id"))
#
# print(all_ids)
# [{'tag_score': 301.4003382097078, 'tag_id': 21}, {'tag_score': 208.39497243446613, 'tag_id': 3285},
#  {'tag_score': 172.1704175641858, 'tag_id': 79}, {'tag_score': 133.7682856812993, 'tag_id': 26},
#  {'tag_score': 94.0, 'tag_id': 896}, {'tag_score': 76.63531068064837, 'tag_id': 65},
#  {'tag_score': 70.97192726896661, 'tag_id': 1233}, {'tag_score': 62.08568700606704, 'tag_id': 15},
#  {'tag_score': 59.7040739678682, 'tag_id': 1055}, {'tag_score': 56.5, 'tag_id': 19}]
# [21, 3285, 79, 26, 896, 65, 1233, 15, 1055, 19]
# [21, 3285, 15, 61, 26, 28, 18, 19, 3459, 64]
# [17, 117, 1233, 221, 38, 45, 21, 1055, 28, 1032]
# #
# ss = [{"follow_time": -1}, {"follow_time": 10}, {"follow_time": 3}, {"follow_time": 2}]
# ss.sort(key=lambda x: x['follow_time'], reverse=True)
# print(ss[:2])
import hashlib, traceback, logging

REDIS_URL = "redis://redis.paas-test.env:6379/0"
redis_client = redis.StrictRedis.from_url(REDIS_URL)


def recommed_service_category_device_id_by_tail(device_id, tail_list=[], real_cary=False, only_use_device_id=False):
    try:
        '''
        设备品类显示, 是否命中灰度
        '''
        if tail_list:
            categroy_select_cary = tail_list
        else:
            categroy_select_cary = ["0", "1", "2", "3", "4", "a", "b", "c", "e"]
        if real_cary:
            categroy_select_cary_v2 = ["0", "1", "2", "3", "4", "a", "b", "c"]

        if not device_id:
            return False

        hd_id = hashlib.md5(str(device_id).encode()).hexdigest()
        is_gray = hd_id[-1] in categroy_select_cary
        print(is_gray)
        if not is_gray or only_use_device_id:
            print("---")
            # gray_devices_key = "gm:gray:devices:key"
            gray_devices_key = "doris:feed:tag3:gray"
            return redis_client.sismember(gray_devices_key, device_id)
        return is_gray
    except:
        logging.error("catch exception,err_msg:%s" % traceback.format_exc())
        return False


# ss = recommed_service_category_device_id_by_tail(device_id="1BA2464E-8D6A-480D-9292-6CB98E44AB31",
#                                                  only_use_device_id=True)
# print(ss)


