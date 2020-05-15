import re
from simhash import Simhash, SimhashIndex
from simhash import Simhash
import re
import pymysql
import time


def get_features(s):
    width = 3
    s = s.lower()
    s = re.sub(r'[^\w]+', '', s)
    return [s[i:i + width] for i in range(max(len(s) - width + 1, 1))]


if __name__ == '__main__':
    begin = time.time()
    all_similar_set = list()
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
    sql = 'select id,content from api_tractate limit 100'
    mimas_cursor.execute(sql)
    data = list(mimas_cursor.fetchall())

    file = open("tractate.txt", "w", encoding="utf-8")
    for one in range(0, len(data)):
        begin = time.time()
        text1 = data[one].get("content", None)
        one_id = data[one].get("id", None)
        all_similar_data[one_id] = text1

    objs = [(str(k), Simhash(get_features(v))) for k, v in all_similar_data.items()]
    index = SimhashIndex(objs, k=6)
    print(index.bucket_size())

    for key, value in all_similar_data.items():
        s1 = Simhash(get_features(value))
        simi_list = index.get_near_dups(s1)
        simi_list.sort(key=lambda x: int(x), reverse=False)

        if len(simi_list) > 1 and simi_list not in all_similar_set:
            all_similar_set.append(simi_list)

    for item in all_similar_set:
        file.write(str(item))
        file.write("\n")
    print("100条数据计算的时间:%f" % (time.time() - begin))
