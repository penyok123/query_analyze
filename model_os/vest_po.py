# import os
#
# sss = os.popen("ps -ef | grep 'auto_vest' ").readlines()
#
# all_items = []
# for item in sss:
#     # python manage.py trans2es_data2es_redis -S auto_vest
#     if 'trans2es_data2es_redis' in item:
#         for items in item.split(' '):
#             if items:
#                 all_items.append(items)
#         sss = os.popen('kill -9 ' + str(all_items[1]))
#     else:
#         pass

# os.popen('cd ~/Desktop/project/vest')
# os.popen('source ~/vest_gm/bin/activate')
# open_process = os.popen('nohup  python manage.py trans2es_data2es_redis -S auto_vest  &')
# print(open_process)


# 15 11 * * * cd /data/log/vest/app  && python vest_kill.py
# 8 11 * * * source ~/vest_gm/bin/activate && cd ~/Desktop/project/vest  && nohup  python manage.py trans2es_data2es_redis -S auto_vest & > /data/log/vest/app/kill.log

pks = [230221, 230222, 230223, 12, 13, 14, 15]
question_ids = [230221, 230222, 230223, 230224, 230225, 230255, 230256, 230257, 230323]
for question_id in question_ids:
    if question_id in pks:
        pks.remove(question_id)


print(pks)