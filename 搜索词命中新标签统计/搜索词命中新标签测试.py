# coding=utf-8
import re, jieba
import xlwt, datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.utils import formataddr
from elasticsearch import Elasticsearch
import jieba
import jieba.analyse
import pymysql
from collections import defaultdict
import logging
import traceback
import redis
import json

es = Elasticsearch([
    {
        'host': 'es.paas-test.env',
        'port': 80,
    }]
)
HIGHLIGHT_TAG = 'ems'

REDIS_URL = "redis://redis.paas-test.env:6379/0"
redis_client = redis.StrictRedis.from_url(REDIS_URL)

logger = logging.getLogger(__name__)


def get_analy_tag(word):
    test_word = str( """不知、不觉·间我~|~已经忘了爱❤。""")
    # test_word = unicode(test_word, "utf-8")
    test_word = test_word.encode("utf-8")
    if len(WordAnalysis.total_tagv3_dict) == 0:
        WordAnalysis.init_tree_data_dict()
    print("9999999999999", WordAnalysis.init_tree_data_dict())
    tree = TrieTree(WordAnalysis.unicode_tagtv3_dict)

    word_attr_info_dict = WordAnalysis.analysis_word(test_word, tree)

    return word_attr_info_dict


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
    multi_match_list = []
    current_node = root
    index, entity_type = -1, ''
    for i in range(start, len(sentence)):
        encode_term = sentence[i]
        if encode_term not in current_node.children:
            if index == -1:
                return [(start + 1, 0, '')]
            else:
                return multi_match_list
        current_node = current_node.children[encode_term]
        if current_node.end_flag:
            index = i
            entity_type = current_node.end_flag
            multi_match_list.append((index + 1, index + 1 - start, entity_type))
    if index != -1:
        return multi_match_list
    return [(start + 1, 0, '')]


class WordAnalysis(object):
    host = "bj-cdb-6slgqwlc.sql.tencentcdb.com"
    user = "work"
    password = "Gengmei1"
    database = "zhengxing_test"
    port = 62120
    cursorclass = pymysql.cursors.DictCursor
    charset = 'utf8'
    total_tagv3_dict = dict()
    unicode_tagtv3_dict = dict()
    extra_first_positions_dict = dict()
    extra_second_positions_dict = dict()

    @classmethod
    def __init__(cls):
        if len(cls.total_tagv3_dict) == 0:
            cls.init_tree_data_dict()

    @classmethod
    def init_tree_data_dict(cls):
        try:
            if len(cls.total_tagv3_dict) > 0:
                return cls.total_tagv3_dict

            zhengxing_conn = pymysql.connect(
                host=cls.host,
                user=cls.user,
                password=cls.password,
                database=cls.database,
                port=cls.port,
                charset="utf8")

            zhengxing_cursor = zhengxing_conn.cursor()

            old_tag_sql = """
            	select name from api_tag where is_online=true and tag_type=3;
            """

            # 二级诉求
            second_demands_sql = """
                    select name from api_tag_attr where is_online=1 and aggregate_type=8;
            """
            # 二级方式
            second_solutions_sql = """
                    select name from api_tag_attr where is_online=1 and aggregate_type=2;
            """
            # 二级部位
            second_positions_sql = """
                    select name from api_tag_attr where is_online=1 and aggregate_type=3;
            """
            # 一级诉求
            first_demands_sql = """
                    select name from api_tag_attr where is_online=1 and aggregate_type=7;
            """
            # 一级方式
            first_solutions_sql = """
                    select name from api_tag_attr where is_online=1 and aggregate_type=6;
            """
            # 一级部位
            first_positions_sql = """
                    select name from api_tag_attr where is_online=1 and aggregate_type=10;
            """
            # 新项目标签
            tag_v3_project_sql = """
                    select name from api_tag_3_0 where is_online=1 and tag_type=1;
            """
            # 新标签同义词
            tag_v3_synonym_sql = """
                    select name from api_tag_aggregate where name!="";
            """

            second_demands_list = list()
            zhengxing_cursor.execute(second_demands_sql)
            sql_tag_results = zhengxing_cursor.fetchall()
            for item in sql_tag_results:
                encode_item = item[0].encode("utf-8")
                second_demands_list.append(encode_item)
                jieba.add_word(encode_item)
                cls.total_tagv3_dict[encode_item] = "second_demands"
                cls.unicode_tagtv3_dict[encode_item] = "second_demands"
            second_demands_list = set(second_demands_list)

            second_solutions_list = list()
            zhengxing_cursor.execute(second_solutions_sql)
            sql_tag_results = zhengxing_cursor.fetchall()
            for item in sql_tag_results:
                encode_item = item[0].encode("utf-8")
                second_solutions_list.append(encode_item)
                jieba.add_word(encode_item)
                cls.total_tagv3_dict[encode_item] = "second_solutions"
                cls.unicode_tagtv3_dict[encode_item] = "second_solutions"
            second_solutions_list = set(second_solutions_list)

            second_positions_list = list()
            zhengxing_cursor.execute(second_positions_sql)
            sql_tag_results = zhengxing_cursor.fetchall()
            for item in sql_tag_results:
                encode_item = item[0]
                second_positions_list.append(encode_item)
                jieba.add_word(encode_item)
                cls.total_tagv3_dict[encode_item] = "second_positions"
                cls.unicode_tagtv3_dict[encode_item] = "second_positions"
            second_positions_list = set(second_positions_list)

            # 部位同义词处理
            suffix_list = ["部"]
            extra_second_positions_dict = dict()
            for position_term in second_positions_list:
                for suffix_term in suffix_list:
                    dis_pos_term = position_term.replace(suffix_term, "")
                    if dis_pos_term != position_term:
                        if len(dis_pos_term) > 0 and dis_pos_term not in cls.extra_second_positions_dict:
                            cls.extra_second_positions_dict[dis_pos_term] = set()
                        cls.extra_second_positions_dict[dis_pos_term].add(position_term)
                        cls.total_tagv3_dict[dis_pos_term] = "extra_second_position"
                        cls.unicode_tagtv3_dict[dis_pos_term] = "extra_second_position"

            first_demands_list = list()
            zhengxing_cursor.execute(first_demands_sql)
            sql_tag_results = zhengxing_cursor.fetchall()
            for item in sql_tag_results:
                encode_item = item[0].encode("utf-8")
                first_demands_list.append(encode_item)
                jieba.add_word(encode_item)
                cls.total_tagv3_dict[encode_item] = "first_demands"
                cls.unicode_tagtv3_dict[encode_item] = "first_demands"
            first_demands_list = set(first_demands_list)

            first_solutions_list = list()
            zhengxing_cursor.execute(first_solutions_sql)
            sql_tag_results = zhengxing_cursor.fetchall()
            for item in sql_tag_results:
                encode_item = item[0].encode("utf-8")
                first_solutions_list.append(encode_item)
                jieba.add_word(encode_item)
                cls.total_tagv3_dict[encode_item] = "first_solutions"
                cls.unicode_tagtv3_dict[encode_item] = "first_solutions"
            first_solutions_list = set(first_solutions_list)

            first_positions_list = list()
            zhengxing_cursor.execute(first_positions_sql)
            sql_tag_results = zhengxing_cursor.fetchall()
            for item in sql_tag_results:
                encode_item = item[0].encode("utf-8")
                first_positions_list.append(encode_item)
                jieba.add_word(encode_item)
                cls.total_tagv3_dict[encode_item] = "first_positions"
                cls.unicode_tagtv3_dict[encode_item] = "first_positions"
            first_positions_list = set(first_positions_list)
            for position_term in first_positions_list:
                print(type(position_term))
                for suffix_term in suffix_list:
                    print(type(suffix_term))
                    dis_pos_term = position_term.decode().replace(suffix_term, "")
                    if len(dis_pos_term) > 0 and dis_pos_term != position_term:
                        if dis_pos_term not in cls.extra_first_positions_dict:
                            cls.extra_first_positions_dict[dis_pos_term] = set()
                        cls.extra_first_positions_dict[dis_pos_term].add(position_term)
                        cls.total_tagv3_dict[dis_pos_term] = "extra_first_position"
                        cls.unicode_tagtv3_dict[dis_pos_term] = "extra_first_position"

            zhengxing_cursor.execute(tag_v3_project_sql)
            sql_tag_results = zhengxing_cursor.fetchall()
            for item in sql_tag_results:
                encode_item = item[0].encode("utf-8")
                jieba.add_word(encode_item)
                cls.total_tagv3_dict[encode_item] = "tag_v3"
                cls.unicode_tagtv3_dict[encode_item] = "tag_v3"

            # zhengxing_cursor.execute(tag_v3_synonym_sql)
            # sql_tag_results = zhengxing_cursor.fetchall()
            # for item in sql_tag_results:
            #     encode_item = item[0].encode("utf-8")
            #     jieba.add_word(encode_item)
            #     cls.total_tagv3_dict[encode_item] = "tag"
        except:
            logging.error("catch exception,err_msg:%s" % traceback.format_exc())
            return dict()

    @classmethod
    def analysis_word(cls, word, tree):
        try:
            end, sent_len = 0, len(word)
            find_term_info_dict = dict()
            cur_index = 0
            # import pdb
            # pdb.set_trace()
            while cur_index < sent_len:
                multi_match_list = match_sentence(word, tree.root, cur_index)
                cur_index += 1
                for term_tuple in multi_match_list:
                    end, entity_len, entity_type = term_tuple
                    # end, entity_len, entity_type = match_sentence(word, tree.root, cur_index)
                    if entity_type:
                        attr_word_set = set()
                        if entity_type == "extra_first_position":
                            entity_type = "first_position"
                            temp_attr_word_set = cls.extra_first_positions_dict[
                                word[end - entity_len:end].encode("utf-8")]
                            attr_word_set = (term for term in temp_attr_word_set)
                        elif entity_type == "extra_second_position":
                            entity_type = "second_position"
                            temp_attr_word_set = cls.extra_second_positions_dict[
                                word[end - entity_len:end].encode("utf-8")]
                            attr_word_set = (term for term in temp_attr_word_set)
                        else:
                            attr_word_set.add(word[end - entity_len:end])

                        if entity_type not in find_term_info_dict:
                            find_term_info_dict[entity_type] = set()
                        find_term_info_dict[entity_type] = find_term_info_dict[entity_type].union(attr_word_set)

            return find_term_info_dict
        except:
            logging.error("catch exception,err_msg:%s" % traceback.format_exc())
            return dict()


def send_email_tome():
    try:
        date = datetime.datetime.now().date() - datetime.timedelta(days=1)
        fromaddr = 'lixiaofang@igengmei.com'
        password = '5dBf6ZeZwsp2GGQM'
        toaddrs = "lixiaofang@igengmei.com"

        content = 'hi  all:附件为' + str(date) + '的搜索词数据统计结果以及近一周的数据统计结果，请查收！'
        textApart = MIMEText(content)

        zipFile = '搜索词近三个月.xls'
        # zipFile = '昨日数据统计结果.xls'
        zipApart = MIMEApplication(open(zipFile, 'rb').read())
        zipApart.add_header('Content-Disposition', 'attachment', filename=zipFile)

        m = MIMEMultipart()
        m.attach(textApart)
        m.attach(zipApart)
        m['From'] = formataddr(["李小芳", fromaddr])
        m["To"] = formataddr(["李小芳", toaddrs])
        m['Subject'] = '每日搜索词结果统计'
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


def by_tag_name_get_id(name, type=2):
    db_zhengxing_eagle = pymysql.connect(host="bj-cdb-6slgqwlc.sql.tencentcdb.com", port=62120, user="work",
                                         password="Gengmei1",
                                         db="zhengxing_test",
                                         charset='utf8',
                                         cursorclass=pymysql.cursors.DictCursor)
    zhengxing_cursor = db_zhengxing_eagle.cursor()
    if type == 1:
        sql = "select id from api_tag_3_0 where name ='%s'" % (name)
    else:
        sql = "select id from api_tag_attr where name ='%s'" % (name)

    zhengxing_cursor.execute("set names 'UTF8'")
    zhengxing_cursor.execute(sql)
    data = zhengxing_cursor.fetchall()
    if data:
        tag_id = data[0].get("id", None)

        return str(tag_id)
    else:
        return None


def get_highlight_query(fields=[], query=''):
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
        'pre_tags': ['<%s>' % HIGHLIGHT_TAG],
        'post_tags': ['</%s>' % HIGHLIGHT_TAG],
        "require_field_match": False,

    }
    return field_highlight


def analyzer_query_tag_relation(query=None, first_demands_name_list=[], second_demands_name_list=[],
                                first_solutions_name_list=[], second_solutions_name_list=[],
                                first_positions_name_list=[], second_positions_name_list=[], tagv3_name_list=[]):
    """
    :param query:
    :return:
    """
    try:
        tag_v3_redis_name = "doris:search:tag_v3_mapping:" + query
        attr_tag_key = "doris:save_attr_tag_by_name"

        redis_tag_mapping_data = redis_client.get(tag_v3_redis_name)
        if redis_tag_mapping_data:
            tagv3_name_list.append(query)
            redis_tag_mapping_dict = json.loads(redis_tag_mapping_data) if redis_tag_mapping_data else {}
            if "first_solutions" in redis_tag_mapping_dict and len(redis_tag_mapping_dict["first_solutions"]) > 0:
                first_solutions_name_list = redis_tag_mapping_dict["first_solutions"]
            if "first_demands" in redis_tag_mapping_dict and len(redis_tag_mapping_dict["first_demands"]) > 0:
                first_demands_name_list = redis_tag_mapping_dict["first_demands"]
            if "positions" in redis_tag_mapping_dict and len(redis_tag_mapping_dict["positions"]) > 0:
                first_positions_name_list = redis_tag_mapping_dict["positions"]
            if "second_solutions" in redis_tag_mapping_dict and len(redis_tag_mapping_dict["second_solutions"]) > 0:
                second_solutions_name_list = redis_tag_mapping_dict["second_solutions"]
            if "second_demands" in redis_tag_mapping_dict and len(redis_tag_mapping_dict["second_demands"]) > 0:
                second_demands_name_list = redis_tag_mapping_dict["second_demands"]
            if "second_positions" in redis_tag_mapping_dict and len(redis_tag_mapping_dict["second_positions"]) > 0:
                second_positions__name_list = redis_tag_mapping_dict["second_positions"]
            logging.info(
                "query:%s,get first_solutions_name_list:%s,first_demands_name_list:%s,first_positions_name_list:%s,second_solutions_name_list:%s,second_demands_name_list:%s,second_positions__name_list:%s" % (
                    query, first_solutions_name_list, first_demands_name_list, first_positions_name_list,
                    second_solutions_name_list, second_demands_name_list, second_positions_name_list))
        else:
            all_attr_tag_data = redis_client.hgetall(attr_tag_key)
            if all_attr_tag_data:
                for item, values in all_attr_tag_data.items():
                    redis_value = json.loads(values)
                    attr_rela = redis_value.get(query, [])
                    if attr_rela:
                        item = str(item, encoding="utf-8")
                        if item == "second_demands_tag":
                            first_demands_name_list.extend(attr_rela)
                            second_demands_name_list.append(query)
                        if item == "first_demands_tag":
                            second_demands_name_list.extend(attr_rela)
                            first_demands_name_list.append(query)

                        if item == "first_soultions_tag":
                            second_solutions_name_list.extend(attr_rela)
                            first_solutions_name_list.append(query)
                        if item == "second_solutions_tag":
                            first_solutions_name_list.extend(attr_rela)
                            second_solutions_name_list.append(query)

                        if item == "first_positions_tag":
                            second_positions_name_list.extend(attr_rela)
                            first_positions_name_list.append(query)
                        if item == "second_positions_tag":
                            first_positions_name_list.extend(attr_rela)
                            second_positions_name_list.append(query)
            logging.info(
                "query:%s,get first_solutions_name_list:%s,first_demands_name_list:%s,first_positions_name_list:%s,second_solutions_name_list:%s,second_demands_name_list:%s,second_positions__name_list:%s" % (
                    query, first_solutions_name_list, first_demands_name_list, first_positions_name_list,
                    second_solutions_name_list, second_demands_name_list, second_positions_name_list))

        return first_solutions_name_list, first_demands_name_list, first_positions_name_list, second_solutions_name_list, second_demands_name_list, second_positions_name_list, tagv3_name_list

    except:
        logging.error("catch exception,logins:%s" % traceback.format_exc())
        return [], [], [], [], [], [], []


def save_tag(key, com_tagname):
    first_demands_name_list = []
    second_demands_name_list = []
    first_solutions_name_list = []
    second_solutions_name_list = []
    first_positions_name_list = []
    second_positions_name_list = []
    tagv3_name_list = []

    first_demands_ids_list = []
    second_demands_ids_list = []
    first_solutions_ids_list = []
    second_solutions_ids_list = []
    first_positions_ids_list = []
    second_positions_ids_list = []
    tagv3_ids_list = []

    if key == "tags_v3" and com_tagname not in tagv3_name_list:
        tagv3_name_list.append(com_tagname)
        tag_id = by_tag_name_get_id(name=com_tagname, type=1)
        if tag_id:
            tagv3_ids_list.append(tag_id)

    if key == "first_demands" and com_tagname not in first_demands_name_list:
        first_demands_name_list.append(com_tagname)
        tag_id = by_tag_name_get_id(name=com_tagname)
        if tag_id:
            first_demands_ids_list.append(tag_id)

    if key == "second_demands" and com_tagname not in second_demands_name_list:
        second_demands_name_list.append(com_tagname)
        tag_id = by_tag_name_get_id(name=com_tagname)
        if tag_id:
            second_demands_ids_list.append(tag_id)

    if key == "first_solutions" and com_tagname not in first_solutions_name_list:
        first_solutions_name_list.append(com_tagname)
        tag_id = by_tag_name_get_id(name=com_tagname)
        if tag_id:
            first_solutions_ids_list.append(tag_id)

    if key == "second_solutions" and com_tagname not in second_solutions_name_list:
        second_solutions_name_list.append(com_tagname)
        tag_id = by_tag_name_get_id(name=com_tagname)
        if tag_id:
            second_solutions_ids_list.append(tag_id)

    if key == "positions" and com_tagname not in first_positions_name_list:
        first_positions_name_list.append(com_tagname)
        tag_id = by_tag_name_get_id(name=com_tagname)
        if tag_id:
            first_positions_ids_list.append(tag_id)

    if key == "second_positions" and com_tagname not in second_positions_name_list:
        second_positions_name_list.append(com_tagname)
        tag_id = by_tag_name_get_id(name=com_tagname)
        if tag_id:
            second_solutions_ids_list.append(tag_id)

    return [tagv3_name_list, first_solutions_name_list, second_solutions_name_list, first_demands_name_list,
            second_demands_name_list, first_positions_name_list, second_positions_name_list,
            tagv3_ids_list, first_positions_ids_list, second_positions_ids_list, first_demands_ids_list,
            second_demands_ids_list, first_solutions_ids_list, second_solutions_ids_list]


def get_target_tag(highlight, all_token_dict, query):
    """
    :param highlight:
    :return:
    """
    first_demands_name_list = []
    second_demands_name_list = []
    first_solutions_name_list = []
    second_solutions_name_list = []
    first_positions_name_list = []
    second_positions_name_list = []
    tagv3_name_list = []

    first_demands_ids_list = []
    second_demands_ids_list = []
    first_solutions_ids_list = []
    second_solutions_ids_list = []
    first_positions_ids_list = []
    second_positions_ids_list = []
    tagv3_ids_list = []
    for item in highlight:
        for key, value in item.items():
            for tag_name in value:
                rel = re.compile(r"<ems>(.*?)</ems>", re.S)
                tag = re.findall(rel, str(tag_name))
                ems_tagname = tag_name.replace("<ems>", "").replace("</ems>", "")
                if ems_tagname == query:
                    [tagv3_name_list, first_solutions_name_list, second_solutions_name_list, first_demands_name_list,
                     second_demands_name_list, first_positions_name_list, second_positions_name_list,
                     tagv3_ids_list, first_positions_ids_list, second_positions_ids_list, first_demands_ids_list,
                     second_demands_ids_list, first_solutions_ids_list, second_solutions_ids_list] = save_tag(key=key,
                                                                                                              com_tagname=ems_tagname)
                else:
                    ana_info_list = []
                    for ana_tag in tag:
                        ana_info = all_token_dict.get(ana_tag, None)
                        if ana_info:
                            ana_info['query'] = ana_tag
                            ana_info_list.append(ana_info)
                    sorted(ana_info_list, key=lambda x: x['position'])
                    bol_tag = False
                    count = 0
                    for i in range(0, len(ana_info_list)):

                        if count < len(ana_info_list) - 1:
                            end = ana_info_list[i].get('end', None)
                            start_1 = ana_info_list[i + 1].get('start', None)
                            if end == start_1:
                                print("可以衔接上")
                                bol_tag = True
                            else:
                                print("衔接不上")
                                bol_tag = False
                        else:
                            end = ana_info_list[i].get('end', None)
                            start = ana_info_list[i].get('start', None)
                            end_1 = ana_info_list[i - 1].get('end', None)
                            if end != len(query):
                                print("衔接不上")
                                bol_tag = False
                            else:
                                if len(ana_info_list) == 1:
                                    anan_query = ana_info_list[0]['query']
                                    if anan_query == query:
                                        print("一样的")
                                        bol_tag = True

                                else:
                                    if start == end_1:
                                        bol_tag = True
                                    else:
                                        bol_tag = False

                        count += 1
                    if bol_tag:
                        [tagv3_name_list, first_solutions_name_list, second_solutions_name_list,
                         first_demands_name_list, second_demands_name_list, first_positions_name_list,
                         second_positions_name_list,
                         tagv3_ids_list, first_positions_ids_list, second_positions_ids_list, first_demands_ids_list,
                         second_demands_ids_list, first_solutions_ids_list, second_solutions_ids_list] = save_tag(
                            key=key, com_tagname=ems_tagname)

    return {"tagv3_name_list": tagv3_name_list, "first_solutions_name_list": first_solutions_name_list,
            "second_solutions_name_list": second_solutions_name_list,
            "first_demands_name_list": first_demands_name_list, "second_demands_name_list": second_demands_name_list,
            "first_positions_name_list": first_positions_name_list,
            "second_positions_name_list": second_positions_name_list, "tagv3_ids_list": tagv3_ids_list,
            "first_positions_ids_list": first_positions_ids_list,
            "second_positions_ids_list": second_positions_ids_list, "first_demands_ids_list": first_demands_ids_list,
            "second_demands_ids_list": second_demands_ids_list, "first_solutions_ids_list": first_solutions_ids_list,
            "second_solutions_ids_list": second_solutions_ids_list}


def handle_tag(first_solutions_name_list=[], first_demands_name_list=[], first_positions_name_list=[],
               second_solutions_name_list=[], second_demands_name_list=[], second_positions_name_list=[],
               tagv3_name_list=[], word_attr_info_dict=[]):
    try:
        for entity_type in word_attr_info_dict:
            for item in word_attr_info_dict[entity_type]:
                if entity_type == "tags_v3" and item not in tagv3_name_list:
                    tagv3_name_list.append(item)

                if entity_type == "first_demands" and item not in first_demands_name_list:
                    first_demands_name_list.append(item)

                if entity_type == "second_demands" and item not in second_demands_name_list:
                    second_demands_name_list.append(item)

                if entity_type == "first_solutions" and item not in first_solutions_name_list:
                    first_solutions_name_list.append(item)

                if entity_type == "second_solutions" and item not in second_solutions_name_list:
                    second_solutions_name_list.append(item)

                if entity_type == "positions" and item not in first_positions_name_list:
                    first_positions_name_list.append(item)

                if entity_type == "second_positions" and item not in second_positions_name_list:
                    second_positions_name_list.append(item)

            return [tagv3_name_list, first_demands_name_list, second_demands_name_list, first_solutions_name_list,
                    second_solutions_name_list, first_positions_name_list, second_positions_name_list]
    except:
        pass


def query_filter_tractate_v1(query=None):
    try:
        cut_word = []
        q = {}
        all_token_dict = {}
        body = {
            'text': query,
            'analyzer': "gm_default_index"
        }

        res = es.indices.analyze(index="gm_test-tractate", body=body)
        for item in res["tokens"]:
            token = item["token"]
            cut_word.append(token)
            all_token_dict[token] = {"start": item['start_offset'], "end": item['end_offset'],
                                     "position": item['position'], 'type': item['type']}

        multi_fields = {
            "tags_v3": 10,
            "first_demands": 6,
            "second_demands": 9,
            "first_solutions": 5,
            "second_solutions": 8,
            "positions": 4,
            "second_positions": 7
        }
        fields = ['^'.join((k, str(v))) for (k, v) in multi_fields.items()]
        multi_match = {
            'query': query,
            'type': 'best_fields',
            'operator': 'and',
            'fields': fields,
            "analyzer": "gm_default_index"
        }

        q["query"] = {
            "function_score": {
                "functions": [
                    {
                        "filter": {
                            "bool": {
                                "should": [
                                    {"term": {"tags_v3": query}},
                                    {"term": {"second_demands": query}},
                                    {"term": {"second_solutions": query}},
                                    {"term": {"second_positions": query}},
                                    {"term": {"first_demands": query}},
                                    {"term": {"first_solutions": query}},
                                    {"term": {"positions": query}}
                                ]
                            }
                        },
                        "weight": 10000

                    },
                    {
                        "filter": {
                            "bool": {
                                "should": {
                                    "multi_match": {
                                        'query': query,
                                        'type': 'best_fields',
                                        'operator': 'and',
                                        'fields': fields,
                                    }
                                }
                            }
                        },
                        "weight": 7000

                    }
                ],
                "query": {
                    "bool": {
                        "must": [{"term": {"is_online": True}},
                                 {"term": {"status": "3"}}],
                        "should": [
                            {"multi_match": multi_match}

                        ],
                        "minimum_should_match": 1,

                    }
                },
                "boost_mode": "sum",
                "score_mode": "sum"
            },

        }

        q["highlight"] = get_highlight_query(
            ["tags_v3", "first_demands", "second_demands", "first_solutions", "second_solutions", "positions",
             "second_positions"], query)
        q['size'] = 100

        q['sort'] = [
            {
                "_score": {
                    "order": "desc"
                }
            }, {
                "tractate_score": {
                    "order": "desc"
                }
            }
        ]
        tractate_extra = []
        res = es.search(index="gm_test-tractate-read", doc_type="tractate", body=q)
        res_hit = res["hits"]["hits"]
        for item in res_hit:
            if '_source' in item:
                highlight = item.get('highlight')
                if highlight != None:
                    tractate_extra.append(highlight)

        return tractate_extra, all_token_dict
    except:
        logging.error("catch exception,logins:%s" % traceback.format_exc())
        return [], []


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
                    data_sheet.write((j + k), i, str(row[i]) if len(row[i]) > 0 else row[i], default)
                except:
                    print(i)
                    raise
                # data_sheet.write(1, i, row1[i], self.set_style('Times New Roman', 220, True))
            k = k + 1
        workbook.save(path)
        print("写入文件成功，共" + str(k) + "行数据")


if __name__ == "__main__":
    data = open("data2", "r", encoding="utf-8")

    all_query_dict = {}
    all_query_list = []
    for item in data.readlines():
        query_num = item.strip().split()
        all_query_dict[query_num[0]] = query_num[1]
        all_query_list.append(query_num[0])

    query_relation_tag = {}
    tag_names_list = []
    all_data_day = []

    for item in all_query_list:
        ##拿到该query词对应的新标签信息
        first_solutions_name_list, first_demands_name_list, first_positions_name_list, second_solutions_name_list, second_demands_name_list, second_positions_name_list, tagv3_name_list = analyzer_query_tag_relation(
            query=item)
        word_attr_info_dict = get_analy_tag(word=item)
        print("**********", word_attr_info_dict)
        all_tag_info = handle_tag(
            first_solutions_name_list=first_solutions_name_list,
            first_demands_name_list=first_demands_name_list,
            first_positions_name_list=first_positions_name_list,
            second_solutions_name_list=second_solutions_name_list,
            second_demands_name_list=second_demands_name_list,
            second_positions_name_list=second_positions_name_list,
            tagv3_name_list=tagv3_name_list, word_attr_info_dict=word_attr_info_dict)

        print("all_tag_info:%s" % all_tag_info)
        relation_tags = {}
        for i in all_tag_info:
            for j in i:
                tractate_extra, all_token_dict = query_filter_tractate_v1(query=item)
                print("tractate_extra:%s" % tractate_extra)
                target_tag = get_target_tag(tractate_extra, all_token_dict, item)
                for key, value in target_tag.items():
                    if key not in relation_tags.keys():
                        relation_tags[key] = value
                    else:
                        relation_tags[key].extend(value)
                print("relation_tags:%s" % relation_tags)
        query_relation_tag[item] = relation_tags
        print("item:%s,relation_tags:%s" % (item, relation_tags))

    tup_title = (
        "搜索query", "过去3个月搜索量", "命中的项目标签name", "命中1级方式name", "命中2级方式name", "命中1级诉求name", "命中2级诉求name", "命中1级部位name",
        "命中2级部位name", "命中的项目标签id", "命中1级方式id", "命中2级方式id", "命中1级诉求id", "命中2级诉求id", "命中1级部位id", "命中2级部位id")

    for key, value in query_relation_tag.items():
        if len(value) > 0:
            tag_names_list.append(
                [
                    key, str(all_query_dict[key]), value["tagv3_name_list"], value["first_solutions_name_list"],
                    value["second_solutions_name_list"], value["first_demands_name_list"],
                    value["second_demands_name_list"],
                    value["first_positions_name_list"],
                    value["second_positions_name_list"], value["tagv3_ids_list"], value["first_positions_ids_list"],
                    value["second_positions_ids_list"],
                    value["first_demands_ids_list"], value["second_demands_ids_list"],
                    value["first_solutions_ids_list"],
                    value["second_solutions_ids_list"]
                ]

            )

    all_data_day.append(tup_title)
    for item in tag_names_list:
        all_data_day.append(tuple(item))

    path = str("搜索词近三个月") + ".xls"
    WritrExcel().write_excel(path, tuple(all_data_day))
    send_email_tome()
