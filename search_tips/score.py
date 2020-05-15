Weight = {
    'search': 0.4,
    'trans': 0.6
}


def cal_score(self, search_rate, conversion_rate):
    s1 = self._cal_score(search_rate, 'SearchScore') * self.Weight['search']
    s2 = self._cal_score(conversion_rate, 'TransScore') * self.Weight['trans']
    return s1 + s2

# MySQL [bran_prod]> select sum(conversion_rate) from trade_tag_conversion where query in  ("隆鼻") and update_date ='2020-01-07' ;
# +----------------------+
# | sum(conversion_rate) |
# +----------------------+
# |   0.8207754500159429 |
# +----------------------+
#MySQL [bran_prod]> select sum(search_rate) from trade_tag_conversion where query in  ("隆鼻") and update_date ='2020-01-07' ;
# +---------------------+
# | sum(search_rate)    |
# +---------------------+
# | 0.24102549791666367 |
# +---------------------+
# 1 row in set (0.01 sec)
#
# MySQL [bran_prod]> select sum(conversion_rate) from trade_tag_conversion where query in  ("隆胸") and update_date ='2020-01-07' ;
# +----------------------+
# | sum(conversion_rate) |
# +----------------------+
# |                 NULL |
# +----------------------+
# 1 row in set (0.01 sec)
# MySQL [bran_prod]> select sum(search_rate) from trade_tag_conversion where query in  ("隆胸") and update_date ='2020-01-07' ;
# +------------------+
# | sum(search_rate) |
# +------------------+
# |             NULL |
# +------------------+


# MySQL [bran_prod]> select sum(conversion_rate) from trade_tag_conversion where query in  ("隆胸套餐") and update_date ='2020-01-07' ;
# +----------------------+
# | sum(conversion_rate) |
# +----------------------+
# |                  0.2 |
# +----------------------+
# 1 row in set (0.01 sec)
# MySQL [bran_prod]> select sum(search_rate) from trade_tag_conversion where query in  ("隆胸套餐") and update_date ='2020-01-07' ;
# +----------------------+
# | sum(search_rate)     |
# +----------------------+
# | 0.006143920712785568 |
# +----------------------+
