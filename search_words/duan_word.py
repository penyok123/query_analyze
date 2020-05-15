# -*- coding: UTF-8 -*-

from elasticsearch import Elasticsearch
import jieba
import sys
import pymysql
from collections import defaultdict
from time import time

zhengxing_conn = pymysql.connect(
    host="172.16.30.141",
    user="work",
    password="BJQaT9VzDcuPBqkd",
    database="zhengxing",
    charset="utf8")
zhengxing_cursor = zhengxing_conn.cursor()


class Node(object):

    def __init__(self, value, children_value=None):
        self._value = value
        self._children = defaultdict()
        self._end_flag = ''

    @property
    def children(self):
        return self._children

    @property
    def value(self):
        return self._value

    @property
    def end_flag(self):
        return self._end_flag

    def set_end_flag(self, value):
        self._end_flag = value

    def set_children(self, children):
        self._children = children

    def __str__(self):
        return self._value


class TrieTree(object):

    def __init__(self, entity_dict=None):
        """
        Args:
            entity_dict: dict
        """
        self._root = Node('root')
        if entity_dict:
            self.update_tree_batch(entity_dict)

    def update_tree_batch(self, entity_dict):
        """
        Args:
            entity_dict: dict
        """
        for entity in entity_dict:
            entity_type = entity_dict[entity]
            self.update_tree(entity, entity_type)

    def update_tree(self, entity, entity_type):
        """
        Args:
            entity: str
            entity_type: str
        """
        name_len = len(entity)
        node_pre = self.root
        for i in range(name_len):
            c = entity[i]
            if c not in node_pre.children:
                node = Node(c)
                node_pre.children[c] = node
                node_pre = node
                if i == name_len - 1:
                    node.set_end_flag(entity_type)
            else:
                if i == name_len - 1:
                    node_pre.children[c].set_end_flag(entity_type)
                node_pre = node_pre.children[c]

    @property
    def root(self):
        return self._root

    def show(self, node, level=0):
        """
        输出tree
        """
        if not node:
            return
        if level == 0:
            print(node)
        else:
            print('└%s%s %s' % ('─' * level * 2, node, node.end_flag))
        for node_value in node.children:
            end_flag = node.children[node_value].end_flag
            print('└%s%s %s' % ('─' * (level + 1) * 2, node_value, end_flag))
            if not node.children[node_value]:
                continue
            for child in node.children[node_value].children:
                self.show(node.children[node_value].children[child], level + 2)


def match_sentence(sentence, root, start):
    """
    Args:
        sentence: str
        root: Node, root node
        start: int, 句子的起始位置
    Return:
        end, entity_len, entity_type
    """
    current_node = root
    index, entity_type = -1, ''
    for i in range(start, len(sentence)):
        if sentence[i] not in current_node.children:
            if index == -1:
                return start + 1, 0, ''
            else:
                return index + 1, index + 1 - start, entity_type
        current_node = current_node.children[sentence[i]]
        if current_node.end_flag:
            index = i
            entity_type = current_node.end_flag
    if index != -1:
        return index + 1, index + 1 - start, entity_type
    return start + 1, 0, ''


def get_city_name_list():
    city_name_set = set()
    city_name_query_sql = """
        select name from api_city where is_online=1;
    """
    zhengxing_cursor.execute(city_name_query_sql)
    sql_results = zhengxing_cursor.fetchall()
    for item in sql_results:
        city_name_set.add(item[0].strip())

    return city_name_set


def get_hospital_name_list():
    hospital_name_set = set()
    hospital_name_query_sql = """
        select name from api_hospital where is_online=1;
    """
    zhengxing_cursor.execute(hospital_name_query_sql)
    sql_results = zhengxing_cursor.fetchall()
    for item in sql_results:
        hospital_name_set.add(item[0].strip())

    return hospital_name_set


def get_doctor_name_list():
    doctor_name_set = set()
    doctor_name_query_sql = """
        select name from api_doctor where is_online=1;
    """
    zhengxing_cursor.execute(doctor_name_query_sql)
    sql_results = zhengxing_cursor.fetchall()
    for item in sql_results:
        doctor_name_set.add(item[0].strip())

    return doctor_name_set


def set_query_word(line, offi_query_word_dict, tree):
    line = line.strip()
    line = line.strip("\n")
    line = line.strip("\t")
    split_list = line.split("\t")
    if len(split_list) == 2:
        word = split_list[0]
        word = word.strip()
        word = word.strip("\t")
        word = word.strip(" ")

        counts = split_list[1]
        counts = counts.strip()
        counts = counts.strip("\t")
        counts = counts.strip(" ")

        bad_word = False
        if word in offi_query_word_dict:
            bad_word = True
            return offi_query_word_dict

        end, word_len = 0, len(word)
        while end < word_len:
            end, entity_len, entity_type = match_sentence(word, tree.root, end)
            if entity_type in ["city", "doctor", "hospital"]:
                bad_word = True
                break
        if len(word) > 30 or int(counts) < 7:
            bad_word = True
        if word.find("￥") >= 0 or word.find("！") >= 0 or word.find("!") >= 0:
            bad_word = True

        for save_word in offi_query_word_dict:
            if save_word.find(word) >= 0:
                bad_word = True
                break

        if not bad_word:
            offi_query_word_dict[word] = counts

    return offi_query_word_dict


if __name__ == "__main__":
    trietree_word_dict = dict()
    city_name_set = get_city_name_list()
    for city_name in city_name_set:
        trietree_word_dict[city_name] = "city"

    doctor_name_set = get_doctor_name_list()
    for doctor_name in doctor_name_set:
        trietree_word_dict[doctor_name] = "doctor"

    hospital_name_suffix_list = ["医疗美容诊所", "诊所", "医院", "整形外科", "门诊部", "医疗美容", "分院", "门诊", "急诊", "总医院"]

    hospital_name_set = get_hospital_name_list()
    for hospital_name in hospital_name_set:
        if len(hospital_name) > 1:
            trietree_word_dict[hospital_name] = "hospital"

        for suffix_name in hospital_name_suffix_list:
            cut_hospital_name = hospital_name.strip(suffix_name)
            if cut_hospital_name != hospital_name and len(cut_hospital_name) > 1:
                trietree_word_dict[cut_hospital_name] = "hospital"

    tree = TrieTree(trietree_word_dict)

    offi_query_word_dict = dict()
    ori_guangyu_query_word_fd = open("/data/log/spider/test_service/sort_search_word_from_guangyu.txt", "r")
    ori_query_word_fd = open("/data/log/word2vec/query_word_from_20190101_20200115.txt", "r")
    offi_query_word_fd = open("./offi_query_word_from_20190101_20200115_v2.txt", "w")

    for line in ori_guangyu_query_word_fd.readlines():
        offi_query_word_dict = set_query_word(line, offi_query_word_dict, tree)
    for line in ori_query_word_fd.readlines():
        offi_query_word_dict = set_query_word(line, offi_query_word_dict, tree)

    doris_conn = pymysql.connect(
        host="172.16.30.136",
        user="doris",
        password="o5gbA27hXHHm",
        database="doris_prod",
        charset="utf8")
    doris_cursor = doris_conn.cursor()

    for word in offi_query_word_dict:
        counts = offi_query_word_dict[word]

        offi_query_word_fd.write(word + "\t" + str(counts) + "\n")
        print("query_word:%s,query_num:%d" % (word, int(counts)))
        es = Elasticsearch([
            {
                'host': '172.16.31.17',
                'port': 9200,
            }, {
                'host': '172.16.31.11',
                'port': 9200,
            }])
        results = es.search(
            index='gm-dbmw-answer-read',
            doc_type='answer',
            timeout='10s',
            size=0,
            body={
                "query": {
                    "bool": {
                        "minimum_should_match": 1,
                        "should": [{"multi_match": {
                            "query": word,
                            "type": "best_fields",
                            "operator": "or",
                            "fields": ["title", "desc", "answer", "tag_name"],
                            "boost": 3,
                            "analyzer": "gm_default_index"
                        }
                        }],
                        "must": [{"term": {"is_online": True}}]
                    }
                },
            }
        )
        answer_content_num = results["hits"]["total"]

        results = es.search(
            index='gm-dbmw-tractate-read',
            doc_type='tractate',
            timeout='10s',
            size=0,
            body={
                "query": {
                    "bool": {
                        "minimum_should_match": 1,
                        "should": [
                            {"multi_match": {
                                "query": word,
                                "type": "best_fields",
                                "operator": "or",
                                "fields": ["content", "tractate_tag_name", "tractate_tag_name_content",
                                           "content_keyword", "fresh_tractate_tag_name"],
                                "boost": 3,
                                "analyzer": "gm_default_index"}
                            }
                        ],
                        "must": [{"term": {"is_online": True}}]
                    }
                },
            }
        )
        tractate_content_num = results["hits"]["total"]

        results = es.search(
            index='gm-dbmw-diary-read',
            doc_type='diary',
            timeout='10s',
            size=0,
            body={
                "query": {
                    "bool": {
                        "minimum_should_match": 1,
                        "should": [{"multi_match": {
                            "query": word,
                            "type": "best_fields",
                            "operator": "or",
                            "fields": ["tags", "answer", "service.name", "title", "fresh_tags"],
                            "boost": 3,
                            "analyzer": "gm_default_index"}
                        }],
                        "must": [{"term": {"is_online": True}}, {"range": {"content_level": {"gte": "3"}}}]
                    }
                },
            }
        )
        diary_content_num = results["hits"]["total"]

        insert_sql = "insert into strategy_history_query_words(keyword,search_num,answer_num,tractate_num,diary_num) values(%s,%s,%s,%s,%s)"
        data = (str(word), int(counts), int(answer_content_num), int(tractate_content_num), int(diary_content_num))
        doris_cursor.execute(insert_sql, data)
        doris_conn.commit()

    ori_guangyu_query_word_fd.close()
    ori_query_word_fd.close()
    offi_query_word_fd.close()
