#!/usr/bin/env python
# -*- coding: utf-8 -*-
import redis
import json
import redis
from django.conf import settings

REDIS_URL = "redis://redis.paas-test.env:6379/0"
# REDIS_URL = 'redis://:ReDis!GmTx*0aN6@172.16.40.133:6379'

redis_client = redis.StrictRedis.from_url(REDIS_URL)

operator_category = "doris:save_second_solutions_isoperator_to_redis"

all_data = ["皮肤手术", "拔牙", "鼻部手术", "补牙", "唇部手术", "耳部手术", "脸型手术", "切开", "手术矫正", "手术修复", "瘦身手术", "私处手术", "腿部手术", "胸部手术",
            "双眼皮手术", "眼部手术", "眼科手术", "妇科手术", "脚部手术", "疤痕手术治疗", "微创", "内切", "外切", "异物取出", "产科手术", "手部手术", "疤痕掩盖"]
redis_client.set(operator_category, json.dumps(all_data))

sss = redis_client.get(operator_category)
print(json.loads(sss))

"""
2级方式	1级方式
皮肤手术	手术
拔牙	手术
鼻部手术	手术
补牙	手术
唇部手术	手术
耳部手术	手术
脸型手术	手术
切开	手术
手术矫正	手术
手术修复	手术
瘦身手术	手术
私处手术	手术
腿部手术	手术
胸部手术	手术
双眼皮手术	手术
眼部手术	手术
眼科手术	手术
妇科手术	手术
脚部手术	手术
疤痕手术治疗	手术
微创	手术
内切	手术
外切	手术
异物取出	手术
产科手术	手术
手部手术	手术
疤痕掩盖	手术
"""
