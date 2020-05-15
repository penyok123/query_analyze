#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pymysql
import sys


def check_contain_chinese(check_str):
    for item in ['照片', '视频', '模拟', '音乐', '漂亮', '陈乔恩', '包邮', '大礼包', '试用', '招募', '首付', '返现', '富二代', '无门槛', '网站',
                 '拍照', '我爱你', '女生', '护肤品', '星座', '图片', '小妹妹', '面膜', '内衣', '钻石', '错误', '长图', '长大', '免费', '埃菲尔', '埃伦',
                 '垃圾', '垂钓', '坐标北京', '坐肚子', '唯一的爱', '地毛天', '地址', '地毛天', '在线', '签到', '圣诞', '土豪', '土豆', '炒肉', '土妞',
                 '女孩', '女生', '发型', '球球', '背景', '美女', '图案', '图像', '老公', '国外', '国内', '固定', '团圆', '爱情', '因为',
                 '回来', '年级', '大学', '岁', '口红', '嘻', '哈', '皇宫', '嗯', '礼拜', '李白', '辣辣', '啦啦', '夏天', '啤酒肚', '文明', '扫一扫',
                 '积极', '哒哒', '呀呀', '啊', '哈哈', '哇', '咳嗽', '咨询', '咖啡', '和平精英', '酒店', '味道', '呃']:

        ##案例  什么
        if item in check_str:
            return False
    for ch in check_str:
        if u'\u4e00' <= ch <= u'\u9fff':
            return True
    return False


def judge_tag_info(word):
    db_zhengxing_eagle = pymysql.connect(host="bj-cdb-6slgqwlc.sql.tencentcdb.com", port=62120, user="work",
                                         password="Gengmei1",
                                         db="zhengxing_test",
                                         charset='utf8',
                                         cursorclass=pymysql.cursors.DictCursor)
    zhengxing_cursor = db_zhengxing_eagle.cursor()
    sql = "select  id from api_tag WHERE  name =  '%s'" % (word)
    zhengxing_cursor.execute("set names 'UTF8'")
    zhengxing_cursor.execute(sql)
    data = zhengxing_cursor.fetchall()
    if data:
        return True
    else:
        return False


def judge_doctor_info(word):
    db_zhengxing_eagle = pymysql.connect(host="bj-cdb-6slgqwlc.sql.tencentcdb.com", port=62120, user="work",
                                         password="Gengmei1",
                                         db="zhengxing_test",
                                         charset='utf8',
                                         cursorclass=pymysql.cursors.DictCursor)
    zhengxing_cursor = db_zhengxing_eagle.cursor()
    sql = "select  id from api_doctor WHERE  name =  '%s'" % (word)
    zhengxing_cursor.execute("set names 'UTF8'")
    zhengxing_cursor.execute(sql)
    data = zhengxing_cursor.fetchall()
    if data:
        return True
    else:
        return False


def judge_hospital_info(word):
    db_zhengxing_eagle = pymysql.connect(host="bj-cdb-6slgqwlc.sql.tencentcdb.com", port=62120, user="work",
                                         password="Gengmei1",
                                         db="zhengxing_test",
                                         charset='utf8',
                                         cursorclass=pymysql.cursors.DictCursor)
    zhengxing_cursor = db_zhengxing_eagle.cursor()
    sql = "select  id from api_hospital WHERE  name =  '%s'" % (word)
    zhengxing_cursor.execute("set names 'UTF8'")
    zhengxing_cursor.execute(sql)
    data = zhengxing_cursor.fetchall()
    if data:
        return True
    else:
        return False


def judge_itemwiki_info(word):
    db_zhengxing_eagle = pymysql.connect(host="bj-cdb-6slgqwlc.sql.tencentcdb.com", port=62120, user="work",
                                         password="Gengmei1",
                                         db="zhengxing_test",
                                         charset='utf8',
                                         cursorclass=pymysql.cursors.DictCursor)
    zhengxing_cursor = db_zhengxing_eagle.cursor()
    sql = "select  id from wiki_item WHERE  name =  '%s' or other_name ='%s'" % (word, word)
    zhengxing_cursor.execute("set names 'UTF8'")
    zhengxing_cursor.execute(sql)
    data = zhengxing_cursor.fetchall()
    if data:
        return True
    else:
        return False


def judge_productwiki_info(word):
    db_zhengxing_eagle = pymysql.connect(host="bj-cdb-6slgqwlc.sql.tencentcdb.com", port=62120, user="work",
                                         password="Gengmei1",
                                         db="zhengxing_test",
                                         charset='utf8',
                                         cursorclass=pymysql.cursors.DictCursor)
    zhengxing_cursor = db_zhengxing_eagle.cursor()
    sql = "select  id from wiki_product WHERE  name =  '%s' or other_name ='%s'" % (word, word)
    zhengxing_cursor.execute("set names 'UTF8'")
    zhengxing_cursor.execute(sql)
    data = zhengxing_cursor.fetchall()
    if data:
        return True
    else:
        return False


def judge_collectwiki_info(word):
    db_zhengxing_eagle = pymysql.connect(host="bj-cdb-6slgqwlc.sql.tencentcdb.com", port=62120, user="work",
                                         password="Gengmei1",
                                         db="zhengxing_test",
                                         charset='utf8',
                                         cursorclass=pymysql.cursors.DictCursor)
    zhengxing_cursor = db_zhengxing_eagle.cursor()
    sql = "select  id from wiki_collect WHERE  name =  '%s' or other_name ='%s'" % (word, word)
    zhengxing_cursor.execute("set names 'UTF8'")
    zhengxing_cursor.execute(sql)
    data = zhengxing_cursor.fetchall()
    if data:
        return True
    else:
        return False


def judge_brandwiki_info(word):
    db_zhengxing_eagle = pymysql.connect(host="bj-cdb-6slgqwlc.sql.tencentcdb.com", port=62120, user="work",
                                         password="Gengmei1",
                                         db="zhengxing_test",
                                         charset='utf8',
                                         cursorclass=pymysql.cursors.DictCursor)
    zhengxing_cursor = db_zhengxing_eagle.cursor()
    sql = "select  id from wiki_brand WHERE  name =  '%s' or other_name ='%s'" % (word, word)
    zhengxing_cursor.execute("set names 'UTF8'")
    zhengxing_cursor.execute(sql)
    data = zhengxing_cursor.fetchall()
    if data:
        return True
    else:
        return False


def judge_api_wordrel_info(word):
    db_zhengxing_eagle = pymysql.connect(host="bj-cdb-6slgqwlc.sql.tencentcdb.com", port=62120, user="work",
                                         password="Gengmei1",
                                         db="zhengxing_test",
                                         charset='utf8',
                                         cursorclass=pymysql.cursors.DictCursor)
    zhengxing_cursor = db_zhengxing_eagle.cursor()
    sql = "select  id from api_wordrel WHERE  keyword =  '%s' " % (word)
    zhengxing_cursor.execute("set names 'UTF8'")
    zhengxing_cursor.execute(sql)
    data = zhengxing_cursor.fetchall()
    if data:
        return True
    else:
        return False


data = open("sort_search_word_from_guangyu.txt", "r", encoding="utf-8")
mysql_not_have_word = []
mysql_have_word = []

for item in data.readlines():
    if check_contain_chinese(item):
        mysql_have_word.append(item)
        # if judge_tag_info(word=item):
        #     mysql_have_word.append(item)
        # elif judge_doctor_info(word=item):
        #     mysql_have_word.append(item)
        # elif judge_hospital_info(word=item):
        #     mysql_have_word.append(item)
        # elif judge_itemwiki_info(word=item):
        #     mysql_have_word.append(item)
        # elif judge_productwiki_info(word=item):
        #     mysql_have_word.append(item)
        # elif judge_brandwiki_info(word=item):
        #     mysql_have_word.append(item)
        # elif judge_collectwiki_info(word=item):
        #     mysql_have_word.append(item)
        # elif judge_api_wordrel_info(item):
        #     mysql_have_word.append(item)
        # else:
        #     mysql_not_have_word.append(item)
    else:
        mysql_not_have_word.append(item)

print(len(mysql_not_have_word))
print(mysql_not_have_word)
