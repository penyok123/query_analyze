# -*- coding: utf-8 -*-
import datetime
import traceback
import logging
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
from django.conf import settings

import json
import redis

my_sender = 'lixiaofang@igengmei.com'
my_pass = 'Wd3W9j5XDbcKQHiz'
my_user6 = "lixiaofang@igengmei.com"
key = "auto_vest_one_user_action:" + str(345)

REDIS_URL = "redis://redis.paas-test.env:6379/0"
redis_client = redis.StrictRedis.from_url(REDIS_URL)
# print(datetime.datetime.now())

ss = {"click": 0, "follow": 0, "comment": 100}
redis_client.set(key, json.dumps(ss))

sss = redis_client.ttl(key)
print(sss)


def send_email_tome(stat_data):
    try:
        msg = MIMEText(stat_data, 'plain', 'utf-8')
        msg['From'] = formataddr(["李小芳", my_sender])
        msg["To"] = formataddr(["李小芳", my_user6])
        msg['Subject'] = str(datetime.date.today()) + "马甲超过次数啦，赶紧看一下"
        server = smtplib.SMTP_SSL("smtp.exmail.qq.com", 465)
        server.login(my_sender, my_pass)
        server.sendmail(my_sender, [my_user6], msg.as_string())
        server.quit()
    except Exception:
        logging.error("catch exception,main:%s" % traceback.format_exc())


# key = "auto_vest_one_user_action:" + str(345)
# redis_data = redis_client.get(key)

redis_data = redis_client.get(key)
print(redis_data)
if redis_data:
    redis_data = json.loads(redis_data)
    click_num = int(redis_data.get("comment")) + 1
    redis_data['comment'] = click_num
    redis_client.set(key, json.dumps(redis_data))
else:
    redis_data = {"click": 0, "follow": 0, "comment": 1}
    redis_client.set(key, json.dumps(redis_data))
redis_client.expire(key, time=24 * 60 * 60)
comment_num = redis_data["comment"]
####在这里做判断 一天不能超过20个 如果超过二十个不下发  不超过二十个下发对应的灌水功能
if comment_num > 20:
    print("-----send")
else:
    print("3343423235523")

ddd = [32269952, 32269956, 32269962, 32269966, 32269973, 32269978, 32269980, 32269982, 32269987, 32269989, 32270003,
       32270004, 32270007, 32270012, 32270015, 32270017, 32270020, 32270024, 32270027, 32270031, 32270041, 32270044,
       32270047, 32270050, 32270054, 32270055, 32270057, 32270059, 32270063, 32270066, 32269913, 32269918, 32269920,
       32269927, 32269933, 32269939, 32269943, 32269948, 32269957, 32269965, 32269972, 32269979, 32269983, 32269988,
       32269995, 32270002, 32270005, 32270011, 32270016, 32270022, 32270029, 32270036, 32270040, 32270051, 32270061,
       32270065, 32270071, 32270075, 32270081, 32270085, 32270094, 32270096, 32270110, 32270116, 32270121, 32270141,
       32270147, 32270152, 32270156, 32270161, 32270114, 32270119, 32270122, 32270125, 32270129, 32270131, 32270133,
       32270134, 32270137, 32270167, 32270068, 32270070, 32270076, 32270078, 32270083, 32270087, 32270093, 32270095,
       32270099, 32270105, 32269992, 32270018, 32270023, 32270030, 32270034, 32270043, 32270048, 32270052, 32270056,
       32270060]

# b = [32270075, 32270029, 32270036, 32270040, 32270051, 32270061, 32270065, 32270071, 32270081, 32270085, 32269972,
#      32269979, 32269983, 32269988, 32269995, 32270002, 32270005, 32270011, 32270016, 32270022, 32269913, 32269918,
#      32269920, 32269927, 32269933, 32269939, 32269943, 32269948, 32269957, 32269965, 32270003, 32270004, 32270007,
#      32270012, 32270015, 32270017, 32270020, 32270024, 32270027, 32270031, 32269952, 32269956, 32269962, 32269966,
#      32269973, 32269978, 32269980, 32269982, 32269987, 32269989]
