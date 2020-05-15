# import os
# import random
#
# crotab_list = [
#     "0 9 * * *  source /srv/envs/physical/bin/activate  && python /data.txt/log/physical/app/crontab.py",
#     "10 9 * * *  source /srv/envs/physical/bin/activate  && python  /data.txt/log/physical/app/crontabs.py",
#     "0 9 * * * sh /data.txt/log/cybertron/app/statistics_query.sh > /data.txt/log/cybertron/app/statistics_query.log",
#     "*/5 * * * * source /srv/envs/physical/bin/activate  && cd /srv/apps/physical && python manage.py  trans2es_mapping2es -m true_click_one",
#     "02,12,22,32,42,52  * * * *   source /srv/envs/physical/bin/activate  && cd /srv/apps/physical &&  python manage.py  trans2es_mapping2es -m true_click_two",
#     "00,10,20,30,40,50  * * * *  source /srv/envs/physical/bin/activate  && cd /srv/apps/physical &&  python manage.py  trans2es_mapping2es -m true_click_three",
#     "02,12,22,32,42,52  * * * *   source /srv/envs/physical/bin/activate  && cd /srv/apps/physical &&  python manage.py  trans2es_mapping2es -m true_click_four",
#     "06,16,26,36,46,56  * * * *  source /srv/envs/physical/bin/activate  && cd /srv/apps/physical &&  python manage.py  trans2es_mapping2es -m true_click_five",
#     "0 14 * * * source /srv/envs/physical/bin/activate  && cd /srv/apps/physical && python manage.py  trans2es_mapping2es -m auto_star_urge",
#     "0 10 * * * source /srv/envs/physical/bin/activate  && cd /srv/apps/physical && python manage.py  trans2es_mapping2es -m auto_urge1",
#     "30 10 * * * source /srv/envs/physical/bin/activate  && cd /srv/apps/physical && python manage.py  trans2es_mapping2es -m auto_urge2",
#     "0   10 * * 3 source /srv/envs/physical/bin/activate  && cd /srv/apps/physical && python manage.py  trans2es_mapping2es -m auto_lunch_app",
#     "30  10 * * 3 source /srv/envs/physical/bin/activate  && cd /srv/apps/physical && python manage.py  trans2es_mapping2es -m auto_lunch_app2",
#     "0  10 * * *  source /srv/envs/physical/bin/activate  && cd /srv/apps/physical && python manage.py  trans2es_mapping2es -m auto_follow",
#     "30 10  * * *  source /srv/envs/physical/bin/activate  && cd /srv/apps/physical && python manage.py  trans2es_mapping2es -m auto_follow2",
#     "00 11 * * 1  source /srv/envs/physical/bin/activate  && cd /srv/apps/physical && python manage.py  trans2es_mapping2es -m auto_follow_new",
#     "0 9  * * *  source /srv/envs/physical/bin/activate  && cd /srv/apps/physical &&   python manage.py  trans2es_mapping2es -m  get_login_session",
#     "0 0  * * 3  source /srv/envs/physical/bin/activate  && cd /srv/apps/physical &&  python manage.py  trans2es_mapping2es -m  get_user_id",
#     "*  14,18,22 *  *  *  source /srv/envs/physical/bin/activate  && cd /srv/apps/physical &&  python manage.py  trans2es_mapping2es -m  principal_online_comment1"
#
# ]
#
# crontab_list = [
#     "* * * source /srv/envs/physical/bin/activate  && cd /srv/apps/physical && python manage.py  trans2es_mapping2es -m answer_reply1",
#     "* * * source /srv/envs/physical/bin/activate  && cd /srv/apps/physical && python manage.py  trans2es_mapping2es -m answer_reply2",
#     "* * * source /srv/envs/physical/bin/activate  && cd /srv/apps/physical && python manage.py  trans2es_mapping2es -m answer_reply3",
#     "* * * source /srv/envs/physical/bin/activate  && cd /srv/apps/physical && python manage.py  trans2es_mapping2es -m answer_reply5",
#     "* * * source /srv/envs/physical/bin/activate  && cd /srv/apps/physical && python manage.py  trans2es_mapping2es -m answer_reply7",
#     "* * * source /srv/envs/physical/bin/activate  && cd /srv/apps/physical && python manage.py  trans2es_mapping2es -m yesterday_topic_reply",
#     "* * * source /srv/envs/physical/bin/activate  && cd /srv/apps/physical && python manage.py  trans2es_mapping2es -m before_yesterday_topic_reply",
#     "* * * source /srv/envs/physical/bin/activate  && cd /srv/apps/physical && python manage.py  trans2es_mapping2es -m three_days_ago_topic_reply",
#     "* * * source /srv/envs/physical/bin/activate  && cd /srv/apps/physical && python manage.py  trans2es_mapping2es -m five_days_ago_topic_reply",
#     "* * * source /srv/envs/physical/bin/activate  && cd /srv/apps/physical && python manage.py  trans2es_mapping2es -m seven_days_ago_reply"]
#
# reply_comment = [
#     "* * * source /srv/envs/physical/bin/activate  && cd /srv/apps/physical && python manage.py  trans2es_mapping2es -m reply_comment1",
#     "* * * source /srv/envs/physical/bin/activate  && cd /srv/apps/physical && python manage.py  trans2es_mapping2es -m reply_comment3",
#     "* * * source /srv/envs/physical/bin/activate  && cd /srv/apps/physical && python manage.py  trans2es_mapping2es -m reply_comment2",
#     "* * * source /srv/envs/physical/bin/activate  && cd /srv/apps/physical && python manage.py  trans2es_mapping2es -m reply_comment5",
#     "* * * source /srv/envs/physical/bin/activate  && cd /srv/apps/physical && python manage.py  trans2es_mapping2es -m reply_comment7"]
#
# ###随机生成10-23的一个数字 代表小时
# ss1 = random.choices(range(10, 23), k=10, weights=range(10, 23))
# ###随机生成1-60的一个数字  表示分钟
# ss2 = random.choices(range(1, 50), k=10, weights=range(1, 50))
# crontablist = []
# reply_comment_list = []
# for i in range(10):
#     crontablist.append(str(ss2[i]) + " " + str(ss1[i]) + " " + str(crontab_list[i]))
#     if i < 5:
#         reply_comment_list.append(str(ss2[i] + 5) + " " + str(ss1[i]) + " " + str(reply_comment[i]))
#
# all_data = []
# all_data.extend(crotab_list)
# all_data.extend(crontablist)
# all_data.extend(reply_comment_list)
#
# data.txt = open("/data.txt/log/physical/app/conf", "w")
# for var in all_data:
#     data.txt.write(var)
#     data.txt.write("\n")


import random
random_num = random.randint(0, 2)

for i in range(random_num):
    print(random_num)
    print("--------")