# # coding=utf-8
# import redis, datetime
#
# # date = datetime.datetime.now().date() - datetime.timedelta(days=1)
# # sql = 'select keywords,sum(sorted) as nums  from api_search_words where is_delete = 0 and create_time =' + str(
# #     date) + ' group by keywords  order by  nums  desc'
# #
# # print(sql)
# # REDIS_URL = 'redis://:ReDis!GmTx*0aN6@172.16.40.133:6379'
# # REDIS_URL = 'redis://:ReDis!GmTx*0aN9@172.16.40.173:6379'
# REDIS_URL = "redis://redis.paas-test.env:6379/0"
# redis_client = redis.StrictRedis.from_url(REDIS_URL)
#
# user_service_portrait_tags_key = "user:service_portrait_tags3:cl_id:" + str(865277037750070)
#
# tag = ["北京"]
# for item in tag:
#     redis_client.hset(user_service_portrait_tags_key, item, 100222000)
#
# s = redis_client.hgetall(user_service_portrait_tags_key)
# print(s)
# # if redis_client.exists(user_service_portrait_tags_key):
# #     user_portrait_redis = redis_client.hgetall(user_service_portrait_tags_key)
# #
# # else:
# #     new_user_service_portrait_tags_key = "user:service_coldstart_tags3"
# #     user_portrait_redis = redis_client.hgetall(new_user_service_portrait_tags_key)
# #
# # print(user_portrait_redis)
#
# # ------------------------------------------------------------------------------------------------------------------------------
#
# # user_portrait = [{"tag_score": float(score), "tag_name": tag} for tag, score in
# #                  user_portrait_redis.items()]
# # #
# # user_portrait_desc = sorted(user_portrait, key=lambda k: (k.get('tag_score', 0)), reverse=True)[:10]
# # user_portrait_tag_list = [str(item.get("tag_name", None), encoding="utf8") for item in user_portrait_desc]
# # print(user_portrait_tag_list)
#
# # ------------------------------------------------------------------------------------------------------------------------------
# # query_dict = {}
# # data = open('word', "r", encoding="utf-8")
# #
# # for item in data.readlines():
# #     word = item.strip().split('\t')[0]
# #     num = item.strip().split('\t')[1]
# #     # print(num)
# #     query_dict[word] = int(num)
# #
# # # print(query_dict)
# # key = "search_tips_save_query_word"
# #
# # redis_client.set(key, json.dumps(query_dict))
# #
# # data = redis_client.get(key)
# # if data:
# #     redis_data = json.loads(data)
# #
# # print(redis_data)
# #
# #
# # for key,value in query_dict.items():
# #     print(key)
# # ------------------------------------------------------------------------------------------------------------------------------
#
#
# # multi_fields = {
# #     'hospital.name': 3,
# #     'hospital.officer_name': 3,
# #     'service_closure_tags': 3
# # }
# # fields = ['^'.join((k, str(v))) for (k, v) in multi_fields.items()]
# # print(fields)
#
# #
#
# #
# # tag_name_key2 = "user_click_search_query_to_service_tab:device_id:" + str(867961035707277)
# # tag_names_list = ["隆鼻", "玻尿酸"]
# # days = datetime.datetime.now()
# # month = str(days.month)
# # day = str(days.day)
# #
# # if days.month < 10:
# #     month = "0" + str(days.month)
# # if days.day < 10:
# #     day = "0" + str(days.day)
# # #
# # date = str(days.year) + month + str(int(day) + 2)
# # print(date)
# # have_save_data = redis_client.hgetall(tag_name_key2)
# # today_save_data = redis_client.hget(tag_name_key2, date)
# #
# # # print(have_save_data)
# #
# # for item in have_save_data:
# #     print(item)
# # ------------0-----------------------------------
# # all_data = {}
# # for item in tag_names_list:
# #     if item in all_data:
# #         all_data[item] += 1
# #     else:
# #         all_data[item] = 1
# #
# # if have_save_data and today_save_data:
# #
# #     have_save_data_sort = sorted(have_save_data.items(), reverse=True)[1:7]
# #     for item in have_save_data_sort:
# #         for key, value in json.loads(item[1]).items():
# #             if key in all_data:
# #                 all_data[key] += value
# #             else:
# #                 all_data[key] = value
# #         redis_client.hset(tag_name_key2, json.loads(item[0]), json.dumps(json.loads(item[1])))
# #
# #     today_save_data = json.loads(today_save_data)
# #     for item in tag_names_list:
# #         if today_save_data.get(item, None):
# #             today_save_data[item] += 1
# #         else:
# #             today_save_data[item] = 1
# #     redis_client.hset(tag_name_key2, date, json.dumps(today_save_data))
# #
# # else:
# #     json_data = {}
# #     for item in tag_names_list:
# #         json_data[item] = 1
# #     redis_client.hset(tag_name_key2, date, json.dumps(json_data))
# #     today_save_data = json_data
# #
# #     have_save_data_sort = sorted(have_save_data.items(), reverse=True)[0:7]
# #     for item in have_save_data_sort:
# #         for key, value in json.loads(item[1]).items():
# #             if key in all_data:
# #                 all_data[key] += value
# #             else:
# #                 all_data[key] = value
# #
# #         redis_client.hset(tag_name_key2, json.loads(item[0]), json.dumps(json.loads(item[1])))
# #
# # #
# #
# # have_save_data = redis_client.hgetall(tag_name_key2)
# #
# # sss = {}
# # fff = []
# # for item, value in have_save_data.items():
# #     if item != b"all":
# #         dict_val = json.loads(value)
# #         for tem in dict_val:
# #             if tem not in sss:
# #                 sss[tem] = int(item)
# #             else:
# #                 new_time = sss[tem]
# #                 if new_time < int(item):
# #                     sss[tem] = int(item)
# #
# # for item, vale in all_data.items():
# #     fff.append([item, vale, sss.get(item)])
# #
# # fff.sort(key=lambda x: x[1], reverse=True)
# #
# # all_data = {}
# # for item in fff:
# #     all_data[item[0]] = item[1]
# #
# #
# # redis_client.hset(tag_name_key2, "all", json.dumps(all_data))
# # +++++++++++#
#
# # ss = redis_client.hget(tag_name_key2, "all")
# # ss = json.loads(ss)
# # print(ss)
# # sss = sorted(ss.items(), key=lambda item: item[1], reverse=True)
# # print(sss)
# # print(have_save_data_sort)
# # print(today_save_data)
# # print(have_save_data_sort.extend(json.dumps(today_save_data)))
# # search_query = "水光针"
# # sql_get_tagid = "select  name from api_tag where  name =  '%s'" % (search_query)
# # print(sql_get_tagid)
#
# # primary_tag_name_list = ["水光针", '隆鼻']
# # service_closure_tags = ["水光针", "玻尿酸"]
# #
# # tag_name = ""
# # for tag in service_closure_tags:
# #     if tag in primary_tag_name_list:
# #         print(tag)
# #         tag_name = tag
# #         break
#
#
# # tag_name_key = "user_click_search_query_to_service_tab:device_id:" + str(123456)
# # data = redis_client.hget(tag_name_key, "all")
# # list_tag_name = list()
# # history_keywords = list()
# # if data is not None:
# #     list_tag_name = json.loads(data)
# #     list_tag_name = sorted(list_tag_name.items(), key=lambda item: item[1], reverse=True)
# #     list_tag_name = list_tag_name[:6]
# #     for item in list_tag_name:
# #         history_keywords.append(item[0])
# #
# # print(history_keywords)
# # if len(hera_all_keywords) + len(history_keywords) == 6:
# # def recommed_service_category_device_id(device_id):
# #     try:
# #         '''
# #         设备品类显示, 是否命中灰度
# #         '''
# #         categroy_select_cary1 = ["0", "1", "2", "3", "c", "d", "e", "f"]
# #         categroy_select_cary2 = ["4", "5", "6", "a"]
# #         categroy_select_cary3 = ["9", "8", "7", "b"]
# #
# #         if not device_id:
# #             return 1
# #
# #         hd_id = hashlib.md5(str(device_id).encode()).hexdigest()
# #         is_gray = hd_id[-1]
# #
# #         if is_gray in categroy_select_cary2:
# #             return 2
# #         elif is_gray in categroy_select_cary3:
# #             return 3
# #         else:
# #             return 1
# #     except:
# #         return 1
# #
# #
# # ss = recommed_service_category_device_id(device_id="123456KK")
# # print(ss)
#
# # 123456LMMM  3
# # 123456KK  2
# # 123456L 1
#
# # ss= [{'answer_num': 1, 'search_num': 100, 'tractate_num': 2, 'diary_num': 2}]
# #
# # print(ss[0])
# #
# # for item in ss[0].values():
# #     print(item)
# # ______________________________________________
# # ss = [{'id': 375, 'keyword': '666', 'jump_target': '', 'jump_type': '14'},
# #       {'id': 316, 'keyword': '812秒杀专场', 'jump_target': '812', 'jump_type': '15'},
# #       {'id': 315, 'keyword': '99秒杀聚合', 'jump_target': '99', 'jump_type': '16'},
# #       {'id': 313, 'keyword': '99秒杀聚合', 'jump_target': '99', 'jump_type': '16'},
# #       {'id': 313, 'keyword': '99秒杀聚合', 'jump_target': '99', 'jump_type': '16'},
# #       {'id': 313, 'keyword': '99秒杀聚合', 'jump_target': '99', 'jump_type': '16'},
# #       {'id': 310, 'keyword': '秒杀聚合--搜索词', 'jump_target': '104', 'jump_type': '16'},
# #       {'id': 309, 'keyword': '秒杀专场--搜索词', 'jump_target': '909', 'jump_type': '15'}]
# #
# # all_data = []
# # diff_keyword = list()
# #
# # for item in ss:
# #
# #     print(item)
# #     if item.get("keyword", None) not in diff_keyword:
# #         print("======")
# #         print(item)
# #         diff_keyword.append(item.get("keyword", None))
# #     else:
# #         ss.remove(item)
# #         print("----")
# #         print(item)
# #
# # print(ss)
# # print(diff_keyword)
#
#
# # def save_query_to_redis(query, from_type=None):
# #     lower_query = str(query).lower()
# #     key = "save_query_to_redis"
# #     redis_data = redis_client.hget(key, lower_query)
# #
# #     if from_type == "search_query":
# #         order_weight = 10
# #         search_num = 10
# #     else:
# #         order_weight = 100
# #         search_num = 100
# #
# #     if redis_data:
# #         json_data = json.loads(redis_data)
# #         have_save_order_weight = json_data.get('order_weight', 0)
# #         have_save_search_num = json_data.get('order_weight', 0)
# #
# #         if have_save_order_weight < order_weight:
# #             redis_client.hset(key, lower_query,
# #                               json.dumps({"order_weight": order_weight, "search_num": search_num}))
# #             return True
# #
# #         elif redis_data == order_weight:
# #             if have_save_search_num < search_num:
# #                 redis_client.hset(key, lower_query,
# #                                   json.dumps({"order_weight": order_weight, "search_num": search_num}))
# #                 return True
# #             else:
# #                 return False
# #         else:
# #             return False
# #     else:
# #         redis_client.hset(key, lower_query,
# #                           json.dumps({"order_weight": order_weight, "search_num": search_num}))
# #
# #         return True
# #
# #
# # query = ",水)光,针."
# # sub_query = re.sub('\W+', '', query)
# # print(sub_query)
# #
# #
# # ss = save_query_to_redis(query=query, from_type="wiki")
# # print(ss)
#
# #
# # ss = max([1, 2, 3, 4, 5])
# # print(ss)
# # ss = "鼻部,眼部,吸脂"
# # sss = [ss.split(",")]
# # print(sss)
# ###---------------------------------###
# import pymysql
# #
# # cursor = pymysql.connect(host='bj-cdb-6slgqwlc.sql.tencentcdb.com', user='work', password='Gengmei1', port=62120,
# #                          db='diagnosis', charset='utf8', cursorclass=pymysql.cursors.DictCursor)
# #
# # cursor = pymysql.connect(host='mysql-service', user='work', password='Gengmei1', port=3306,
# #                          db='diagnosis', charset='utf8', cursorclass=pymysql.cursors.DictCursor)
# # #
# #
# # zhengxing_cursor = cursor.cursor()
# # data = {
# #     'id': '1',
# #     "create_time": None,
# #     "first_consultation_time": None,
# #     "is_banned": 1,
# #     "banned_time": None,
# #     "type": 1,
# #     "merchant_id": 1,
# #     "user_id": 1,
# #     'doctor_id': 'zhanggaoxin',
# #     "status": 1,
# #     "is_assistant": 0,
# #     'good_at': "",
# #     "record_id": None
# # }
# # table = 'consultation_counsellor'
# # keys = ', '.join(data.keys())
# # values = ', '.join(['%s'] * 13)
# # sql = 'insert into consultation_counsellor  values ({values})'.format(table=table, keys=keys, values=values)
# # print(sql)
# # try:
# #
# #     zhengxing_cursor.execute(sql, tuple(data.values()))
# #     print('Successful')
# #     cursor.commit()
# # except:
# #     print('Failed')
# #     zhengxing_cursor.rollback()
# #     zhengxing_cursor.close()
# #
# # zhengxing_cursor.close()
#
#
# # first_demands_name_list = []
# # second_demands_name_list = []
# # first_solutions_name_list = []
# # second_solutions_name_list = []
# # first_positions_name_list = []
# # second_positions_name_list = []
# # first_classify_name_list = []
# # second_classify_name_list = []
#
# # ##如果当前词是项目词
# # judge_tagv3_info = list(TagV3.objects.filter(name=query, is_online=True).values("tag_type", "id"))
# # if judge_tagv3_info:
# #     id = judge_tagv3_info[0].get("id")
# #     tag_type = judge_tagv3_info[0].get("tag_type", None)
# #     relation_tagids = list(
# #         TagV3MapAttrTag.objects.filter(tag_id=id, is_online=True).values_list("tag_attr_id", flat=True))
# #     attr_tagv3_info = list(
# #         AttrTag.objects.filter(id__in=relation_tagids, is_online=True).values("name", "aggregate_type"))
# #     for item in attr_tagv3_info:
# #         aggregate_type = item.get("aggregate_type", None)
# #         name = item.get('name', None)
# #         if aggregate_type == 7:
# #             first_demands_name_list.append(name)
# #         if aggregate_type == 8:
# #             second_demands_name_list.append(name)
# #         if aggregate_type == 10:
# #             first_positions_name_list.append(name)
# #         if aggregate_type == 3:
# #             second_positions_name_list.append(name)
# #         if aggregate_type == 6:
# #             first_solutions_name_list.append(name)
# #         if aggregate_type == 2:
# #             second_solutions_name_list.append(name)
# #
# # else:


sss = ["水光针", "玻尿酸", "水光针", "玻尿酸", "水光针", "玻尿酸"]

print(list(set(sss)))
