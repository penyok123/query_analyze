# -*- coding:utf-8 -*-
from simhash import Simhash
import re
import pymysql
import time


def filter_html(html):
    """
    :param html: html
    :return: 返回去掉html的纯净文本
    """
    dr = re.compile(r'<[^>]+>', re.S)
    dd = dr.sub('', html).strip()
    return dd


# 求两篇文章相似度
def simhash_similarity(text1, text2):
    """
    :param tex1: 文本1
    :param text2: 文本2
    :return: 返回两篇文章的相似度
    """
    begin = time.time()
    aa_simhash = Simhash(text1)
    bb_simhash = Simhash(text2)
    # print(aa_simhash.value)
    # print(bb_simhash.value)

    max_hashbit = max(len(bin(aa_simhash.value)), (len(bin(bb_simhash.value))))
    # 汉明距离
    distince = aa_simhash.distance(bb_simhash)

    similar = 1 - distince / max_hashbit

    print("两两计算的时间:%f" % (time.time() - begin))
    return similar


if __name__ == '__main__':
    begin = time.time()

    all_similar_data = {}
    # db_miams_eagle = pymysql.connect(host="172.16.30.138", port=3306, user="mimas",
    #                                  password="GJL3UJe1Ck9ggL6aKnZCq4cRvM",
    #                                  db="mimas_prod",
    #                                  cursorclass=pymysql.cursors.DictCursor, charset='utf8')
    db_miams_eagle = pymysql.connect(host="bj-cdb-6slgqwlc.sql.tencentcdb.com", port=62120, user="work",
                                     password="Gengmei1",
                                     db="mimas_test",
                                     cursorclass=pymysql.cursors.DictCursor, charset='utf8')

    mimas_cursor = db_miams_eagle.cursor()
    sql = 'select id,content from api_tractate limit 10000'
    mimas_cursor.execute(sql)
    data = list(mimas_cursor.fetchall())

    file = open("tractate.txt", "w", encoding="utf-8")
    for one in range(0, len(data)):
        begin = time.time()
        text1 = data[one].get("content", None)
        one_id = data[one].get("id", None)

        for two in range(one + 1, len(data)):
            text2 = data[two].get("content", None)
            two_id = data[two].get("id", None)
            similar = simhash_similarity(text1, text2)
            print("similar:%s" % similar)
            # print("text1_id:%s,text1_content:%s,text2_id:%s,text1_content:%s,similar:%s" % (
            #     one_id, text1, two_id, text2, similar))

            if similar > 0.9 and one_id != two_id:

                if one_id in all_similar_data.keys():
                    all_similar_data[one_id].append(two_id)
                else:
                    all_similar_data[one_id] = [two_id]

        simi_ids = all_similar_data.get(one_id, None)
        if simi_ids:
            file.write(str(one_id))
            file.write(":")
            file.write(str(simi_ids))
            file.write("\n")
    print("100条数据计算的时间:%f" % (time.time() - begin))
