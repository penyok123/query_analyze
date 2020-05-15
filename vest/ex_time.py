# import datetime
#
# #
# # date1 = '2018-01-19'
# # date2 = '2018-02-10'
# #
# # d1 = datetime.datetime.strptime(date1, '%Y-%m-%d')  # 将日期字符串转换成日期对象
# # d2 = datetime.datetime.strptime(date2, '%Y-%m-%d')  # 将日期字符串转换成日期对象
# # day = (d2 - d1).days
# #
# # print(day)
# #
# # now = datetime.datetime.now()
# #
# # print(now)
# #
# # strtime = now.strftime("%Y-%m-%d %H:%M:%S")
# #
# # print(strtime)
# #
# # yes_time = now - datetime.timedelta(hours=4)
# #
# # print(yes_time)
# #
# #
# # def time_conv(minutest, minutest2):
# #     try:
# #         now = datetime.datetime.now()
# #         yes_time = now - datetime.timedelta(minutes=minutest)
# #         yes_time2 = now - datetime.timedelta(minutes=minutest2)
# #         return yes_time, yes_time2
# #     except:
# #         return None
# #
# #
# # # python2 不兼容，python3正常
# # import datetime, random
# #
# #
# # def randomtimes(start, end, n, frmt="%Y-%m-%d"):
# #     stime = datetime.datetime.strptime(start, frmt)
# #     etime = datetime.datetime.strptime(end, frmt)
# #     return [random.random() * (etime - stime) + stime for _ in range(n)]
# #
# #
# # print(now)
# # strtime = now.strftime("%Y-%m-%d")
# # print(strtime)
# # yes_time = (now + datetime.timedelta(days=365)).strftime("%Y-%m-%d")
# # print(yes_time)
# # s = randomtimes(strtime, yes_time, 1)[0]
# # print(s)
# # coding:utf8
# # import time
# # import math
# #
# #
# # def changeTime(allTime):
# #     day = 24 * 60 * 60
# #     hour = 60 * 60
# #     min = 60
# #     if allTime < 60:
# #         return "%d sec" % math.ceil(allTime)
# #     elif allTime > day:
# #         days = divmod(allTime, day)
# #         return "%d days, %s" % (int(days[0]), changeTime(days[1]))
# #     elif allTime > hour:
# #         hours = divmod(allTime, hour)
# #         return '%d hours, %s' % (int(hours[0]), changeTime(hours[1]))
# #     else:
# #         mins = divmod(allTime, min)
# #         return "%d mins, %d sec" % (int(mins[0]), math.ceil(mins[1]))
# #
# #
# # if __name__ == "__main__":
# #     nums = 19778979
# #     t = time.time()
# #     data.txt = changeTime(nums)
# #     print(time.time() - t)
# #     print(data.txt)
#
# # import random
# # import time
# # from datetime import datetime
# #
# #
# # def strTimeProp(start, end, prop, frmt):
# #     stime = time.mktime(time.strptime(start, frmt))
# #     etime = time.mktime(time.strptime(end, frmt))
# #     ptime = stime + prop * (etime - stime)
# #     return int(ptime)
# #
# #
# # def randomTimestamp(start, end, frmt='%Y-%m-%d %H:%M:%S'):
# #     return strTimeProp(start, end, random.random(), frmt)
# #
# #
# # def randomDate(start, end, frmt='%Y-%m-%d %H:%M:%S'):
# #     return time.strftime(frmt, time.localtime(strTimeProp(start, end, random.random(), frmt)))
# #
# #
# # def randomTimestampList(start, end, n, frmt='%Y-%m-%d %H:%M:%S'):
# #     return [randomTimestamp(start, end, frmt) for _ in range(n)]
# #
# #
# # def randomDateList(start, end, n, frmt='%Y-%m-%d %H:%M:%S'):
# #     return [randomDate(start, end, frmt) for _ in range(n)]
#
#
# # nows = datetime.datetime.now()
# # strtime = nows.strftime("%Y-%m-%d %H:%M:%S")
# # print(strtime)
# # # yes_time = (now + datetime.timedelta(days=365)).strftime("%Y-%m-%d")
# # print(nows.hour)
# #
# # zeroday = str(datetime.datetime(nows.year, nows.month, nows.day + 13, 10, 0, 0))
# # lastday = str(datetime.datetime(nows.year, nows.month, nows.day, 23, 0, 0))
# # print(zeroday)
#
# # lenth = 10
# # print(randomTimestamp(start, end))
# # print(randomDate(start, end))
# # print(randomTimestampList(start, end, lenth))
# # print(randomDateList(start, end, lenth))
# # action_num = random.randint(0, 1)
# # print(action_num)
# date2 = "2019-02-28 18:40:03"
# d2 = datetime.datetime.strptime(date2, '%Y-%m-%d %H:%M:%S')
# date1 = "2019-02-24 18:40:03"
# d1 = datetime.datetime.strptime(date1, '%Y-%m-%d %H:%M:%S')
#
# print("------")
# print(d2)
#
# print(d1)
#
# print(d2 - d1)
# print((d2 - d1).days)
#
# print("-----")
# print(d2 + datetime.timedelta(days=1))
# # .strftime("%Y-%m-%d %H:%M:%S")
#
# # def chuli_time_follow(d2):
# #     # nows = datetime.datetime.now()
# #     nows = d2
# #     year = d2.year
# #     month = d2.month
# #     day = d2.day
# #
# #     if nows.month in (1, 3, 5, 7, 8, 10, 12):
# #         if nows.day >= 22:
# #             if nows.month == 12:
# #                 year = nows.year + 1
# #                 month = 1
# #                 day = 1
# #             else:
# #                 month = nows.month + 1
# #                 day += 10
# #
# #         else:
# #             day = nows.day + 10
# #
# #     elif nows.month in (4, 6, 9, 11):
# #         if nows.day >= 21:
# #             month = nows.month + 1
# #             day = 30 - nows.day
# #         else:
# #             day = nows.day + 10
# #
# #     else:
# #         if nows.day >= 19:
# #             month = nows.month + 1
# #             day = 10 - (28 - 24)
# #         else:
# #             day = nows.day + 10
# #
# #     return year, month, day
# #
# #
# # y, m, d = chuli_time(d2)
# # print(y)
# # print(m)
# # print(d)
# # def chuli_time():
# #     nows = datetime.datetime.now()
# #     year = nows.year
# #     month = nows.month
# #     day = nows.day
# #
# #     if nows.month in (1, 3, 5, 7, 8, 10, 12):
# #         if nows.day == 31:
# #             if nows.month == 12:
# #                 year = nows.year + 1
# #                 month = 1
# #                 day = 1
# #             else:
# #                 month = nows.month + 1
# #                 day = 1
# #
# #         else:
# #             day = nows.day + 1
# #     elif nows.month in (4, 6, 9, 11):
# #         if nows.day == 30:
# #             if nows.month == 12:
# #                 year = nows.year + 1
# #                 month = 1
# #                 day = 1
# #
# #             else:
# #                 month = nows.month + 1
# #                 day = 1
# #         else:
# #             day = nows.day + 1
# #
# #     else:
# #         if nows.day == 28:
# #             month = nows.month + 1
# #             day = 1
# #         else:
# #             day = nows.day + 1
# #
# #     return year, month, day
# print("=====")
# content_day_need_add_one_day = True
# now = datetime.datetime.now()
# print(now)
# if content_day_need_add_one_day == True:
#     nows = now
#     now = nows + datetime.timedelta(days=1)
#     print(nows)
# print(now)
#
# print("================")
# now = datetime.datetime.now()
# zeroday = datetime.datetime(now.year, now.month, now.day, 10, 0, 0)
# lastday = datetime.datetime(now.year, now.month, now.day, 23, 0, 0)
# print(zeroday.day)
# print(lastday.day)
# print(lastday)
# now = zeroday + datetime.timedelta(days=10)
# print(now)
# # def chuli_time_follow(d2):
# #     # nows = datetime.datetime.now()
# #     nows = d2
# #     year = d2.year
# #     month = d2.month
# #     day = d2.day
# #
# #     if nows.month in (1, 3, 5, 7, 8, 10, 12):
# #         if nows.day >= 22:
# #             if nows.month == 12:
# #                 year = nows.year + 1
# #                 month = 1
# #                 day = 1
# #             else:
# #                 month = nows.month + 1
# #                 day += 10
# #
# #         else:
# #             day = nows.day + 10
# #
# #     elif nows.month in (4, 6, 9, 11):
# #         if nows.day >= 21:
# #             month = nows.month + 1
# #             day = 30 - nows.day
# #         else:
# #             day = nows.day + 10
# #
# #     else:
# #         if nows.day >= 19:
# #             month = nows.month + 1
# #             day = 10 - (28 - 24)
# #         else:
# #             day = nows.day + 10
# #
# #     return year, month, day
#
#
# print("------------------------------")
# now = datetime.datetime.now()
# zeroday = datetime.datetime(now.year, now.month, now.day, 10, 0, 0)
# lastday = datetime.datetime(now.year, now.month, now.day, 23, 0, 0)
#
# start_time = zeroday + datetime.timedelta(days=10)
# end_time = lastday + datetime.timedelta(days=10)
#
# print(start_time)
# print(end_time)
#
# import random
# action_num = random.randint(0, 2)
# print(action_num)im


# import datetime
#
# create_time = '2019-12-29 22:17:09'
# datetime_create_time = datetime.datetime.strptime(create_time, '%Y-%m-%d %H:%M:%S')
#
# str_data = str(datetime_create_time.year) + str(datetime_create_time.month) + str(datetime_create_time.day)
# print(str_data)
# import datetime
#
# today = datetime.datetime.now()
# str_today = str(today.year) + str(today.month) + str(today.day)
# push_time = '2019-12-29 22:17:09'
# push_datetime = datetime.datetime.strptime(push_time, '%Y-%m-%d %H:%M:%S')
# print(push_datetime)
# str_push_datetime = str(push_datetime.year) + str(push_datetime.month) + str(push_datetime.day)
#
# print(str_push_datetime)
# print(str_today)
import datetime
import random
import time


def strTimeProp(start, end, prop, frmt):
    stime = time.mktime(time.strptime(start, frmt))
    etime = time.mktime(time.strptime(end, frmt))
    ptime = stime + prop * (etime - stime)
    return int(ptime)


def randomDate(create_time, frmt='%Y-%m-%d %H:%M:%S', action_type=None):
    if action_type in ("follow", "click"):
        action_num = random.randint(1, 3)

    if action_type == "comment":
        action_num = random.randint(1, 2)

    start = str(create_time + datetime.timedelta(minutes=30))
    end = str(create_time + datetime.timedelta(hours=2))

    random_times = [randomDate_six_one(start, end, frmt) for _ in range(action_num)]
    have_sort_times = sorted(random_times, key=lambda date: get_list(date))

    return have_sort_times


def randomDate_six_one(start, end, frmt='%Y-%m-%d %H:%M:%S'):
    return time.strftime(frmt, time.localtime(strTimeProp(start, end, random.random(), frmt)))


def get_list(date):
    return datetime.datetime.strptime(date, "%Y-%m-%d %H:%M:%S").timestamp()


def get_ten_last_days_random_time(num_days=None, frmt='%Y-%m-%d %H:%M:%S', content_level=0,
                                  content_day_need_add_one_day=False, action_type=None, repeat_time=1):
    try:
        all_time_list = []
        if num_days == None:
            return []
        ##比较当前时间和最后一次创建时间的差
        now = datetime.datetime.now()
        zeroday = datetime.datetime(now.year, now.month, now.day, 9, 0, 0)

        add_number = 0
        if num_days > 15 and action_type in ("follow", "click"):
            action_num = random.randint(1, 2)
            add_number = 3

        elif num_days > 6 and action_type in ("comment"):
            if content_level <= 3:
                action_num = 1
                add_number = 3
            else:
                action_num = random.randint(1, 2)
                add_number = 3

        else:
            pass
        start_time = zeroday + datetime.timedelta(days=add_number)
        ##第一个时间段
        zeroday1 = str(datetime.datetime(start_time.year, start_time.month, start_time.day, 9, 0, 0))
        lastday1 = str(datetime.datetime(start_time.year, start_time.month, start_time.day, 10, 59, 59))
        random_times = [randomDate_six_one(zeroday1, lastday1, frmt) for _ in range(action_num)]
        have_sort_times1 = sorted(random_times, key=lambda date: get_list(date))

        ##第二个时间段
        zeroday2 = str(datetime.datetime(start_time.year, start_time.month, start_time.day, 12, 0, 0))
        lastday2 = str(datetime.datetime(start_time.year, start_time.month, start_time.day, 14, 59, 59))
        random_times = [randomDate_six_one(zeroday2, lastday2, frmt) for _ in range(action_num)]
        have_sort_times2 = sorted(random_times, key=lambda date: get_list(date))

        ##第三个时间段
        zeroday3 = str(datetime.datetime(start_time.year, start_time.month, start_time.day, 20, 0, 0))
        lastday3 = str(datetime.datetime(start_time.year, start_time.month, start_time.day, 23, 59, 59))
        random_times = [randomDate_six_one(zeroday3, lastday3, frmt) for _ in range(action_num)]
        have_sort_times3 = sorted(random_times, key=lambda date: get_list(date))

        all_time_list.extend(have_sort_times1)
        all_time_list.extend(have_sort_times2)
        all_time_list.extend(have_sort_times3)

        # if content_day_need_add_one_day == True:
        #     start_time = zeroday + datetime.timedelta(days=add_number * repeat_time)
        #     end_time = lastday + datetime.timedelta(days=add_number * repeat_time)
        #
        # else:
        #     start_time = zeroday + datetime.timedelta(days=add_number)
        #     end_time = lastday + datetime.timedelta(days=add_number)

        # random_times = [randomDate_six_one(str(start_time), str(end_time), frmt) for _ in range(action_num)]
        # have_sort_times = sorted(random_times, key=lambda date: get_list(date))

        return all_time_list
    except:
        return []


def get_one_six_days_random_time(frmt='%Y-%m-%d %H:%M:%S', num_days=0, action_type=None, content_level=0,
                                 content_day_need_add_one_day=False):
    try:
        action_num = 0
        all_time_list = []
        ##follow 发布后1天 3：1-2  4：5-10
        ##
        if num_days == 1 and action_type in ("follow", "click") and int(content_level) < 3:
            action_num = random.randint(1, 2)

        if num_days == 1 and action_type in ("follow") and int(content_level) >= 3:
            action_num = random.randint(5, 10)

        if num_days == 1 and action_type in ("click") and int(content_level) >= 3:
            action_num = random.randint(6, 12)

        if num_days <= 15 and num_days > 1 and action_type in ("follow", "click") and int(content_level) < 3:
            action_num = random.randint(1, 2)

        if num_days <= 15 and num_days > 1 and action_type in ("follow") and int(content_level) >= 3:
            action_num = random.randint(1, 5)

        if num_days <= 15 and num_days > 1 and action_type in ("click") and int(content_level) >= 3:
            action_num = random.randint(1, 6)

        if num_days >= 1 and num_days <= 6 and action_type in ("comment"):
            if int(content_level) <= 3:
                action_num = random.randint(2, 4)
            else:
                action_num = random.randint(3, 4)

        now = datetime.datetime.now()
        if content_day_need_add_one_day == True:
            nows = now
            now = nows + datetime.timedelta(days=1)

        ##第一个时间段
        zeroday = str(datetime.datetime(now.year, now.month, now.day, 9, 0, 0))
        lastday = str(datetime.datetime(now.year, now.month, now.day, 10, 59, 59))
        random_times = [randomDate_six_one(zeroday, lastday, frmt) for _ in range(action_num)]
        have_sort_times1 = sorted(random_times, key=lambda date: get_list(date))

        ##第二个时间段
        zeroday = str(datetime.datetime(now.year, now.month, now.day, 12, 0, 0))
        lastday = str(datetime.datetime(now.year, now.month, now.day, 14, 59, 59))
        random_times = [randomDate_six_one(zeroday, lastday, frmt) for _ in range(action_num)]
        have_sort_times2 = sorted(random_times, key=lambda date: get_list(date))

        ##第三个时间段
        zeroday = str(datetime.datetime(now.year, now.month, now.day, 20, 0, 0))
        lastday = str(datetime.datetime(now.year, now.month, now.day, 23, 59, 59))
        random_times = [randomDate_six_one(zeroday, lastday, frmt) for _ in range(action_num)]
        have_sort_times3 = sorted(random_times, key=lambda date: get_list(date))

        all_time_list.extend(have_sort_times1)
        all_time_list.extend(have_sort_times2)
        all_time_list.extend(have_sort_times3)
        return all_time_list
    except:
        return []


all_time_list = get_ten_last_days_random_time(num_days=10, action_type='comment')
print(all_time_list)
