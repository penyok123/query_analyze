# coding=utf-8
import os
import json
import datetime
import traceback
import logging
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr


import json
import redis

my_sender = 'lixiaofang@igengmei.com'
my_pass = 'xSBzZCmxFBgJs3k3'
my_user6 = "lixiaofang@igengmei.com"
key = "auto_vest_one_user_action:" + str(345)

data = open("data.txt", "r", encoding="utf-8")
query_num = dict()
for item in data.readlines():
    log = item.strip()
    dict_log = eval(log)
    message = dict_log.get("message", None)
    get_info = message.split("user_search_query")[1].split("get_sug_num")

    query = get_info[0][1:-1]
    num = get_info[1][1:]
    query_num[query] = num

# print(query_num)
sort_by_num = sorted(query_num.items(), key=lambda x: x[1], reverse=True)


# print(sort_by_num)
# file = open("query_num.txt", "w", encoding="utf-8")
# with open("query_num.txt", "w", encoding='utf8') as f:
#     for item in sort_by_num:
#         f.write(str(item[0]))
#         f.write("\t")
#         f.write(str(item[1]))
#         f.write("\n")

def send_email_tome(stat_data):
    try:
        msg = MIMEText(str(stat_data), 'plain', 'utf-8')
        msg['From'] = formataddr(["李小芳", my_sender])
        msg["To"] = formataddr(["李小芳", my_user6])
        msg['Subject'] = str(datetime.date.today()) + "马甲超过次数啦，赶紧看一下"
        server = smtplib.SMTP_SSL("smtp.exmail.qq.com", 465)
        server.login(my_sender, my_pass)
        server.sendmail(my_sender, [my_user6], msg.as_string())
        server.quit()
    except Exception:
        logging.error("catch exception,main:%s" % traceback.format_exc())


send_email_tome(sort_by_num)
