# # -*- coding: UTF-8 -*-
# import datetime
# import logging
# # from libs.error import logging_exception
# import traceback
# import random
# import time
#
# logger = logging.getLogger(__name__)
#
#
# def get_create_time_now_short_days(create_time):
#     try:
#         now = datetime.datetime.now()
#         # strtime = now.strftime("%Y-%m-%d %H:%M:%S")
#         strtime = datetime.datetime.strptime(now[0:10], "%Y-%m-%d")
#         createt = datetime.datetime.strptime(create_time[0:10], "%Y-%m-%d")
#         num = (strtime - createt).days
#         return num
#     except:
#         logger.error("catch exception,err_log:%s" % traceback.format_exc())
#         return False
#
#
# def strTimeProp(start, end, prop, frmt):
#     stime = time.mktime(time.strptime(start, frmt))
#     etime = time.mktime(time.strptime(end, frmt))
#     ptime = stime + prop * (etime - stime)
#     return int(ptime)
#
#
# def get_two_four_random_time(create_time, nowt, frmt='%Y-%m-%d %H:%M:%S'):
#     try:
#         start = str(create_time + datetime.timedelta(hours=2))
#         end = str(create_time + datetime.timedelta(hours=4))
#         return time.strftime(frmt, time.localtime(strTimeProp(start, end, random.random(), frmt)))
#
#     except:
#         logger.error("catch exception,err_log:%s" % traceback.format_exc())
#         return None
#
#
# def get_two_hours_time(create_time):
#     try:
#         yes_time = create_time + datetime.timedelta(hours=2)
#         return yes_time
#     except:
#         logger.error("catch exception,err_log:%s" % traceback.format_exc())
#         return None
#
#
# def get_one_six_days_random_time(create_time, day_num):
#     try:
#         yes_time = create_time + datetime.timedelta(days=day_num)
#
#         return yes_time
#     except:
#         logger.error("catch exception,err_log:%s" % traceback.format_exc())
#         return None
#
#
# def get_create_time_now_short_days(create_time):
#     try:
#         now = datetime.datetime.now()
#         # strtime = now.strftime("%Y-%m-%d %H:%M:%S")
#         strtime = datetime.datetime.strptime(now[0:10], "%Y-%m-%d")
#         createt = datetime.datetime.strptime(create_time[0:10], "%Y-%m-%d")
#         num = (strtime - createt).days
#         return num
#     except:
#         logger.error("catch exception,err_log:%s" % traceback.format_exc())
#         return False
#
#
# def get_two_hours_time(create_time):
#     try:
#         yes_time = create_time + datetime.timedelta(hours=2)
#         return yes_time
#     except:
#         logger.error("catch exception,err_log:%s" % traceback.format_exc())
#         return False
#
#
# def get_two_four_random_time(create_time):
#     try:
#         pass
#         # print("------")
#         # two_hours = (create_time + datetime.timedelta(hours=2)).strftime("%Y-%m-%d")
#         # four_hours = (create_time + datetime.timedelta(hours=4)).strftime("%Y-%m-%d")
#         # print(two_hours)
#         # print(four_hours)
#         # stime = datetime.datetime.strptime(two_hours, four_hours)
#         # etime = datetime.datetime.strptime(four_hours, two_hours)
#         # return [random.random() * (etime - stime) + stime for _ in range(1)]
#     except:
#         logger.error("catch exception,err_log:%s" % traceback.format_exc())
#         return False
#
#
# def get_time_by_create_time(create_time):
#     try:
#         ##先获取当天的下发时间：
#         now = datetime.datetime.now()
#
#     except:
#         logger.error("catch exception,err_log:%s" % traceback.format_exc())
#         return False
#
#
# def strTimeProp(start, end, prop, frmt):
#     stime = time.mktime(time.strptime(start, frmt))
#     etime = time.mktime(time.strptime(end, frmt))
#     ptime = stime + prop * (etime - stime)
#     return int(ptime)
#
#
# def randomDate(create_time, frmt='%Y-%m-%d %H:%M:%S'):
#     start = str(create_time + datetime.timedelta(hours=2))
#     end = str(create_time + datetime.timedelta(hours=4))
#     return time.strftime(frmt, time.localtime(strTimeProp(start, end, random.random(), frmt)))
#
#
# def randomDate_six_one(start, end, frmt='%Y-%m-%d %H:%M:%S'):
#     return time.strftime(frmt, time.localtime(strTimeProp(start, end, random.random(), frmt)))
#
#
# def get_list(date):
#     return datetime.datetime.strptime(date, "%Y-%m-%d %H:%M:%S").timestamp()
#
#
# def get_one_six_days_random_time(frmt='%Y-%m-%d %H:%M:%S', comment_num=3):
#     try:
#         now = datetime.datetime.now()
#         zeroday = str(datetime.datetime(now.year, now.month, now.day, 0, 0, 0))
#         lastday = str(datetime.datetime(now.year, now.month, now.day + 1, 0, 0, 0))
#         random_times = [randomDate_six_one(zeroday, lastday, frmt) for _ in range(comment_num)]
#         have_sort_times = sorted(random_times, key=lambda date: get_list(date))
#         return have_sort_times
#     except:
#         logger.error("catch exception,err_log:%s" % traceback.format_exc())
#         return False
#
#
# def get_ten_last_days_random_time(push_time=None, frmt='%Y-%m-%d %H:%M:%S', comment_num=3):
#     try:
#         ##比较当前时间和最后一次创建时间的差
#         now = datetime.datetime.now()
#         zeroday = str(datetime.datetime(now.year, now.month, now.day + 10, 0, 0, 0))
#         lastday = str(datetime.datetime(now.year, now.month, now.day + 11, 0, 0, 0))
#         random_times = [randomDate_six_one(zeroday, lastday, frmt) for _ in range(comment_num)]
#         have_sort_times = sorted(random_times, key=lambda date: get_list(date))
#         return have_sort_times
#     except:
#         logger.error("catch exception,err_log:%s" % traceback.format_exc())
#         return False
#
#
# create_time = "2019-12-16 23:29:02"
# now = datetime.datetime.now()
# createt = datetime.datetime.strptime(create_time, '%Y-%m-%d %H:%M:%S')
# print("--------------")
# print(createt.hour)
# nowt = now.strftime('%Y-%m-%d %H:%M:%S')
#
# ##相差秒数
# num = (now - createt).total_seconds()
# min = 60
# mins = divmod(num, min)[0]
# print(mins)
#
# # createt_day = datetime.datetime.strptime(create_time, '%Y-%m-%d')
# # print(createt_day)
#
# if now > createt:
#     print('======')
# num_days = now.day - createt.day
# print(num_days)
#
# ##转化成分数后进行一层一层的比较
#
# if mins < 120 and num_days == 0:
#     print("时候未到")
#
# ##进入当天的下发时间
# elif mins >= 120 and mins <= 4 * 60 and num_days == 0:
#     print("当天")
#     get_time = randomDate(createt)
#     print(get_time)
#
#
# elif mins > 4 * 60 and mins <= 24 * 60 * 6:
#
#     print("1-6天的")
#     get_time = get_one_six_days_random_time(comment_num=3)
#     print(get_time)
#
# elif mins > 24 * 60 * 6 and mins <= 24 * 60 * 365:
#     print("6天后的")
#     push_time = '2019-12-16 16:23:20'
#     get_time = get_ten_last_days_random_time(push_time=push_time, comment_num=3)
#     print(get_time)
#
# else:
#     ##需要删掉kafka的数据不再进行下发
#     print("所有下发结束")
#
#
# def randomDate(create_time, frmt='%Y-%m-%d %H:%M:%S', action_type=None):
#     if action_type == "follow":
#         action_num = random.randint(1, 3)
#
#     start = str(create_time + datetime.timedelta(hours=2))
#     end = str(create_time + datetime.timedelta(hours=4))
#
#     random_times = [randomDate_six_one(start, end, frmt) for _ in range(action_num)]
#     have_sort_times = sorted(random_times, key=lambda date: get_list(date))
#
#     return have_sort_times
#
#
# sss = randomDate(create_time=createt, action_type="follow")
# print(sss)
#
# ss = [1, 2, 3]
#
# ss.remove(11)
# print(ss)
#
# print(ss.pop())
#
# create_time = "2019-12-16 23:29:02"
# now = datetime.datetime.now()
# createt = datetime.datetime.strptime(create_time, '%Y-%m-%d %H:%M:%S')

import jieba
import pymysql
from bs4 import BeautifulSoup
import jieba.analyse

class GetContentKeyWords(object):
    def __init__(self):
        self.jeiba = jieba
        self.tag_list = ["瘦脸针kyc", "双眼皮kyc", "水光针kyc", "玻尿酸kyc", "吸脂kyc", "埋线提升kyc", "鼻综合kyc", "光子嫩肤kyc", "没有想法kyc",
                         "牙齿kyc", "抗衰紧致kyc", "胸部kyc"]
        self.star_list = []
        self.synonym_tag_list = []
        self.tags = ""
        self.stars = ""
        self.synonym_tags = ""

    def add_tag_word(self):
        jieba = self.jeiba

        if self.tag_list:
            for word in self.tag_list:
                jieba.add_word(word)

        if self.star_list:
            for word in self.star_list:
                jieba.add_word(word)

        if self.synonym_tag_list:
            for word in self.synonym_tag_list:
                jieba.add_word(word)

    def get(self, content):
        self.add_tag_word()
        return self.jeiba.cut(content)

    def get_keywords(self, content, k=None):
        self.add_tag_word()
        jieba = self.jeiba
        keywords = jieba.analyse.extract_tags(content, topK=9999, withWeight=True, allowPOS=())

        tags = []
        stars = []
        synonym_tags = []

        for item in keywords:
            if item[0] in self.tag_list:
                tags.append(str(item[0]))

            if item[0] in self.star_list:
                stars.append(str(item[0]))

            if item[0] in self.synonym_tag_list:
                synonym_tags.append(str(item[0]))

        self.tags = ",".join(tags[:k])
        self.stars = ",".join(stars[:k])
        self.synonym_tags = ",".join(synonym_tags[:k])



NAME = 'mimas_test'
USER = 'work'
PAASWORD = 'Gengmei1'
HOST = 'bj-cdb-6slgqwlc.sql.tencentcdb.com'
PORT = 62120

db_zhengxing_eagle = pymysql.connect(host=HOST, user=USER, password=PAASWORD, db=NAME, port=PORT)

print(db_zhengxing_eagle)
zhengxing_cursor = db_zhengxing_eagle.cursor()
sql = 'select content from api_answer where id = %s ' % (529413)
zhengxing_cursor.execute(sql)
data = list(zhengxing_cursor.fetchall())

if len(data) > 0:
    content = data[0][0]

html = """
<html>
<head><title>story12345</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><span>westos</span><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister1" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""
soup = BeautifulSoup(data[0][0], 'html.parser')
print(soup.text)

ck = GetContentKeyWords()
keywords = ck.get_keywords(soup.text, len(ck.tag_list))

print(keywords)
