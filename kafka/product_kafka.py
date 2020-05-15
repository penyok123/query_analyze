# #!/usr/bin/env python
# # -*- coding: utf-8 -*-
# from kafka import KafkaConsumer
# from django.conf import settings
# import json
# from kafka import KafkaProducer
#
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


from kafka import KafkaProducer
import time
import json

producer = KafkaProducer(bootstrap_servers=["kafka-service-0.kafka-service-headless.test:9092"])

dic = {}
i = 1

while True:
    msg_dic = {
        "card_id": i,
        "card_user_id": 23243 + i,
        "card_type": "auto_vest",
        "create_time": "2020-04-09 09:55:43",
        "content_level": 6,
        "tag_names": ["瘦脸针kyc", "鼻综合kyc"],
        "type": "get_write_answer_userinfo",
        "current_push_time": "kafka/product_kafka.py:109",
        'action_type': 'follow'
    }
    print(producer)
    producer.send('auto_vest', json.dumps(msg_dic).encode())
    print("----")

    i += 1
producer.close()
