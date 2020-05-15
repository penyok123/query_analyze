import json
import datetime
import redis

# today = datetime.datetime.now()
#
# str_today = str(today.year) + str(today.month) + str(today.day)
# print(str_today)

REDIS_URL = "redis://redis.paas-test.env:6379/0"
redis_client = redis.StrictRedis.from_url(REDIS_URL)
card_info = {"card_id": 123, "comment_content": "嘻嘻嘻", "current_user_id": 23445}

# key = "auto_vest_one_user_action_answer" + str(1)
# redis_client.delete(key)

# redis_data = redis_client.hget(key, str_today)
# redis_data_30 = redis_client.hget(key, 2020130)
# print(redis_data)
# print(redis_data_30)
#
# if redis_data:
#     redis_data = json.loads(str(redis_data, encoding="utf8"))
#     click_num = int(redis_data.get("click")) + 1
#     redis_data['click'] = click_num
#     redis_client.hset(key, str_today, json.dumps(redis_data))
# else:
#     ##代表还没有存储或者是已经过去一天了 需要清掉数据 从新的一天开始
#     redis_client.delete(key)
#     redis_data = {"click": 1, "follow": 0, "comment": 0}
#     ss = redis_client.hset(key, str_today, json.dumps(redis_data))
#     print(ss)
#
#
# click_num = redis_data["click"]
# print(click_num)
# if click_num > 10:
#     print("------")
#     # send_email_tome(str(redis_data) + str(card_info))
# else:
#     print("++++++++")
# values = list(redis_data.values())
# s = [True for i in values if i > 10]

# key = 'have_reply_answer_comment:' + str(card_info['card_id'])
#
# # redis_client.delete(key)
#
#
# redis_data = redis_client.hget(key, card_info['current_user_id'])
# print(redis_data)
# if redis_data:
#     datas = json.loads(redis_data, encoding="utf-8")
#     print(datas)
#     if card_info['comment_content'] in datas:
#         print("当前评论和当前的用户已经存在了")
#         pass
#     else:
#         datas.append(card_info['comment_content'])
#         redis_client.hset(key, card_info['current_user_id'], json.dumps(datas))
# else:
#     conent = [card_info['comment_content']]
#     redis_client.hset(key, card_info['current_user_id'], json.dumps(conent))


# card_info = {"card_id": 123, "comment_content": "嘻嘻嘻", "current_user_id": 23445, "need_pust_num": 3, "have_pust_num": 2}
# today = datetime.datetime.now()
# str_today = str(today.year) + str(today.month) + str(today.day)
# key = "auto_vest_one_user_action_answer:" + str(card_info['card_id'])
# # redis_client.delete(key)
#
# redis_data = redis_client.hget(key, str_today)
#
# print(redis_data)
#
# if redis_data:
#     redis_data = json.loads(str(redis_data, encoding="utf8"))
#     have_pust_num = int(redis_data.get('comment_have_pust_num', card_info['have_pust_num']))
#     need_pust_num = int(redis_data.get('comment_need_pust_num', card_info['need_pust_num']))
#
#     print(have_pust_num)
#     print(need_pust_num)
#     if have_pust_num > need_pust_num:
#         print("当前下发次数:%s已经达上限%s次，不能再下发:%s" % (have_pust_num, need_pust_num, card_info))
#
#     else:
#         redis_data['comment_have_pust_num'] = have_pust_num + 1
#         redis_client.hset(key, str_today, json.dumps(redis_data))
# else:
#     redis_data = {"comment_have_pust_num": card_info['have_pust_num'],
#                   "comment_need_pust_num": card_info['need_pust_num']
#                   }
#     redis_client.hset(key, str_today, json.dumps(redis_data))
