# -*- coding: utf-8 -*-
from pyhive import hive
import thrift



from itertools import zip_longest
from pyhive import hive
from functools import wraps


class Retry(object):
    def __init__(self, retry=3):
        self.retry = retry

    def __call__(self, func):
        @wraps(func)
        def wrapped_func(conn, query_sql):
            retry_count = 0
            while retry_count < self.retry:
                try:
                    return func(conn, query_sql)
                except Exception as e:
                    print(str(e))
                    conn.init_connection()
                    retry_count += 1
                    continue
            raise Exception("多次重试仍然失败，sql语句为: " + query_sql)

        return wrapped_func


class HiveClient(object):

    def __init__(self, host, port, username, password, auth='CUSTOM'):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.auth = auth
        self.init_connection()

    def init_connection(self):
        self.conn = hive.Connection(host=self.host, port=self.port, username=self.username,
                                    password=self.password, auth=self.auth)

    @Retry()
    def query(self, query_sql):
        datas = []
        curosr = self.conn.cursor()
        curosr.execute(query_sql)
        clumns = curosr.description
        for result in curosr.fetchall():
            item = {}
            for key, value in zip_longest(clumns, result):
                item[key[0]] = value
                datas.append(item)

        curosr.close()
        return datas


hc = HiveClient(host='jdbc:mysql://rm-m5e842126ng59jrv6.mysql.rds.aliyuncs.com:3306/hive', port=10000, username='hive_xmtnrifc2c')
sql = "select * from user"
data = hc.query(sql)
print(data)


conn = hive.Connection(host='jdbc:mysql://rm-m5e842126ng59jrv6.mysql.rds.aliyuncs.com:3306/hive', port=10000,
                       username='hive_xmtnrifc2c', database='default')
cursor = conn.cursor()
cursor.execute('select * from demo_table limit 10')
for result in cursor.fetchall():
    print(result)