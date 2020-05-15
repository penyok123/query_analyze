import json
from kafka import KafkaConsumer
import threading
import sys
import datetime
import time

threads = []


# col_dic, sql_dic = get()


class MyThread(threading.Thread):
    def __init__(self, thread_name):
        threading.Thread.__init__(self)
        self.thread_name = thread_name

    def run(self):
        print("Starting " + self.name)
        Consumer(self.thread_name)

    def stop(self):
        sys.exit()


def Consumer(thread_name):
    '''
    fetch_min_bytes（int） - 服务器为获取请求而返回的最小数据量，否则请等待
    fetch_max_wait_ms（int） - 如果没有足够的数据立即满足fetch_min_bytes给出的要求，服务器在回应提取请求之前将阻塞的最大时间量（以毫秒为单位）
    fetch_max_bytes（int） - 服务器应为获取请求返回的最大数据量。这不是绝对最大值，如果获取的第一个非空分区中的第一条消息大于此值，
                            则仍将返回消息以确保消费者可以取得进展。注意：使用者并行执行对多个代理的提取，因此内存使用将取决于包含该主题分区的代理的数量。
                            支持的Kafka版本> = 0.10.1.0。默认值：52428800（50 MB）。
    enable_auto_commit（bool） - 如果为True，则消费者的偏移量将在后台定期提交。默认值：True。
    max_poll_records（int） - 单次调用中返回的最大记录数poll()。默认值：500
    max_poll_interval_ms（int） - poll()使用使用者组管理时的调用之间的最大延迟 。这为消费者在获取更多记录之前可以闲置的时间量设置了上限。
                                如果 poll()在此超时到期之前未调用，则认为使用者失败，并且该组将重新平衡以便将分区重新分配给另一个成员。默认300000
    '''
    consumer = KafkaConsumer(bootstrap_servers=["kafka-service-0.kafka-service-headless.test:9092"],
                             group_id="vest",
                             client_id=thread_name,
                             enable_auto_commit=True,
                             # fetch_min_bytes=1024 * 1024,  # 1M
                             # fetch_max_bytes=1024 * 1024 * 1024 * 10,
                             # fetch_max_wait_ms=60000,  # 30s
                             # request_timeout_ms=305000,
                             # consumer_timeout_ms=1,
                             # max_poll_records=5000,
                             # max_poll_interval_ms=60000 无该参数
                             auto_commit_interval_ms=100,
                             # topic='auto_vest',
                             auto_offset_reset='earliest'

                             )
    consumer.subscribe(['auto_vest', ])

    # 查出数据库上次保存的offset，此offset已经是上次消费最后一条的offset的offset+1,也就是这次消费的起始位
    # 分配该消费者的TopicPartition，也就是topic和partition，根据参数，我是三个消费者，三个线程，每个线程消费者消费一个分区
    # 重置此消费者消费的起始位
    num = 0  # 记录该消费者消费次数
    # end_offset = consumer.end_offsets([tp])[tp]
    # print(end_offset)
    s = 1
    while True:
        print(s)
        start_time = time.time()
        msg_dict = consumer.poll(timeout_ms=100, max_records=1)
        consumer.commit_async()
        print("cost  :", time.time() - start_time)

        for msg in msg_dict.values():
            for msg_value in msg:
                card_info = json.loads(str(msg_value.value, encoding="utf8"))
                print(datetime.datetime.now())
                print("程序首次运行\t线程:", thread_name, "分区:", msg_value.partition, "偏移量:", msg_value.offset, "\t开始消费...")

                print("消费到新数据了:%s" % (card_info))
        s += 1


if __name__ == '__main__':
    try:
        start_time = time.time()
        t0 = MyThread("Thread-0")
        threads.append(t0)
        t1 = MyThread("Thread-1")
        threads.append(t1)
        t2 = MyThread("Thread-2")
        threads.append(t2)
        t3 = MyThread("Thread-3")
        threads.append(t3)
        t4 = MyThread("Thread-4")
        threads.append(t4)
        t5 = MyThread("Thread-5")
        threads.append(t5)
        t6 = MyThread("Thread-6")
        threads.append(t6)
        t7 = MyThread("Thread-7")
        threads.append(t7)
        t8 = MyThread("Thread-8")
        threads.append(t8)

        for t in threads:
            t.start()

        for t in threads:
            t.join()
        print("cost  :", time.time() - start_time)
        print("exit program with 0")
    except:
        print("Error: failed to run consumer program")
