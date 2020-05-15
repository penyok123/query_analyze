#!/usr/bin/env python
# -*- coding: utf-8 -*-
import redis
import json
import redis
from django.conf import settings

REDIS_URL = "redis://redis.paas-test.env:6379/0"
redis_client = redis.StrictRedis.from_url(REDIS_URL)

data = {
    "first_demands": {"近视": 10, "填充": 15},
    "second_demands": {"双眼皮": 60},
    "first_solutions": {"手术": 25},
    "second_solutions": {"植发": 12},
    "first_positions": {"鼻子": 5},
    "second_positions": {"抬头纹": 15},
    "project": {"水光针": 50, "鼻子": 5, "双眼皮": 60, "胸部手术": 25, "植发": 12, "眼皮": 5, "皮肤": 10, "测试双眼皮": 100, "脚部手术": 200}
}

keys = "user_portrain_info:" + str(123456)

redis_client.set(keys, json.dumps(data))

project_tags = dict()
portrait_info = redis_client.get(keys)

if portrait_info:
    portrait_user_info = json.loads(portrait_info)
    project_tags = portrait_user_info.get("project", {})

    a1 = sorted(project_tags.items(), key=lambda x: x[1], reverse=True)

print(a1)
