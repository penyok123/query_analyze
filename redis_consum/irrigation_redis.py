import redis
import json

REDIS_URL = "redis://redis.paas-test.env:6379/0"
redis_client = redis.StrictRedis.from_url(REDIS_URL)
offset = 30
partition = 1


def judge_offset_partition_have_consum(offset=0, partition=0):
    """
    根据当前的offset和分区去判断数据是否已经被消费
    :param offset:
    :param partition:
    :return:
    """
    redis_list_data = set()
    key = "irrigation_partition_offset_have_consum:" + str(partition)
    redis_data = redis_client.get(key)
    print(redis_data)
    if redis_data:
        redis_list_data = set(json.loads(redis_data))
        if offset in redis_list_data:
            return False
    redis_list_data.add(offset)
    redis_client.set(key, json.dumps(list(redis_list_data)))
    return True


ss = judge_offset_partition_have_consum(offset=offset, partition=partition)
print(ss)
