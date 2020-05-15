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
        "host": "172.16.44.125",
        "port": 9201
    },
    {
        "host": "172.16.44.106",
        "port": 9201
    },
    {
        "host": "172.16.44.87",
        "port": 9201
    }
])


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
        sug_data1 = []
        sug_data2 = []
        sug_query1 = []
        sug_nquer1_query2 = []

        file = open("sug.txt", "r", encoding="utf-8")
        for items in file.readlines():
            item = items.strip().split()
            print(item[0])
            total = get_sug(word=item[0])
            all = (item[0], item[1], item[2])
            sug_nquer1_query2.append(tuple(all))

        # print(sug_nquer1_query2)
        data = sorted(sug_nquer1_query2, key=lambda x: x[2], reverse=False)
        tup_title = ("关键词", "搜索次数", "sug的结果")
        sug_nquer1_query2.insert(0, tup_title)

        path = "sug_word.xls"
        WritrExcel().write_excel(path, tuple(data))

    except:
        pass
