# !/usr/bin/python
# coding:utf8
import pymysql

buwei_data = open("buwei.txt", "r", encoding="utf-8")

buwei_list = list()
tag_names_list = list()
for item in buwei_data.readlines():
    buwei_list.append(item.strip())

print(buwei_list)

db_zhengxing_eagle = pymysql.connect(host="172.16.30.143", port=3306, user="work",
                                     password="BJQaT9VzDcuPBqkd",
                                     db="zhengxing",
                                     charset='utf8',
                                     cursorclass=pymysql.cursors.DictCursor)

# db_zhengxing_eagle = pymysql.connect(host="bj-cdb-6slgqwlc.sql.tencentcdb.com", port=62120, user="work",
#                                      password="Gengmei1",
#                                      db="zhengxing_test",
#                                      charset='utf8',
#                                      cursorclass=pymysql.cursors.DictCursor)

zhengxing_cursor = db_zhengxing_eagle.cursor()

sql = 'select name from api_tag '

zhengxing_cursor.execute("set names 'UTF8'")
zhengxing_cursor.execute(sql)
data = zhengxing_cursor.fetchall()

for name in list(data):
    tag_names_list.append(name.get("name", None))

print(tag_names_list)
# tag_names_list = ["鼻综合", "丰面颊", "玻尿酸丰太阳穴"]
cut_result_data1 = []
cut_result_data2 = []
for tag_name in tag_names_list:
    flot = False

    for bwword in buwei_list:
        if bwword in tag_name:
            tag_list = []
            tag_list.append(tag_name)
            flot = True
            ss = tag_name.split(bwword)
            tag_list.append(bwword)
            ss.append(bwword)
            if isinstance(ss, list):
                if '' in ss:
                    ss.remove('')
            tag_list.append(ss)
            cut_result_data1.append(tag_list)
    if flot == False:
        cut_result_data2.append(tag_name)

data = open("cut_result_data.txt", "w", encoding="utf-8")

for cut_result in cut_result_data1:
    data.write(str(cut_result))
    data.write("\n")

for cut_result in cut_result_data2:
    data.write(str(cut_result))
    data.write("\n")
