# -*- coding: utf-8 -*-
from __future__ import division
from __future__ import print_function
import pymysql
import re
from elasticsearch import Elasticsearch

es = Elasticsearch([
    {
        'host': 'es.paas-test.env',
        'port': 80,
    }, {
        'host': 'es.paas-test.env',
        'port': 80,
    }])


class AnalyzeContent(object):

    def __init__(self):
        pass

    def get_highlight_query(self, fields=[], query=''):
        field_highlight = {
            'fields': {k: {"highlight_query": {
                "bool": {
                    "must": {
                        "match": {
                            k: {
                                "query": query
                            }
                        }
                    },
                    "minimum_should_match": 0
                }
            }} for k in fields},
            'fragment_size': 10000,
            'pre_tags': ['<%s>' % 'ems'],
            'post_tags': ['</%s>' % 'ems'],
            "require_field_match": False,

        }
        return field_highlight

    def get_mysql_data(self):
        card_id = (20893462, 20894306, 20894517)

        db_miams_eagle = pymysql.connect(host="bj-cdb-6slgqwlc.sql.tencentcdb.com", port=62120, user="work",
                                         password="Gengmei1",
                                         db="mimas_test",
                                         cursorclass=pymysql.cursors.DictCursor, charset="utf8")

        mimas_cursor = db_miams_eagle.cursor()
        sql = "select id,content from api_tractate where id  in (20893628) "
        mimas_cursor.execute(sql)
        data = mimas_cursor.fetchall()

        return data

    def cut_sent(self, para):
        # for item in data:
        #     content = item.get("content", "")
        #     pattern = r',|\.|/|;|\'|`|\[|\]|<|>|\?|:|"|\{|\}|\~|!|@|#|\$|%|\^|&|\(|\)|-|=|\_|\+|，|。|、|；|‘|’|【|】|·|！| |…|（|）'
        #     result_list = re.split(pattern, content)
        #     print(result_list)
        # for item in data:
        #     content = item.get("content", "")
        #     pattern = r'\.|/|;|\'|`|\[|\]|<|>|\?|:|"|\{|\}|\~|!|@|#|\$|%|\^|&|\(|\)|-|=|\_|\+|。|、|；|‘|’|【|】|·|！| |…|（|）'
        #     result_list = re.split(pattern, content)
        #     print(result_list)

        para = re.sub('([；。！？\?])([^”’])', r"\1\n\2", para)  # 单字符断句符
        para = re.sub('(\.{6})([^”’])', r"\1\n\2", para)  # 英文省略号
        para = re.sub('(\…{2})([^”’])', r"\1\n\2", para)  # 中文省略号
        para = re.sub('([；。！？\?][”’])([^，。！？\?])', r'\1\n\2', para)
        # 如果双引号前有终止符，那么双引号才是句子的终点，把分句符\n放到双引号后，注意前面的几句都小心保留了双引号
        para = para.rstrip()  # 段尾如果有多余的\n就去掉它
        para = para.replace("\r", "")
        para = para.replace("?", "")
        # 很多规则中会考虑分号;，但是这里我把它忽略不计，破折号、英文双引号等同样忽略，需要的再做些简单调整即可。
        return para.split("\n")

    def get_es_highlight(self, query=None, id=0):
        tractate_hl = None
        q = {
            "query": {
                "bool": {
                    "must": {
                        "term": {
                            "id": id
                        }
                    }
                }
            }
        }
        q['highlight'] = self.get_highlight_query(query=query, fields=['content'])
        results = es.search(
            index='gm_test-tractate',
            doc_type='tractate',
            timeout='10s',
            size=1,
            body=q
        )

        if results['hits']['hits']:
            tractate_hl = results["hits"]['hits'][0]['highlight']

        return tractate_hl


if __name__ == '__main__':

    all_content = {}
    anacon = AnalyzeContent()
    data = anacon.get_mysql_data()  ##获取帖子的内容
    for item in data:
        content_list = []
        cid = item.get("id", 0)
        content = item.get("content", "")
        for con in anacon.cut_sent(content):  ##切分文章成一句一句的内容
            r = '[’!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~]+'
            if con not in ['\r', '?', '?\r', '❤️❤️\r', '?\r', '??', '', '.', ',']:
                print("切分后的语句-------------------", con)
                content_list.append(con)
        print("------------------------------------------------------------------------")
        print(content)
        print("------------------------------------------------------------------------")

        highlight = anacon.get_es_highlight(query="少女针", id=cid)
        content = highlight.get("content", "")[0]
        for con in content.split("', '"):
            if "<ems>" in con:
                print("有高亮的语句-------------------",con)
