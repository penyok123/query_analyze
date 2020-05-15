# coding=utf-8
import pymysql
from elasticsearch import Elasticsearch
import smtplib, xlwt, logging, traceback, datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.utils import formataddr

es = Elasticsearch([
    {
        'host': '172.16.31.17',
        'port': 9200,
    }, {
        'host': '172.16.31.11',
        'port': 9200,
    }])


def send_email_tome():
    try:
        date = datetime.datetime.now().date() - datetime.timedelta(days=1)
        fromaddr = 'lixiaofang@igengmei.com'
        password = 'hTx9kAikArsSNsDr'
        toaddrs = "lixiaofang@igengmei.com"
        toaddrs1 = "duanyingrong@igengmei.com"
        toaddrs2 = "dengguangyu@igengmei.com"
        toaddrs3 = "wangxin@igengmei.com"
        toaddrs4 = "hezijun@igengmei.com"
        toaddrs5 = "malinxi@igengmei.com"

        content = 'hi  all:附件为' + str(date) + '的搜索词数据统计结果以及近一周的数据统计结果，请查收！'
        textApart = MIMEText(content)

        zipFile = str(date) + ".xls"
        # zipFile = '昨日数据统计结果.xls'
        zipApart = MIMEApplication(open(zipFile, 'rb').read())
        zipApart.add_header('Content-Disposition', 'attachment', filename=zipFile)

        zipFile_week = '近一周数据统计结果.xls'
        zipApart_week = MIMEApplication(open(zipFile_week, 'rb').read())
        zipApart_week.add_header('Content-Disposition', 'attachment', filename=zipFile_week)

        m = MIMEMultipart()
        m.attach(textApart)
        m.attach(zipApart_week)
        m.attach(zipApart)
        m['From'] = formataddr(["李小芳", fromaddr])
        m["To"] = formataddr(["李小芳", toaddrs])
        m["To"] = formataddr(["段英荣", toaddrs1])
        m["To"] = formataddr(["邓光宇", toaddrs2])
        m["To"] = formataddr(["王昕", toaddrs3])
        m["To"] = formataddr(["赫梓君", toaddrs4])
        m["To"] = formataddr(["马霖唏", toaddrs5])

        m['Subject'] = '每日搜索词结果统计'
        try:
            server = smtplib.SMTP_SSL('smtp.exmail.qq.com', 465)
            server.login(fromaddr, password)
            server.sendmail(fromaddr, [toaddrs3, toaddrs2, toaddrs5, toaddrs4, toaddrs, toaddrs1], m.as_string())
            print('success')
            server.quit()
        except smtplib.SMTPException as e:
            print('error', e)
    except Exception:
        logging.error("catch exception,main:%s" % traceback.format_exc())


def get_es_word(word):
    ###answer
    results = es.search(
        index='gm-dbmw-answer-read',
        doc_type='answer',
        timeout='10s',
        size=0,
        body={
            "query": {
                "bool": {
                    "minimum_should_match": 1,
                    "should": [{"match_phrase": {"title": {"query": word, "analyzer": "gm_default_index"}}},
                               {"match_phrase": {"desc": {"query": word, "analyzer": "gm_default_index"}}},
                               {"match_phrase": {"answer": {"query": word, "analyzer": "gm_default_index"}}}],
                    "must": [{"term": {"is_online": True}}]
                }
            },
        }
    )
    answer_content_num = results["hits"]["total"]

    # tractate
    results = es.search(
        index='gm-dbmw-tractate-read',
        doc_type='tractate',
        timeout='10s',
        size=0,
        body={
            "query": {
                "bool": {
                    "minimum_should_match": 1,
                    "should": [{"match_phrase": {"content": {"query": word, "analyzer": "gm_default_index"}}}, {
                        "match_phrase": {"tractate_tag_name": {"query": word, "analyzer": "gm_default_index"}}}, {
                                   "match_phrase": {"tractate_tag_name_content": {"query": word,
                                                                                  "analyzer": "gm_default_index"}}}],
                    "must": [{"term": {"is_online": True}}]
                }
            },
        }
    )
    tractate_content_num = results["hits"]["total"]

    ###diary
    results = es.search(
        index='gm-dbmw-diary-read',
        doc_type='diary',
        timeout='10s',
        size=0,
        body={
            "query": {
                "bool": {
                    "minimum_should_match": 1,
                    "should": [{"match_phrase": {"tags": {"query": word, "analyzer": "gm_default_index"}}},
                               {"match_phrase": {"answer": {"query": word, "analyzer": "gm_default_index"}}},
                               {"match_phrase": {"service.name": {"query": word, "analyzer": "gm_default_index"}}}],
                    "must": [{"term": {"is_online": True}}, {"range": {"content_level": {"gte": "3"}}}]
                }
            },
        }
    )
    diary_content_num = results["hits"]["total"]

    return answer_content_num, tractate_content_num, diary_content_num


def get_es_syno_word(word):
    body = {
        'text': word,
        'analyzer': "gm_default_index"
    }

    res = es.indices.analyze(index='gm-dbmw-diary', body=body)

    # 全词匹配term列表
    complete_matching_term_set = set()

    for item in res["tokens"]:
        token = item['token']
        start_offset = item['start_offset']
        end_offset = item['end_offset']
        type = item['type']
        # SYNONYM
        if start_offset == 0 and end_offset == len(word) and type == "SYNONYM":
            complete_matching_term_set.add(token)

    return list(complete_matching_term_set)


class WritrExcel():

    def set_style(self, name, height, bold=False):
        style = xlwt.XFStyle()  # 初始化样式
        font = xlwt.Font()  # 为样式创建字体
        font.name = name
        font.bold = bold
        font.color_index = 4
        font.height = height
        style.font = font
        return style

    # 写入Excel
    def write_excel(self, path, rows):
        # 创建工作簿
        workbook = xlwt.Workbook(encoding='utf-8')
        # 创建sheet
        data_sheet = workbook.add_sheet('Sheet1')
        # 将样式定义在循环之外
        default = self.set_style('Times New Roman', 220, True)
        j = k = 0
        # 循环读取每一行数据并写入Excel
        for row in rows[:65530]:
            for i in range(len(row)):
                try:
                    # 写入
                    data_sheet.write((j + k), i, row[i], default)
                except:
                    print(i)
                    raise
                # data_sheet.write(1, i, row1[i], self.set_style('Times New Roman', 220, True))
            k = k + 1
        workbook.save(path)
        print("写入文件成功，共" + str(k) + "行数据")


if __name__ == "__main__":
    tag_names_list = []
    tag_names_list_week = []
    all_data_day = []
    all_data_week = []
    db_zhengxing_eagle = pymysql.connect(host="172.16.30.136", port=3306, user="doris",
                                         password="o5gbA27hXHHm",
                                         db="doris_prod",
                                         charset='utf8',
                                         cursorclass=pymysql.cursors.DictCursor)
    zhengxing_cursor = db_zhengxing_eagle.cursor()
    date = datetime.datetime.now().date() - datetime.timedelta(days=1)
    sql = 'select keywords,sum(sorted) as nums,uv  from api_search_words where is_delete = 0 and create_time = "' + str(
        date) + '" group by keywords  order by  nums  desc'

    zhengxing_cursor.execute("set names 'UTF8'")
    zhengxing_cursor.execute(sql)
    data = zhengxing_cursor.fetchall()

    tup_title = ("关键词", "搜索次数", "uv", "日记数量", "回答数量", "帖子数量", "同义词日记数量", "同义词回答数量", "同义词帖子数量")
    for name in list(data):
        word = name.get("keywords", None)
        num = name.get("nums", 0)
        uv = name.get("uv", 0)

        answer_content_num, tractate_content_num, diary_content_num = get_es_word(word)
        complete_matching_term_set = get_es_syno_word(word=word)
        sy_answer_content_num = 0
        sy_tractate_content_num = 0
        sy_diary_content_num = 0
        for item in complete_matching_term_set:
            answer_num, tractate_num, diary_num = get_es_word(item)
            sy_diary_content_num += diary_num
            sy_answer_content_num += answer_num
            sy_tractate_content_num += tractate_num

        tag_names_list.append(
            [word, num, uv, diary_content_num, answer_content_num, tractate_content_num,
             sy_diary_content_num + diary_content_num,
             sy_answer_content_num + answer_content_num, sy_tractate_content_num + tractate_content_num])

    all_data_day.append(tup_title)
    for item in tag_names_list:
        all_data_day.append(tuple(item))

    path = str(date) + ".xls"
    WritrExcel().write_excel(path, tuple(all_data_day))

    date = datetime.datetime.now().date() - datetime.timedelta(days=7)
    sql = 'select keywords,sum(sorted) as nums,sum(uv) as uvs  from api_search_words where is_delete = 0 and create_time >= "' + str(
        date) + '" group by keywords  order by  nums  desc'

    zhengxing_cursor.execute("set names 'UTF8'")
    zhengxing_cursor.execute(sql)
    data = zhengxing_cursor.fetchall()

    tup_title = ("关键词", "搜索次数", "uv", "日记数量", "回答数量", "帖子数量", "同义词日记数量", "同义词回答数量", "同义词帖子数量")
    for name in list(data):
        word = name.get("keywords", None)
        sorteds = name.get("nums", 0)
        uv = name.get("uvs", 0)

        answer_content_num, tractate_content_num, diary_content_num = get_es_word(word)
        complete_matching_term_set = get_es_syno_word(word=word)
        sy_answer_content_num = 0
        sy_tractate_content_num = 0
        sy_diary_content_num = 0
        for item in complete_matching_term_set:
            answer_num, tractate_num, diary_num = get_es_word(item)
            sy_diary_content_num += diary_num
            sy_answer_content_num += answer_num
            sy_tractate_content_num += tractate_num

        tag_names_list_week.append(
            [word, sorteds, uv, diary_content_num, answer_content_num, tractate_content_num,
             sy_diary_content_num + diary_content_num,
             sy_answer_content_num + answer_content_num, sy_tractate_content_num + tractate_content_num])

    all_data_week.append(tup_title)
    for item in tag_names_list_week:
        all_data_week.append(tuple(item))

    path = "近一周数据统计结果.xls"
    WritrExcel().write_excel(path, tuple(all_data_week))

    send_email_tome()
