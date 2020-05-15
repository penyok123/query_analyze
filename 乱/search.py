# -*- coding: utf-8 -*-
from __future__ import division
from __future__ import print_function
import json
import msgpack
import pymysql
import time
import smtplib
import traceback
from email.mime.text import MIMEText
from email.utils import formataddr
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import logging
import redis
import reload
import sys


def gbk_decoder(s):
    if not s:
        return None
    else:
        try:
            data = msgpack.loads(s, encoding='utf-8')
            return data
        except Exception as e:
            print(e)
            data = json.loads(s)
            return data

    # rdd transform


def get_data(x):
    try:
        data = x[1]
        card_content_type = ""
        index_type = ""
        search_query = ""
        db_tag_name = ""
        card_id = ""
        device_id = ""
        sql = ""
        tag_name_key = ""

        tag_names_list = list()
        # 先获取首页feed的数据
        if data["type"] == "on_click_card":
            device_id = data["device"]["device_id"]
            card_id = data["params"]["card_id"]
            ###diary qa user_post
            card_content_type = data["params"]["card_content_type"]
            if card_content_type == "diary":
                db_tag_name = "api_diary_tags"
            elif card_content_type == "qa":
                db_tag_name = "api_questiontag"
            elif card_content_type == "user_post":
                db_tag_name = "api_tractate_tag"
            else:
                db_tag_name = ""

        # 获取搜索的数据
        if data["type"] == "do_search":
            device_id = data["device"]["device_id"]
            search_query = data["params"]["query"]

        # 获取综搜页的日记卡片的数据
        if data["type"] == "on_click_diary_card":
            device_id = data["device"]["device_id"]
            # search_query = data.txt["params"]["query"]
            card_id = data["params"]["diary_id"]
            db_tag_name = "api_diary_tags"

        if data["type"] == "search_result_welfare_click_item":
            device_id = data["device"]["device_id"]
            card_id = data["params"]["business_id"]
            # search_query = data.txt["params"]["query"]
            db_tag_name = "api_servicetag"

        ##连接数据库去获取数据
        db_zhengxing_eagle = pymysql.connect(host="bj-cdb-6slgqwlc.sql.tencentcdb.com", port=62120, user="work",
                                             password="Gengmei1",
                                             db="zhengxing_test",
                                             cursorclass=pymysql.cursors.DictCursor)

        db_miams_eagle = pymysql.connect(host="bj-cdb-6slgqwlc.sql.tencentcdb.com", port=62120, user="work",
                                         password="Gengmei1",
                                         db="mimas_test",
                                         cursorclass=pymysql.cursors.DictCursor)

        zhengxing_cursor = db_zhengxing_eagle.cursor()
        mimas_cursor = db_miams_eagle.cursor()

        print(db_tag_name)
        if db_tag_name == "api_diary_tags":
            sql = 'select name from api_tag where id in (select tag_id from api_diary_tags where diary_id = %s) and tag_type in (1,2,3)' % (
                card_id)
            zhengxing_cursor.execute(sql)
            data = zhengxing_cursor.fetchall()
            for name in list(data):
                print(name)
                tag_names_list.append(name.get("name", None))

        elif db_tag_name == "api_servicetag":
            sql = 'select name from api_tag where id in (select tag_id from api_servicetag where service_id = %s) and tag_type in (1,2,3)' % (
                card_id)

            zhengxing_cursor.execute(sql)
            print(sql)
            data = zhengxing_cursor.fetchall()
            for name in list(data):
                tag_names_list.append(name.get("name", None))

        elif db_tag_name == "api_questiontag":
            sql = "select tag_id from api_questiontag where question_id = (select question_id from api_answer where id = %s) and tag_type in (1,2,3)" % (
                card_id)
            mimas_cursor.execute(sql)
            question_id = mimas_cursor.fetchall()
            question_id_list = list(question_id)
            print(question_id_list)
            tags = []
            if len(question_id_list) > 0:
                for id in question_id_list:
                    tags.append(id.get("tag_id", None))
                sql = 'select name from api_tag where id in (%s)' % ', '.join(list(map(lambda x: "'%s'" % x, tags)))
                zhengxing_cursor.execute(sql)
                data = zhengxing_cursor.fetchall()
                for name in list(data):
                    tag_names_list.append(name.get("name", None))

        elif db_tag_name == "api_tractate_tag":

            sql = "select tag_id from api_tractate_tag where tractate_id = %s " % (card_id)
            mimas_cursor.execute(sql)
            data = mimas_cursor.fetchall()
            tag_ids = list(data)
            print(tag_ids)
            tags = []
            if len(tag_ids) > 0:
                for item in tag_ids:
                    tags.append(item.get("tag_id", None))
                sql = 'select name from api_tag where id in (%s) and tag_type in (1,2,3)' % ', '.join(
                    list(map(lambda x: "'%s'" % x, tags)))
                zhengxing_cursor.execute(sql)
                data = zhengxing_cursor.fetchall()
                for name in list(data):
                    tag_names_list.append(name.get("name", None))

        else:
            pass

        if search_query is not "":
            print('-----bbbbbbbbbbb---------')
            tag_names_list.append(search_query)

            print(tag_names_list)

        tag_name_key = ""
        if device_id is not None and len(tag_names_list) > 0:
            ##把拿到的数据存到redis中根据device_id
            redis_client = redis.Redis(host='redis.paas-test.env', port=6379, socket_timeout=5000, db=3)

            tag_name_key = "user_click_search_query:device_id:" + str(device_id)
            print("+++++++")
            print(tag_names_list)
            print("+++++++")

            redis_client.set(tag_name_key, json.dumps(tag_names_list))

        return tag_names_list, tag_name_key

    except:
        logging.error("catch exception,logins:%s" % traceback.format_exc())
        return None


# def Json(data.txt):
#     # data.txt = json.loads(x)
#     ##先获取首页的数据
#     if "type" in data.txt and "params" in data.txt and "device" in data.txt and "card_content_type" in data.txt["params"]:
#         if data.txt["type"] == "on_click_card" and data.txt["params"]["card_content_type"] in ["qa", "diary", "user_post"]:
#             return True
#
#     ##获取搜索框进行搜索的数据
#     elif "type" in data.txt and "params" in data.txt and "device" in data.txt and "query" in data.txt["params"]:
#         if data.txt["type"] == "do_search" and data.txt["params"]["tab"] in ["综合", "美购", "日记", "百科", "帖子"] and data.txt["params"][
#             "input_type"] in ["历史", "联想", "发现"]:
#             return True
#
#     ##获取综合搜索页的数据（只有日记）
#     elif "type" in data.txt and "params" in data.txt and "device" in data.txt and "diary_id" in data.txt["params"]:
#         print("---hhhhhhhhhhh----")
#         if data.txt["type"] == "on_click_diary_card" and data.txt["params"]["business_type"] in ["diary"]:
#             return True
#
#     ##获取美购日记tab下的数据
#     elif "type" in data.txt and "params" in data.txt and "device" in data.txt and "params" in data.txt:
#         if data.txt["type"] == "search_result_welfare_click_item" and data.txt["params"]["page_name"] in [
#             "search_result_welfare"]:
#             return True
#     else:
#         return False


def model(i):
    try:

        bo = Json(i)
        tag_names_list, tag_name_key = get_data(i)

        return bo, tag_names_list, tag_name_key
    except:
        print("fail")
        print(traceback.format_exc())


data = [(None, {'create_at': '1567563851', 'gm_nginx_timestamp': 1567563851.983, 'user_id': '', 'version': '147',
                'params': {'is_cpc': 0, 'tab_name': '帖子', 'cpc_referer': '1', 'query': '测试x', 'diary_id': '422',
                           'business_type': 'diary', 'position': 2, 'item_type': 0, 'page_name': 'search_result_more'},
                'app_session_id': 'ce218fbf-6206-43d3-942c-088039dafc90',
                'app': {'version': '7.14.1', 'grey_type': '{"home": "0", "post_detail": "0"}', 'current_city_id': '',
                        'user_type': {'config_type': '1'}, 'name': 'gengmei_user', 'serial_id': 131,
                        'channel': 'benzhan'}, 'gm_nginx_key': 1,
                'device': {'android_device_id': 'androidid_27d76d00d7dd9e88', 'sys_version': '7.1.1',
                           'lng': '116.486535', 'is_WiFi': '1', 'lat': '40.001305', 'device_id': '867961035707277',
                           'manufacturer': 'OPPO', 'net_type': 'wifi', 'device_type': 'android', 'ip': '172.30.8.39',
                           'model': 'OPPO R11st'}, 'type': 'on_click_diary_card'}),
        (None, {'create_at': '1567563851', 'gm_nginx_timestamp': 1567563852.043, 'user_id': '', 'version': '147',
                'params': {'down_loading_times': 1, 'business_id': '', 'page_name': 'search_result_more',
                           'exposure_cards': [
                               {'is_cpc': 0, 'result_status': '1', 'card_id': '4667393', 'absolute_position': 0,
                                'transaction_type': '-1', 'card_type': 'card', 'cpc_referer': '2',
                                'card_content_type': 'service', 'relative_position': 0},
                               {'is_cpc': 0, 'result_status': '1', 'card_id': '4667943', 'absolute_position': 1,
                                'transaction_type': '-1', 'card_type': 'card', 'cpc_referer': '2',
                                'card_content_type': 'service', 'relative_position': 0},
                               {'is_cpc': 1, 'result_status': '1', 'card_id': '5740140', 'absolute_position': 2,
                                'transaction_type': '-1', 'card_type': 'card', 'cpc_referer': '2',
                                'card_content_type': 'service', 'relative_position': 0},
                               {'is_cpc': 0, 'result_status': '1', 'card_id': '4667393', 'absolute_position': 0,
                                'transaction_type': '-1', 'card_type': 'card', 'cpc_referer': '2',
                                'card_content_type': 'service', 'relative_position': 0},
                               {'is_cpc': 0, 'result_status': '1', 'card_id': '4667943', 'absolute_position': 1,
                                'transaction_type': '-1', 'card_type': 'card', 'cpc_referer': '2',
                                'card_content_type': 'service', 'relative_position': 0},
                               {'is_cpc': 1, 'result_status': '1', 'card_id': '5740140', 'absolute_position': 2,
                                'transaction_type': '-1', 'card_type': 'card', 'cpc_referer': '2',
                                'card_content_type': 'service', 'relative_position': 0},
                               {'absolute_position': 0, 'cpc_referer': '1', 'transaction_type': '', 'card_type': 'card',
                                'card_content_type': 'answer', 'relative_position': 0, 'card_id': '531246'},
                               {'absolute_position': 1, 'cpc_referer': '1', 'transaction_type': '', 'card_type': 'card',
                                'card_content_type': 'answer', 'relative_position': 1, 'card_id': '530811'},
                               {'absolute_position': 2, 'cpc_referer': '1', 'is_cpc': 0, 'transaction_type': '-1',
                                'card_type': 'card', 'card_content_type': 'diary', 'relative_position': 2,
                                'card_id': 9458990},
                               {'absolute_position': 3, 'cpc_referer': '1', 'is_cpc': 0, 'transaction_type': '-1',
                                'card_type': 'card', 'card_content_type': 'diary', 'relative_position': 3,
                                'card_id': 422}], 'tab_name': '综合', 'down_slide_times': 1, 'query': '测试x', 'filter': '',
                           'referrer_id': '', 'referrer': 'search_home', 'up_loading_times': 0, 'is_exposure': '1',
                           'up_slide_times': 3}, 'app_session_id': 'ce218fbf-6206-43d3-942c-088039dafc90',
                'app': {'version': '7.14.1', 'grey_type': '{"home": "0", "post_detail": "0"}', 'current_city_id': '',
                        'user_type': {'config_type': '1'}, 'name': 'gengmei_user', 'serial_id': 133,
                        'channel': 'benzhan'}, 'gm_nginx_key': 'gzip',
                'device': {'android_device_id': 'androidid_27d76d00d7dd9e88', 'sys_version': '7.1.1',
                           'lng': '116.486535', 'is_WiFi': '1', 'lat': '40.001305', 'device_id': '867961035707277',
                           'manufacturer': 'OPPO', 'net_type': 'wifi', 'device_type': 'android', 'ip': '172.30.8.39',
                           'model': 'OPPO R11st'}, 'type': 'page_precise_exposure'})
        ]


def Json(x):
    print("json------------------")
    # data.txt = json.loads(x[1])
    data = x[1]
    ##先获取首页的数据
    print(data)
    print(type(data))

    if 'type' in data and 'params' in data and "device" in data and "card_content_type" in data["params"] and data[
        "type"] == "on_click_card" and data["params"]["card_content_type"] in ["qa", "diary", "user_post"]:
        print("------11111111-------")
        return True

    ##获取搜索框进行搜索的数据
    elif "type" in data and "params" in data and "device" in data and "query" in data["params"] and data[
        "type"] == "do_search" and data["params"]["tab"] in ["综合", "美购", "日记", "百科", "帖子"] and data["params"][
        "input_type"] in ["历史",
                          "联想",
                          "发现"]:
        print("------22222222-------")
        return True

    ##获取综合搜索页的数据（只有日记）
    elif "type" in data and "params" in data and "device" in data and "diary_id" in data["params"] and data[
        "type"] == "on_click_diary_card" and data["params"]["business_type"] in ["diary"]:
        print("--f-fffffffffff----")
        return True

    ##获取美购日记tab下的数据
    elif "type" in data and "params" in data and "device" in data and "params" in data and data[
        "type"] == "search_result_welfare_click_item" and data["params"]["page_name"] in [
        "search_result_welfare"]:
        print("------33333333-------")
        return True
    else:
        return False

        print(True)
        print("-------")


for i in data:
    bo = Json(i)
    print("-------------------------")

    if bo == True:
        get_data(i)
