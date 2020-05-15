#!/usr/bin/env python
# -*- coding: utf-8 -*-
import redis
import json
import redis
from django.conf import settings

REDIS_URL = "redis://redis.paas-test.env:6379/0"
redis_client = redis.StrictRedis.from_url(REDIS_URL)

diary_content_abstract_redis_name = "doris:diary_content_abstract"

sss = redis_client.hget(diary_content_abstract_redis_name, 1)

redis_client.hset(diary_content_abstract_redis_name, 1, "")
