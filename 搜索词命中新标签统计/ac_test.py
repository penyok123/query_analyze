# -*- coding:utf-8 -*-
"""
Description: AC自动机

@author: WangLeAi
@date: 2018/8/19
"""
from collections import defaultdict
from django.views.decorators.cache import cache_page


class TrieNode(object):
    def __init__(self, value=None):
        self.value = value
        self.fail = None
        self.tail = 0
        self.children = {}


class Trie(object):
    def __init__(self, words, word_dict):
        print("初始化")
        self.root = TrieNode()
        self.count = 0
        self.words = words
        for word in words:
            self.insert(word)
        self.ac_automation()
        self.word_info = word_dict
        print("初始化完毕")

    def insert(self, sequence):
        """
        基操，插入一个字符串
        :param sequence: 字符串
        :return:
        """
        self.count += 1
        cur_node = self.root
        for item in sequence:
            if item not in cur_node.children:
                child = TrieNode(value=item)
                cur_node.children[item] = child
                cur_node = child
            else:
                cur_node = cur_node.children[item]
        cur_node.tail = self.count
        print("*" * 10, cur_node)

    def ac_automation(self):
        """
        构建失败路径
        :return:
        """
        queue = [self.root]
        while len(queue):
            temp_node = queue[0]
            queue.remove(temp_node)
            for value in temp_node.children.values():
                if temp_node == self.root:
                    value.fail = self.root
                else:
                    p = temp_node.fail
                    while p:
                        if value.value in p.children:
                            value.fail = p.children[value.value]
                            break
                        p = p.fail
                    if not p:
                        value.fail = self.root
                queue.append(value)

    def search(self, text):
        """
        模式匹配
        :param self:
        :param text: 长文本
        :return:
        """
        p = self.root
        start_index = 0
        rst = defaultdict(list)
        rst_all = list()

        for i in range(len(text)):
            single_char = text[i]
            while single_char not in p.children and p is not self.root:
                p = p.fail
            if single_char in p.children and p is self.root:
                start_index = i
            if single_char in p.children:
                p = p.children[single_char]
            else:
                start_index = i
                p = self.root
            temp = p
            while temp is not self.root:
                if temp.tail:
                    sindex = (start_index, i)
                    type = self.word_info[self.words[temp.tail - 1]]
                    rst[self.words[temp.tail - 1]].append(sindex)

                temp = temp.fail
        print(rst_all)
        return rst


if __name__ == "__main__":
    import pickle
    import redis

    REDIS_URL = "redis://redis.paas-test.env:6379/1"
    redis_client = redis.StrictRedis.from_url(REDIS_URL)

    all_data = {}
    test_text = """不知、不觉·间我~|~已经忘了爱❤。"""
    test_words = ["不知", "不觉", "忘了爱", "不"]
    word_dict = {"不知": "doctor", "不": "hopital", "不觉": "tagv3", "忘了爱": "tagv3"}
    model = Trie(test_words, word_dict)
    redis_client.set("ac_tree", pickle.dumps(model))
    content = model.search(test_text)
    all_words = []
    for item in content.items():
        all_data[item[0]] = item[1]
    print(all_data)

    # f = open('tree.pickle', 'rb')
    # model = pickle.load(f)  # 从f文件中提取出模型赋给clf2
    # content = model.search(test_text)
    # for key, value in all_data.items():
    #     if [key for item in all_data.keys().remove(item) if key in item or key == item]:
