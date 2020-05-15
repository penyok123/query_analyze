# -*- coding: UTF-8 -*-
import datetime
import time
import logging
import traceback
import random
from kafka import KafkaProducer
import random
from django.conf import settings
import json, redis
import pymysql
import socket

CELERY_BROKER_URL = 'redis://redis.paas-test.env:6379/0'
REDIS_URL = 'redis://redis.paas-test.env:6379/0'
REDIS_URL2 = 'redis://redis.paas-test.env:6379/0'
redis_client = redis.StrictRedis.from_url(REDIS_URL)
# from base
# from base
ENGINE = 'django.db.backends.mysql',  # 设置为mysql数据库
NAME = 'mimas_test'
USER = 'work'
PASSWORD = 'Gengmei1'
HOST = 'bj-cdb-6slgqwlc.sql.tencentcdb.com'
PORT = 62120

ENGINE1 = 'django.db.backends.mysql',  # 设置为mysql数据库
NAME1 = 'zhengxing_test'
USER1 = 'work'
PASSWORD1 = 'Gengmei1'
HOST1 = 'bj-cdb-6slgqwlc.sql.tencentcdb.com'

logger = logging.getLogger(__name__)

db_mimas_eagle = pymysql.connect(host=HOST, port=PORT, user=USER,
                                 password=PASSWORD,
                                 db=NAME, charset='utf8')

mimas_cursor = db_mimas_eagle.cursor()

db_zhengxing_eagle = pymysql.connect(host=HOST1, port=PORT, user=USER1,
                                     password=PASSWORD1,
                                     db=NAME1, charset='utf8')

zhengxing_cursor = db_zhengxing_eagle.cursor()


def get_vest_userid_and_comment(need_comment_num=0, tag_names=[], card_id=0):
    try:
        if need_comment_num:
            all_comment_list = []
            content = []
            redis_key = "vest_kyc_tag_content_data"
            group_keys = "get_group_comment_by_tag:group_id"
            for item in tag_names:
                ##如果自带的标签有kyc的话走kyc的标签
                service_closure_tags = redis_client.hget(redis_key, str(item))
                if service_closure_tags:
                    closure_tags = json.loads(str(service_closure_tags, encoding="utf-8"))
                    all_comment_list.extend(closure_tags)

            if all_comment_list:
                content = random.sample(all_comment_list, need_comment_num)
            else:
                ##没有kyc的标签看标签所属的小组 拿对应小组的数据
                all_group_ids = set()
                all_comments = []
                for item in tag_names:
                    sql_get_tagid = "select  id from api_tag WHERE  name =  '%s'" % (item)
                    zhengxing_cursor.execute(sql_get_tagid)
                    data = zhengxing_cursor.fetchall()
                    if len(data):
                        tag_ids = data[0]
                        # ids = data[0][0]
                        sql = 'select tag_category_id from api_tag_category_relation where tag_id =  %s' % (tag_ids)
                        zhengxing_cursor.execute(sql)
                        group_ids = zhengxing_cursor.fetchall()
                        for item in group_ids:
                            all_group_ids.add(item[0])

                for all_group_id in list(all_group_ids):
                    get_comment = redis_client.hget(group_keys, int(all_group_id))
                    if get_comment:
                        comment = json.loads(str(get_comment, encoding="utf-8"))
                        all_comment_list.extend(comment)

                content = random.sample(all_comment_list, need_comment_num)
        zhengxing_cursor.close()
        return content

    except:
        logging.error("catch exception,err_msg:%s" % traceback.format_exc())
        return []


sss = get_vest_userid_and_comment(need_comment_num=10, tag_names=["Y", "端午三级", "微创双眼皮1"])
print(sss)
