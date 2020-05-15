# coding=utf-8
import re, time, json, redis

from elasticsearch import Elasticsearch

es = Elasticsearch(
    [
        {
            'host': '172.16.31.17',
            'port': 9200,
        },
        {
            'host': '172.16.31.11',
            'port': 9200,
        },
        {
            'host': '172.16.31.13',
            'port': 9200,
        }
    ]
)
REDIS_URL = "redis://:ReDis!GmTx*0aN6@172.16.40.133:6379"
redis_client = redis.StrictRedis.from_url(REDIS_URL)


def get_es_result(tid=[]):
    max_id = 0
    q = {"query": {"terms": {"id": tid}},
         "sort": {"tractate_score": {"order": "desc"}, "last_modified": {"order": "desc"}}}

    res = es.search(index="gm_test-tractate-read", doc_type="tractate", body=q)
    if res['hits']['total'] > 0:
        max_id = res['hits']['hits'][0]["_source"]['id']

    return max_id


if __name__ == '__main__':
    file_data = open("t3", "r", encoding="utf-8")
    begin = time.time()
    should_show = []
    must_not_show = []
    for item in file_data.readlines():
        all_tid = [int(it) for it in item.strip().split(",")]
        max_id = get_es_result(all_tid)
        should_show.append(max_id)
        all_tid.remove(max_id)
        must_not_show.extend(all_tid)

    print(must_not_show)
    print(should_show)
    print(time.time() - begin)
    redis_client.set("tractate_simi_tids", json.dumps({"must_not_show": must_not_show, "should_show": should_show}))
    redis_d = redis_client.get('tractate_simi_tids')
    print(json.loads(redis_d))
