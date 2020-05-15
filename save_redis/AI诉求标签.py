#!/usr/bin/env python
# -*- coding: utf-8 -*-
import redis
import json
import redis
from django.conf import settings

REDIS_URL = "redis://redis.paas-test.env:6379/0"
# REDIS_URL = 'redis://:ReDis!GmTx*0aN6@172.16.40.133:6379'

redis_client = redis.StrictRedis.from_url(REDIS_URL)
operator_category_key = "doris:ai_save_second_demonds_to_redis"

all_second_demods = ['祛黑眼圈', '祛眼袋', '除法令纹', '祛黑头', '缩毛孔', '祛痘', '祛痘印', '祛痘坑', '补水', '美白嫩肤', '洁面', '双眼皮', '开眼角', '嘴角上提',
                     '颧骨提升', '颧骨内推', '丰太阳穴', '缩短下巴', '下眼睑下至', '上眼睑提升', '缩鼻翼', '鼻部缩短', '瘦脸', '丰唇', '垫下巴', '缩短眼距', '嘴角上扬',
                     '薄唇', '鼻部加长', '人中缩短', '缩下颌角']

redis_client.set(operator_category_key, json.dumps(all_second_demods))
ss = redis_client.get(operator_category_key)
if ss:
    print(json.loads(ss))
