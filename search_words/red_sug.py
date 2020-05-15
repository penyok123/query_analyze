# coding=utf-8
from elasticsearch import Elasticsearch
import xlrd
from elasticsearch import Elasticsearch
import logging, xlwt, traceback, datetime
import smtplib, traceback
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.utils import formataddr

es = Elasticsearch([
    {
        'host': 'es6.paas-test.env',
        'port': 80,
    }, {
        'host': 'es6.paas-test.env',
        'port': 80,
    }])


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


def get_sug(word):
    try:
        q = {
            "suggest": {
                "tips-suggest": {
                    "prefix": word,
                    "completion": {
                        "field": "suggest",
                        "size": 50,
                        "contexts": {
                            "is_online": [True]
                        },
                        "fuzzy": {
                            "fuzziness": 0
                        }
                    }
                }
            },
            "_source": {
                "includes": ["id", "ori_name", "offline_score", "is_online", "type_flag", "results_num"]
            }
        }
        res = es.search(index='gm_test-suggest-read',
                        doc_type='_doc',
                        size=10,
                        body=q,
                        from_=0)

        total = len(res['suggest']['tips-suggest'][0]['options'])
        return total
    except:
        print(traceback.format_exc())


def send_email_tome():
    try:
        date = datetime.datetime.now().date() - datetime.timedelta(days=1)
        fromaddr = 'lixiaofang@igengmei.com'
        password = '8YEfruErRAe27idA'
        toaddrs = "lixiaofang@igengmei.com"

        content = 'hi  all:'
        textApart = MIMEText(content)

        zipFile_week = 'sug_word.xls'
        zipApart_week = MIMEApplication(open(zipFile_week, 'rb').read())
        zipApart_week.add_header('Content-Disposition', 'attachment', filename=zipFile_week)

        m = MIMEMultipart()
        m.attach(textApart)
        m.attach(zipApart_week)

        m['From'] = formataddr(["李小芳", fromaddr])
        m["To"] = formataddr(["李小芳", toaddrs])
        m['Subject'] = 'sug词'
        try:
            server = smtplib.SMTP_SSL('smtp.exmail.qq.com', 465)
            server.login(fromaddr, password)
            server.sendmail(fromaddr, [toaddrs], m.as_string())
            print('success')
            server.quit()
        except smtplib.SMTPException as e:
            print('error', e)
    except Exception:
        logging.error("catch exception,main:%s" % traceback.format_exc())


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
    try:
        data = xlrd.open_workbook("17-24.xlsx")
        data1 = xlrd.open_workbook("24-31.xlsx")
        table1 = data.sheets()[0]
        table2 = data1.sheets()[0]

        sug_data1 = []
        sug_data2 = []
        sug_query1 = []
        sug_nquer1_query2 = []

        for item in range(0, table1.nrows):
            sug_data1.append(table1.row_values(item))
            sug_query1.append(table1.row_values(item)[0])

        for item in range(0, table2.nrows):
            sug_data2.append(table2.row_values(item))

        for item in sug_data2:
            if item[0] not in sug_query1:
                total = get_sug(word=item[0])
                item.append(total)
                sug_nquer1_query2.append(tuple(item))

        data = sorted(sug_nquer1_query2, key=lambda x: x[2], reverse=False)
        tup_title = ("关键词", "搜索次数", "sug的结果")
        sug_nquer1_query2.insert(0, tup_title)

        path = "sug_word.xls"
        WritrExcel().write_excel(path, tuple(data))

    except:
        pass
