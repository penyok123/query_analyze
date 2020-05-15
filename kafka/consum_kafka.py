# #!/usr/bin/env python
# # -*- coding: utf-8 -*-
# from kafka import KafkaConsumer
# from django.conf import settings
# import json
# from kafka import KafkaProducer
import datetime
from kafka import KafkaProducer
from kafka import KafkaConsumer, TopicPartition
import time
import json

# ###链接kafka获取数据
# # @classmethod
# # def get_kafka_consumer_ins(consumser_obj, topic_name=None):
# #     if not consumser_obj:
# #         topic_name = settings.KAFKA_TOPIC_NAME if not topic_name else topic_name
# #         gm_logging_name = settings.KAFKA_GM_LOGGING_TOPIC_NAME
# #         consumser_obj = KafkaConsumer(bootstrap_servers=settings.KAFKA_BROKER_LIST)
# #         consumser_obj.subscribe([topic_name, gm_logging_name])
# #
# #     return consumser_obj
#
#
# producer = KafkaProducer(bootstrap_servers='kafka-service-0.kafka-service-headless.test:9092')
#
# print(producer)
# msg_dict = {
#     "sleep_time": 10,
#     "db_config": {
#         "database": "gm-logging-paas",
#         "host": "kafka-service-0.kafka-service-headless.test",
#         "user": "root",
#         "password": "root"
#     },
#     "table": "msg",
#     "msg": "Hello World"
# }
# msg = json.dumps(msg_dict)
# producer.send(b'auto_vest', msg)
# producer.close()
#
# consumer = KafkaConsumer('auto_vest', bootstrap_servers=['kafka-service-0.kafka-service-headless.test:9092'])
# print(consumer)
# # 这是一个永久堵塞的过程，生产者消息会缓存在消息队列中,并且不删除,所以每个消息在消息队列中都有偏移
# # consumer是一个消息队列，当后台有消息时，这个消息队列就会自动增加．所以遍历也总是会有数据，当消息队列中没有数据时，就会堵塞等待消息带来
# for message in consumer:
#     print("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition, message.offset, message.key, message.value))
#
# # !/usr/bin/env python
# # -*- coding: utf-8 -*-
# import datetime
# import json
# import time
# import uuid
#
# # from kafka import KafkaProducer
# from kafka.errors import KafkaError
#
# # producer = KafkaProducer(bootstrap_servers='kafka-service-0.kafka-service-headless.test:9092')
# # print(producer)
# # topic = 'test_20181105'
#
# #
# # def test():
# #     print('begin')
# #     try:
# #         n = 0
# #         while True:
# #             dic = {}
# #             dic['id'] = n
# #             n = n + 1
# #             dic['myuuid'] = str(uuid.uuid4().hex)
# #             dic['time'] = datetime.datetime.now().strftime("%Y%m%d %H:%M:%S")
# #             producer.send(topic, json.dumps(dic).encode())
# #             print("send:" + json.dumps(dic))
# #             time.sleep(0.5)
# #     except KafkaError as e:
# #         print(e)
# #     finally:
# #         producer.close()
# #         print('done')
# #
# #
# # if __name__ == '__main__':
# #     test()
# # import kafka
# # def create_topic(topic='topic', num_partitions=3, configs=None, timeout_ms=3000, brokers=['kafka-service-0.kafka-service-headless.test:9092'],
# #                  no_partition_change=True):
# #     client =kafka.KafkaClient(bootstrap_servers=brokers)
# #
# #     if topic not in client.cluster.topics(exclude_internal_topics=True):  # Topic不存在
# #
# #         request = kafka.(
# #             create_topic_requests=[(
# #                 topic,
# #                 num_partitions,
# #                 -1,  # replication unset.
# #                 [],  # Partition assignment.
# #                 [(key, value) for key, value in configs.items()],  # Configs
# #             )],
# #             timeout=timeout_ms
# #         )
# #
# #         future = client.send(2, request)  # 2是Controller,发送给其他Node都创建失败。
# #         client.poll(timeout_ms=timeout_ms, future=future, sleep=False)  # 这里
# #
# #         result = future.value
# #         # error_code = result.topic_error_codes[0][1]
# #         print("CREATE TOPIC RESPONSE: ", result)  # 0 success, 41 NOT_CONTROLLER, 36 ALREADY_EXISTS
# #         client.close()
# #     else:  # Topic已经存在
# #         print("Topic already exists!")
# #         return


consumer = KafkaConsumer(bootstrap_servers=["kafka-service-0.kafka-service-headless.test:9092"],
                         enable_auto_commit=False, auto_commit_interval_ms=100, group_id="vest",
                         auto_offset_reset='earliest')
consumer.subscribe(['auto_vest', ])

# print(consumer)

s = 1
while s <= 100:
    msg_dict = consumer.poll(timeout_ms=100000, max_records=100)
    consumer.commit()
    for msg_value in msg_dict.values():
        for msg in msg_value:
            card_info = json.loads(msg.value)
            print(card_info)
            print(msg.offset)
            print(msg.partition)
    s += 1
    time.sleep(10)

# consumer.assign([
#     TopicPartition(topic='auto_vest', partition=0),
#     TopicPartition(topic='auto_vest', partition=1),
#     TopicPartition(topic='auto_vest', partition=2)
# ])
#
# consumer.seek(TopicPartition(topic='auto_vest', partition=0), 12)  # 指定起始offset为12
# consumer.seek(TopicPartition(topic='auto_vest', partition=1), 0)  # 可以注册多个分区，此分区从第一条消息开始接收
#
# for msg in consumer:
#     print(msg)

# import random
#
# user_list = [1, 2, 3]
# need_comment_num = 1
# ss = random.sample(user_list, 2)
#
# print(ss)

# import pypinyin
#
# from pypinyin import pinyin, lazy_pinyin
#
# query = "中心"
# # sss = bytes(query, encoding="utf8")
# # print(sss)
# ss = lazy_pinyin(query)
# str_query = ''
# for item in ss:
#     str_query += str(item)
# print(str_query)
#
# print(time.time())
# name = "Q Max祛斑王"
# sss  = str(name).lower()
# print(sss)
#
#
# def set_highlihgt(query=None, ori_name=None):
#     ###高亮调整
#     all_word = set()
#     query2 = ori_name
#     for item in range(0, len(query)):
#         all_word.add(query[item])
#
#     print(all_word)
#     for item in all_word:
#         is_find = query2.find(item)
#         if is_find >= 0:
#             highlight_marks = u'<>%s</>' % item
#             high_query = query2.replace(item, highlight_marks)
#             query2 = high_query
#
#         highlight_name = query2.replace('<>', '<ems>').replace('</>', '</ems>')
#
#     return highlight_name
#
#
# highlight_name = set_highlihgt(query="眼叫", ori_name="e开外眼角")
# print(highlight_name)
#
# import datetime
#
# days = datetime.datetime.now()
# if days.month < 10:
#     month = "0" + str(days.month)
#
# if days.day < 10:
#     day = "0" + str(days.day)
#
# date = str(days.year) + month + day
#
#
# print(date)