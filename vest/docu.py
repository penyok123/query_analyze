####发回答后评论
#
# 2-4小时内随机，给予[0-1]个评论
#
# 对所有回答每天1次夜里24点轮询：
#
# 1天-6天之间发的的回答：
# 3星以下
# [0-1]个评论
# 4星以上
# [2-4]个评论
# 6天后，每10天：
# 3星以下
# [0-1]个评论
# 4星以上
# [0-2]个评论

# 轮询时间-发布时间超过365天，终止加评论

# 1.后端请求接口后传参数（卡片ID，卡片类型，创建时间，等级，标签名称[列表]）先拿到这部分数据后存到kafka里，然后去消费
#
#
#
# 2.拿到数据后先进行第一轮判断，如果当前时间-创建时间in（2，4）代表是当天，随机一个次数，并在2-4小时内一个随机时间（push-time），一个已经执行的次数，该执行的次数
#
#
# 3。系统轮训轮训当轮训到当前数据，判断时间是否大于当前的（push-time）如果是执行4，如果不是进入下一轮讯
#
#
# 4.如果到了该执行的时间了，给他开始执行；执行完了之后，就会进入1-6天的执行规则
#
# 5.当完成当天的执行后，
#  会去判断星级，并按照规则随机下发时间和次数
#  会给push-time重新一个随机24点之后的时间，和一个随机的该执行的次数，和当前执行次数重新赋值成0，表示一天后，该随机执行几次，下一次执行的时间
#
#
#
# 6.每次都得判断当前时间和创建时间的差


##########发回答后被加关注
# 发帖后2小时：[1-3]个粉丝
#
# 对所有回答每天1次轮询：
#
# 3星以下：
# 1天前发的回答：[1-3]个粉丝
# 2-15天前发的回答：[0-1]个粉丝
# 15天前或更早发的回答：每隔11天[0-2]个粉丝
# 2. 3星以上：
#
# 1天前发的回答：[5-10]个粉丝
# 前2-15天发的回答：[0-5]个粉丝
# 15天前或更早发的回答：每隔10天[0-2]个粉丝
#
# 3.轮询时间-发布时间超过365天，终止加粉


##########发回答后被点赞
# 发帖后2小时：[1-3]个赞
#
# 对所有帖子每天1次轮询：
#
# 3星以下：
# 1天前发的回答：[1-3]个赞
# 2-15天前发的回答：[0-1]个赞
# 15天前或更早发的：每隔6天[0-1]个赞
# 3星以上：
# 1天前发的回答：[6-12]个赞
# 2-15天前发的回答：[0-6]个赞
# 15天前或更早发的回答：每隔5天[0-2]个赞
#
# 3.轮询时间-发布时间超过365天，终止点赞

# import hashlib
#
#
# def recommed_service_category_device_id(device_id):
#     try:
#         '''
#         设备品类显示, 是否命中灰度
#         '''
#         categroy_select_cary1 = ["0", "1", "2", "3", "c", "d", "e", "f"]
#         categroy_select_cary2 = ["4", "5", "6", "a"]
#         categroy_select_cary3 = ["9", "8", "7", "b"]
#
#         if not device_id:
#             return 1
#
#         hd_id = hashlib.md5(str(device_id).encode()).hexdigest()
#
#         print(hd_id)
#         is_gray = hd_id[-1]
#
#         if is_gray in categroy_select_cary2:
#             return 2
#         elif is_gray in categroy_select_cary3:
#             return 3
#         else:
#             return 1
#     except:
#         return 1
#
#
# is_gray = recommed_service_category_device_id(device_id="867961030707205c")
#
# print(is_gray)
#
#
# #   123456ASBBBWWWfffvvfsfsfvv   3
#
# import datetime
#
# one_month_ago = datetime.datetime.now() - datetime.timedelta(days=30)
# sss= one_month_ago.strftime("%Y-%m-%d %H:%M:%S")
# print(type(sss))
# print(sss)


# import copy
#
# dic = {'key1': 123, 'key2': [123, 456]}  # 创建一个字典嵌套列表
#
# print(dic['key2'][0])  # 打印列表中的地址
#
# print("\n")
#
# new_dic = copy.deepcopy(dic)  # 使用浅拷贝赋值
# new_dic2222 = copy.deepcopy(dic)  # 使用浅拷贝赋值
#
#
# new_dic['key2'][0] = 789  # 改变字典中列表的值
#
# print(dic['key2'][0])
# print((new_dic['key2'][0]))
# print(new_dic2222)
from pytz import timezone
import datetime
import time

one_month_ago = time.mktime(
    time.strptime((datetime.datetime.now() - datetime.timedelta(days=30)).strftime('%Y-%m-%d %H:%M:%S'),
                  '%Y-%m-%d %H:%M:%S'))

# print(one_month_ago)
# print(type(one_month_ago))
#
# sss = time.mktime(one_month_ago)
# print(one_month_ago)


# timeStamp = one_month_ago
# dateArray = datetime.datetime.fromtimestamp(timeStamp)
# print(dateArray)
# otherStyleTime = dateArray.strftime("%Y-%m-%d %H:%M:%S")
# print(otherStyleTime)   # 2013--10--10 23:40:00


# def tzlc(dt, truncate_to_sec=True):
#     print(dt)
#     if dt is None:
#         return None
#     if truncate_to_sec:
#         dt = dt.replace(microsecond=0)
#     return timezone("UTC").localize(dt)
#
#
# now_str = tzlc(datetime.datetime.now()- datetime.timedelta(days=30))
#
# print(now_str)
# print(type(now_str))


# tag_relations = {
#     'tag_type_list': [{'id': 9, 'description': '省份'}, {'id': 4, 'description': '城市'}, {'id': 6, 'description': '医生'},
#                       {'id': 1, 'description': '一级分类'}, {'id': 7, 'description': '医院'},
#                       {'id': 3, 'description': '三级分类'}, {'id': 5, 'description': '自由添加'},
#                       {'id': 11, 'description': '运营标签'}, {'id': 2, 'description': '二级分类'},
#                       {'id': 10, 'description': '国家'}, {'id': 12, 'description': '大学'}, {'id': 8, 'description': '频道'}],
#     'tag_queried': None,
#     'tag_relations': [{'child_tag_id': 81, 'parent_tag_id': 14}, {'child_tag_id': 81, 'parent_tag_id': 758},
#                       {'child_tag_id': 2078, 'parent_tag_id': 81}, {'child_tag_id': 16, 'parent_tag_id': 758},
#                       {'child_tag_id': 16, 'parent_tag_id': 1074}, {'child_tag_id': 16, 'parent_tag_id': 1}],
#     'tag_list': [{'tag_type_id': 1, 'is_online': True, 'id': 1, 'name': '眼眉整形'},
#                  {'tag_type_id': 1, 'is_online': True, 'id': 14, 'name': '术后修复'},
#                  {'tag_type_id': 2, 'is_online': True, 'id': 16, 'name': '泪沟'},
#                  {'tag_type_id': 2, 'is_online': True, 'id': 81, 'name': '轮廓修复'},
#                  {'tag_type_id': 5, 'is_online': True, 'id': 1074, 'name': '眼部整形'},
#                  {'tag_type_id': 8, 'is_online': True, 'id': 758, 'name': '整形'},
#                  {'tag_type_id': 2, 'is_online': True, 'id': 2078, 'name': 'sd'}]}
#
# all_tag_ids = [16, 2078]
# all_have_get_ids = []
# parent_tag_info = []
#
# tag_list = tag_relations.get('tag_list', None)
# tag_relations = tag_relations.get('tag_relations', None)
#
# for item in tag_relations:
#     print(item)
#     current_id = item.get('child_tag_id', None)
#
#     if current_id in all_tag_ids and current_id not in all_have_get_ids:
#         print("----")
#         all_have_get_ids.append(current_id)
#
#         ##先拿到当前的标签的父级ID包括父级的父级
#         parent_tag_id = []
#
#         child_tag_id = item.get('child_tag_id', None)
#         current_name = [{'name': sm['name'], "tag_type_id": sm['tag_type_id']} for sm in tag_list if
#                         sm['id'] == current_id]
#
#         parent_tag_id = [item['parent_tag_id'] for item in tag_relations if
#                          item['child_tag_id'] == child_tag_id]
#
#         parent_tag_id.extend([item['parent_tag_id'] for item in tag_relations if
#                               item['child_tag_id'] in parent_tag_id])
#
#         print(parent_tag_id)
#
#         parent_tag_info.extend(
#             [{"parent_tag_name": parent_tag['name'], "parent_id": parent_tag['id'],
#               "parent_type_id": parent_tag['tag_type_id'], "keyword_id": current_id,
#               "keyword_type_id": current_name[0]['tag_type_id'], 'keyword': current_name[0]['name']} for
#              parent_tag
#              in tag_list if
#              parent_tag['id'] in parent_tag_id and parent_tag['is_online'] == True and parent_tag[
#                  'tag_type_id'] == 1])
#
# print()
# print(parent_tag_info)
# import time
# begin = time.time()
# print(begin)
#
# ss = '2017-09-19T11:48:28+08:00'

# 1505792920
# time.sleep(0.8)
# print(time.time()-begin)
import redis
import json

redis_url = 'redis://redis.paas-test.env:6379/0'
redis_client = redis.StrictRedis.from_url(redis_url)

answer_group_redis_name = "doris:answer_group_data_ids"
tractate_group_redis_name = "doris:tractate_group_data_ids"

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

f_3_tractate = ["84843", "84965", "11534", "2136", "38439", "84877", "36864", "9963", "80028", "76105", "76098",
                "76049", "75973", "75733", "76140", "76100", "36773", "7569", "75726", "9217", "32422", "72278",
                "76031", "75972", "76106", "75803", "85191", "76138", "75954", "75628", "75667", "75980", "76041",
                "78947", "83512", "83661", "5574", "17769", "3572", "79491", "47198", "76252", "75776", "85155",
                "70894", "75613", "28248", "2132", "75696", "11298", "76078", "3050", "76174", "75612", "76173",
                "84369", "1763", "7061", "6519", "3798", "76045", "84372", "85176", "76044", "85158", "85170", "85173",
                "85160", "85162", "85200", "85166", "85183", "75697"]
f_3_answer = ["713476", "713341", "713322", "713318", "713289", "713035", "713555", "713029", "713025", "711433",
              "711427", "711432", "711430", "711424", "711377", "711304", "711302", "711303", "711297", "711296",
              "711293", "704396", "703155", "704394", "701859", "704242", "704221", "704111", "703210", "704674"]

f_2_tractate = [12259427, 12259428, 12259429, 12259430, 12259431, 12258190, 12260379, 12260416, 12260418, 12260420]
f_2_answer = [552139, 552140, 552139, 552137, 552135, 552106, 552117, 552146, 543667, 543666]

f_1_tractate = [12277487, 12277488, 12271784, 12271783, 12271782, 12272059, 12277488, 12277487, 12277435, 12277342,
                12277243]
f_1_answer = [544771, 544770, 544769, 544768, 544767, 544766, 544765, 552128, 552131, 552138, 552135]

group_id = 1

redis_client.hset(answer_group_redis_name, 1, json.dumps(f_1_answer))
redis_data = redis_client.hget(answer_group_redis_name, 1)
if redis_data:
    group_id_list = json.loads(redis_data, encoding="utf-8")
print(group_id_list)

redis_client.hset(answer_group_redis_name, 1, json.dumps(f_1_tractate))
redis_data = redis_client.hget(answer_group_redis_name, 1)
if redis_data:
    group_id_list = json.loads(redis_data, encoding="utf-8")
print(group_id_list)

# _------------------
#
redis_client.hset(answer_group_redis_name, 2, json.dumps(f_2_answer))
redis_data = redis_client.hget(answer_group_redis_name, 2)
if redis_data:
    group_id_list = json.loads(redis_data, encoding="utf-8")
print(group_id_list)

redis_client.hset(answer_group_redis_name, 2, json.dumps(f_2_tractate))
redis_data = redis_client.hget(answer_group_redis_name, 2)
if redis_data:
    group_id_list = json.loads(redis_data, encoding="utf-8")
print(group_id_list)

# # _------------------
#
redis_client.hset(answer_group_redis_name, 3, json.dumps(f_3_answer))
redis_data = redis_client.hget(answer_group_redis_name, 3)
if redis_data:
    group_id_list = json.loads(redis_data, encoding="utf-8")
print(group_id_list)

redis_client.hset(answer_group_redis_name, 3, json.dumps(f_3_tractate))
redis_data = redis_client.hget(answer_group_redis_name, 3)
if redis_data:
    group_id_list = json.loads(redis_data, encoding="utf-8")
print(group_id_list)

# # --------------------
redis_client.hset(answer_group_redis_name, 4, json.dumps(f_4_answer))
redis_data = redis_client.hget(answer_group_redis_name, 4)
if redis_data:
    group_id_list = json.loads(redis_data, encoding="utf-8")
print(group_id_list)

redis_client.hset(answer_group_redis_name, 4, json.dumps(f_4_tractate))
redis_data = redis_client.hget(answer_group_redis_name, 4)
if redis_data:
    group_id_list = json.loads(redis_data, encoding="utf-8")

print(group_id_list)

#
# # ---------------------
redis_client.hset(answer_group_redis_name, 5, json.dumps(f_5_answer))
redis_data = redis_client.hget(answer_group_redis_name, 5)
if redis_data:
    group_id_list = json.loads(redis_data, encoding="utf-8")
print(group_id_list)

redis_client.hset(answer_group_redis_name, 5, json.dumps(f_5_tractate))
redis_data = redis_client.hget(answer_group_redis_name, 5)
if redis_data:
    group_id_list = json.loads(redis_data, encoding="utf-8")
print(group_id_list)
