import redis
import json

redis_url = 'redis://redis.paas-test.env:6379/0'
redis_client = redis.StrictRedis.from_url(redis_url)

answer_group_redis_name = "doris:answer_group_data"
tractate_group_redis_name = "doris:tractate_group_data"

f_7_tractate = [20891852]
f_7_answer = [544457, 544728]

f_6_answer = [545210]

f_5_tractate = ["80009", "69756", "34411", "8246", "10118", "3267", "15613", "72668", "75982", "39835", "9774", "70803",
                "6536", "24571", "11033", "76158", "19004", "458", "8555", "7172", "3974", "23320", "79373", "32381",
                "53131", "8514", "37054", "10487", "10346", "59994", "75768", "69971", "5617", "9479", "3185", "34190",
                "70803", "6749", "13986", "28260", "80211", "5731", "12031", "477", "8190", "4289", "470", "79004",
                "6324", "5270"]

f_5_answer = ["797348", "796947", "799976", "800383", "803628", "807763", "796259", "796787", "796797", "796112",
              "785043", "784844", "784533", "784410", "784361", "783337", "783549", "784300", "780494", "780454",
              "753832", "753852", "753949", "737119", "754052", "754007", "713556", "713475", "713554", "713550",
              "713481", "713480", "785096", "770923", "797270", "797326", "713486", "713551", "736973", "737157",
              "753772", "753792", "753847", "777380", "777429", "779133", "710854", "713552", "713801", "753804",
              "713791"]

f_4_tractate = ["77441", "75684", "85021", "84949", "84946", "84906", "85005", "77709", "75741", "76092", "17624",
                "8353", "76104", "75652", "84966", "84974", "69044", "75996", "76190", "42727", "76087", "68024",
                "8809", "84827", "84713", "13764", "8104", "75756", "77267", "77377", "77400", "76154", "75965",
                "75951", "75630", "43794", "32538", "10059", "8770", "77289", "77414", "8217", "8101", "84991", "76057",
                "76136", "71386", "75617", "76081", "54881"]
f_4_answer = ["803665", "799670", "797937", "797919", "797536", "796913", "783360", "781285", "780447", "776556",
              "772568", "748608", "713952", "713410", "712796", "711215", "710824", "713693", "711136", "797912",
              "779110", "777121", "776792", "776686", "776527", "776270", "775095", "753626", "753409", "753261",
              "736524", "502954", "702234", "696442", "567294", "518460", "737553", "432389", "797841", "797923",
              "810588", "781135", "781033", "781025", "781001", "780822", "777132", "754353", "754334", "748869"]
#
f_3_tractate = [12277182, 12277259]
f_3_answer = [552157, 552156]
#
f_2_tractate = [533948, 361]
f_2_answer = [533948, 361]

f_1_tractate = [12277487, 12277488, 12271784, 12271783, 12271782, 12272059, 12277488, 12277487, 12277435, 12277342,
                12277243]


for answer_id in f_6_answer:
    redis_data = redis_client.hget(answer_group_redis_name, answer_id)
    group_id_list = list()
    if redis_data:
        group_id_list = json.loads(redis_data)
        print(str(group_id_list), "6")
    group_id_list.append(6)
    redis_client.hset(answer_group_redis_name, answer_id, json.dumps(group_id_list))




# for answer_id in f_7_answer:
#     redis_data = redis_client.hget(answer_group_redis_name, answer_id)
#     group_id_list = list()
#     if redis_data:
#         group_id_list = json.loads(redis_data)
#         print(str(group_id_list), "7")
#     group_id_list.append(7)
#     redis_client.hset(answer_group_redis_name, answer_id, json.dumps(group_id_list))
#
# for tractate_id in f_7_tractate:
#     redis_data = redis_client.hget(tractate_group_redis_name, tractate_id)
#     group_id_list = list()
#     if redis_data:
#         group_id_list = json.loads(redis_data)
#         print(str(group_id_list), "7")
#     group_id_list.append(7)
#     redis_client.hset(tractate_group_redis_name, tractate_id, json.dumps(group_id_list))

# for tractate_id in f_5_tractate:
#     redis_data = redis_client.hget(tractate_group_redis_name, tractate_id)
#     group_id_list = list()
#     if redis_data:
#         group_id_list = json.loads(redis_data)
#         print(str(group_id_list), "5")
#     group_id_list.append(5)
#     redis_client.hset(tractate_group_redis_name, tractate_id, json.dumps(group_id_list))
#
# for tractate_id in f_4_tractate:
#     redis_data = redis_client.hget(tractate_group_redis_name, tractate_id)
#     group_id_list = list()
#     if redis_data:
#         group_id_list = json.loads(redis_data)
#         print(str(group_id_list), "4")
#     group_id_list.append(4)
#     redis_client.hset(tractate_group_redis_name, tractate_id, json.dumps(group_id_list))
#
# for tractate_id in f_3_tractate:
#     redis_data = redis_client.hget(tractate_group_redis_name, tractate_id)
#     group_id_list = list()
#     if redis_data:
#         group_id_list = json.loads(redis_data)
#         print(str(group_id_list), "3")
#     group_id_list.append(3)
#     redis_client.hset(tractate_group_redis_name, tractate_id, json.dumps(group_id_list))
#
# for tractate_id in f_2_tractate:
#     redis_data = redis_client.hget(tractate_group_redis_name, tractate_id)
#     group_id_list = list()
#     if redis_data:
#         group_id_list = json.loads(redis_data)
#         print(str(group_id_list), "2")
#     group_id_list.append(2)
#     redis_client.hset(tractate_group_redis_name, tractate_id, json.dumps(group_id_list))
# #
# for tractate_id in f_1_tractate:
#     redis_data = redis_client.hget(tractate_group_redis_name, tractate_id)
#     group_id_list = list()
#     if redis_data:
#         group_id_list = json.loads(redis_data)
#         print(str(group_id_list), "1")
#     group_id_list.append(1)
#     redis_client.hset(tractate_group_redis_name, tractate_id, json.dumps(group_id_list))
#
# for answer_id in f_5_answer:
#     redis_data = redis_client.hget(answer_group_redis_name, answer_id)
#     group_id_list = list()
#     if redis_data:
#         group_id_list = json.loads(redis_data)
#         print(str(group_id_list), "5")
#     group_id_list.append(5)
#     redis_client.hset(answer_group_redis_name, answer_id, json.dumps(group_id_list))
#
# for answer_id in f_4_answer:
#     redis_data = redis_client.hget(answer_group_redis_name, answer_id)
#     group_id_list = list()
#     if redis_data:
#         group_id_list = json.loads(redis_data)
#         print(str(group_id_list), "4")
#     group_id_list.append(4)
#     redis_client.hset(answer_group_redis_name, answer_id, json.dumps(group_id_list))
#
# for answer_id in f_3_answer:
#     redis_data = redis_client.hget(answer_group_redis_name, answer_id)
#     group_id_list = list()
#     if redis_data:
#         group_id_list = json.loads(redis_data)
#         print(str(group_id_list), "3")
#     group_id_list.append(3)
#     redis_client.hset(answer_group_redis_name, answer_id, json.dumps(group_id_list))

# for answer_id in f_2_answer:
#     redis_data = redis_client.hget(answer_group_redis_name, answer_id)
#     group_id_list = list()
#     if redis_data:
#         group_id_list = json.loads(redis_data)
#         print(str(group_id_list), "2")
#     group_id_list.append(2)
#     redis_client.hset(answer_group_redis_name, answer_id, json.dumps(group_id_list))

# for answer_id in f_1_answer:
#     redis_data = redis_client.hget(answer_group_redis_name, answer_id)
#     group_id_list = list()
#     if redis_data:
#         group_id_list = json.loads(redis_data)
#         print(str(group_id_list), "1")
#     group_id_list.append(1)
#     redis_client.hset(answer_group_redis_name, answer_id, json.dumps(group_id_list))
