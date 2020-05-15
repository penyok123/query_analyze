import threading
import time, redis
import threading

#
# REDIS_URL = 'redis://redis.paas-test.env:6379'
#
# redis_client = redis.StrictRedis.from_url(REDIS_URL)
# key = "good_tractate_user_id_sssssssss"
#
# if redis_client.hsetnx(key, [], "0"):
#     print(False)
# else:
#     print(True)

s = [{"term": {"id_online": True}}, {"term": {"tag_ids": [123]}}
