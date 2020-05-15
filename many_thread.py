#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
import time
import threading
from kafka import KafkaProducer
from traitlets import log
import json


# def on_send_success(record_metadata):
#     print(record_metadata.topic)
#     print(record_metadata.partition)
#     print(record_metadata.offset)

#
# def on_send_error(excp):
#     log.error('I am an errback', exc_info=excp)
#     # handle exception


def send_messag(topic, id, interval_time):
    print("-------------")
    producer = KafkaProducer(bootstrap_servers=['kafka-service-0.kafka-service-headless.test:9092'])
    while True:
        msg_dic = {
            "card_id": i,
            "card_user_id": 23243,
            "card_type": "auto_vest12",
            "create_time": "2019-12-30 09:55:43",
            "content_level": 6,
            "tag_names": ["瘦脸针kyc", "鼻综合kyc"],
            "type": "get_write_answer_userinfo",
            "current_push_time": "2019-12-30 09:55:43",
            'action_type': 'follow'
        }
        producer.send(topic, json.dumps(msg_dic).encode())
        # 间隔多长时间生产一条消息
        # time.sleep(interval_time)
    producer.close()


interval_times = [60, 300, 600, 1200, 1800, 3600]

# 开启50个线程
# for i in range(0, 50):
#     deviceId = "%06d" % random.randint(0, 999999)
#     print(deviceId)
#     interval_time = [random.randint(0, len(interval_times) - 1)]
#
#     recv_thread = threading.Thread(target=send_messag, args=("my-topic", id, interval_time))
#
#     # 守护主线程，主线程退出后子线程直接销毁
#     recv_thread.setDaemon(True)
#     recv_thread.start()

# while True:
#     # 主线程一直运行
#     time.sleep(5000)
# _____________________________#!

# !/usr/bin/python3

import _thread
import time


# 为线程定义一个函数
def print_time(threadName, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print("%s: %s" % (threadName, time.ctime(time.time())))


# 创建两个线程
try:
    _thread.start_new_thread(target=print_time, args=("Thread-1", 2))
    _thread.start_new_thread(target=print_time, args=("Thread-2", 4))
except:
    print("Error: 无法启动线程")

while 1:
    pass
