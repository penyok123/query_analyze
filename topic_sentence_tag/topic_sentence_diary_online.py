# coding=utf-8
# -*- coding:utf-8 -*-
from simhash import Simhash
import re
import pymysql
import time, redis, jieba

REDIS_URL2 = 'redis://:ReDis!GmTx*0aN9@172.16.40.173:6379'

redis_client2 = redis.StrictRedis.from_url(REDIS_URL2)


class Analyze:
    db_miams_eagle = None
    mimas_cursor = None

    def __init__(self):
        pass

    def cnt_mysql_mimas(self):

        db_miams_eagle = pymysql.connect(host="172.16.30.138", port=3306, user="mimas",
                                         password="GJL3UJe1Ck9ggL6aKnZCq4cRvM",
                                         db="mimas_prod",
                                         charset='utf8',
                                         cursorclass=pymysql.cursors.DictCursor)

        mimas_cursor = db_miams_eagle.cursor()

        return mimas_cursor, db_miams_eagle

    def cnt_mysql_zhengxing(self):

        db_miams_eagle = pymysql.connect(host="172.16.30.143", port=3306, user="work",
                                         password="BJQaT9VzDcuPBqkd",
                                         db="zhengxing",
                                         charset='utf8',
                                         cursorclass=pymysql.cursors.DictCursor)

        mimas_cursor = db_miams_eagle.cursor()

        return mimas_cursor, db_miams_eagle

    def cnt_mysql_jerry(self):
        db_miams_eagle = pymysql.connect(host="172.16.40.170", port=4000, user="st_user",
                                         password="aqpuBLYzEV7tML5RPsN1pntUzFy",
                                         db="jerry_test",
                                         cursorclass=pymysql.cursors.DictCursor, charset='utf8')
        mimas_cursor = db_miams_eagle.cursor()

        return mimas_cursor, db_miams_eagle

    def get_new_tag(self):
        all_attr_sec_demands = []
        all_attr_fir_demands = []
        all_attr_sec_solutions = []
        all_attr_fir_solutions = []
        all_attr_sec_position = []
        all_attr_fir_position = []

        mimas_cursor, db_miams_eagle = self.cnt_mysql_zhengxing()
        sql = 'select id,name from api_tag_3_0 where is_online =1 and tag_type=1'
        mimas_cursor.execute(sql)
        all_project_tag = list(mimas_cursor.fetchall())

        sql = 'select id,name,aggregate_type from api_tag_attr where is_online =1 '
        mimas_cursor.execute(sql)
        all_project_tag_attr = list(mimas_cursor.fetchall())

        for item in all_project_tag_attr:
            tp = item.get("aggregate_type")
            if tp == "2":
                all_attr_sec_solutions.append(item)

            if tp == "3":
                all_attr_sec_position.append(item)

            if tp == "6":
                all_attr_fir_position.append(item)

            if tp == "7":
                all_attr_fir_demands.append(item)

            if tp == "8":
                all_attr_sec_demands.append(item)

            if tp == "10":
                all_attr_fir_solutions.append(item)

        db_miams_eagle.close()
        return {"all_project_tag": all_project_tag, "all_attr_sec_demands": all_attr_sec_demands,
                "all_attr_fir_demands": all_attr_fir_demands, "all_attr_sec_solutions": all_attr_sec_solutions,
                "all_attr_fir_solutions": all_attr_fir_solutions, "all_attr_sec_position": all_attr_sec_position,
                "all_attr_fir_position": all_attr_fir_position}

    def write_mysql(self, diary_id, diary_info):
        try:

            second_dem = [item.get("name", []) for item in diary_info['second_dem']]
            second_pop = [item.get("name", []) for item in diary_info['second_pop']]
            second_solu = [item.get("name", []) for item in diary_info['second_solu']]
            first_dem = [item.get("name", []) for item in diary_info['first_dem']]
            first_solu = [item.get("name", []) for item in diary_info['first_solu']]
            first_pop = [item.get("name", []) for item in diary_info['first_pop']]
            tagv3_name = [item.get("name", []) for item in diary_info['tagv3_name']]

            mimas_cursor, db_miams_eagle = self.cnt_mysql_jerry()
            sql = """ INSERT INTO diary_purport_get_tagv3(content_id,second_demands,second_solutions,second_positions,first_demands,first_solutions,first_positions,project_tags) VALUES(%s,%s,%s,%s,%s,%s,%s,%s) """
            data = (diary_id, ",".join(second_dem), ",".join(second_solu), ",".join(second_pop), ",".join(first_dem),
                    ",".join(first_solu), ",".join(first_pop), ",".join(tagv3_name))

            print(data)
            mimas_cursor.execute(sql, data)
            db_miams_eagle.commit()
            print('数据写入成功:%s' % diary_id)
        except Exception as e:
            db_miams_eagle.rollback()
            print('数据写入失败:%s' % e)

    def get_diary_content(self):
        mimas_cursor, db_mimas_eagle = self.cnt_mysql_mimas()
        sql = "select  answer from api_problem where diary_id =  1  and flag ='n' order by operation_time,id desc "
        mimas_cursor.execute(sql)
        content = mimas_cursor.fetchall()
        if content:
            con = content[0].get("answer", None)
            return con[:20]
        return None


class DiaryGetNewTag:
    diary_id = None
    diary_pop = None
    new_tag = {}

    def __init__(self, diary_pop, diary_id, new_tag):
        self.diary_pop = diary_pop
        self.diary_id = diary_id
        self.new_tag = new_tag

    def diary_get_tag(self):
        new_tag = self.new_tag

        tagv3_name = []
        first_pop = []
        first_solu = []
        first_dem = []
        second_pop = []
        second_solu = []
        second_dem = []

        all_project_tag = new_tag.get("all_project_tag", [])
        all_attr_sec_demands = new_tag.get("all_attr_sec_demands", [])
        all_attr_fir_demands = new_tag.get("all_attr_fir_demands", [])
        all_attr_sec_solutions = new_tag.get("all_attr_sec_solutions", [])
        all_attr_sec_position = new_tag.get("all_attr_sec_position", [])
        all_attr_fir_solutions = new_tag.get("all_attr_fir_solutions", [])
        all_attr_fir_position = new_tag.get("all_attr_fir_position", [])

        for item in all_project_tag:
            name = item.get("name", None)
            if name in self.diary_pop:
                tagv3_name.append(item)

        for item in all_attr_sec_demands:
            name = item.get("name", None)
            if name in self.diary_pop:
                second_dem.append(item)

        for item in all_attr_fir_demands:
            name = item.get("name", None)
            if name in self.diary_pop:
                first_dem.append(item)

        for item in all_attr_fir_solutions:
            name = item.get("name", None)
            if name in self.diary_pop:
                first_solu.append(item)

        for item in all_attr_sec_solutions:
            name = item.get("name", None)
            if name in self.diary_pop:
                second_solu.append(item)

        for item in all_attr_fir_position:
            name = item.get("name", None)
            if name in self.diary_pop:
                first_pop.append(item)

        for item in all_attr_sec_position:
            name = item.get("name", None)
            if name in self.diary_pop:
                second_pop.append(item)

        return {"tagv3_name": tagv3_name, "first_pop": first_pop, "first_solu": first_solu,
                "first_dem": first_dem, "second_pop": second_pop,
                "second_solu": second_solu, "second_dem": second_dem}


if __name__ == '__main__':
    begin = time.time()
    ana = Analyze()
    new_tag = ana.get_new_tag()
    keys = "doris:diary_content_abstract"
    get_diary_purport = ""
    redis_info = redis_client2.hgetall(keys)
    for key, val in redis_info.items():
        diary_id = str(key, encoding="utf-8")
        diary_pop = str(val, encoding="utf-8")
        if diary_pop:
            diary_t = DiaryGetNewTag(diary_id=diary_id, diary_pop=diary_pop, new_tag=new_tag)
        else:
            content = ana.get_diary_content()
            diary_t = DiaryGetNewTag(diary_id=diary_id, diary_pop=content, new_tag=new_tag)
        diary_info = diary_t.diary_get_tag()
        print(diary_info)
        ana.write_mysql(diary_id=diary_id, diary_info=diary_info)

    print(time.time() - begin)
