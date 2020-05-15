from collections import deque, OrderedDict
import unittest, random
import itertools
import functools

GROUP_SIZE = 80


def variousness(items, variety_size):
    src = deque(items)
    dst = []
    while len(src) > 0:
        pos, temp, recover, dup = 0, [], [], []
        while pos < variety_size:
            try:
                item = src.popleft()
                if item.get("group") in dup:
                    recover.append(item)
                else:
                    temp.append(item)
                    dup.append(item.get("group"))
                    pos = pos + 1
            except IndexError:
                diff = variety_size - pos
                diff, remain = recover[:diff], recover[diff:]
                temp.extend(diff)
                recover = remain
                break

        multi = OrderedDict()
        for key in dup:
            multi[key] = []
        for item in temp:
            multi[item.get("group")].append(item)
        temp = filter(lambda a: a != None, itertools.chain.from_iterable(itertools.zip_longest(*multi.values())))

        dst.extend(temp)
        src.extendleft(reversed(recover))

    return dst


def region_division(items, current_city):
    in_city_white_list = True
    city, nearby, other = [], [], []
    for item in items:
        if current_city == item.get("city"):
            city.append(item)
        elif current_city in item.get("nearby"):
            nearby.append(item)
        else:
            other.append(item)
    # if in_city_white_list:
    #     return [city, nearby, other]
    return [city + nearby, other]


# service_ids = [5833119, 5815944, 5851491, 5831712, 5833120, 5833117, 5833115, 5844404, 5836780, 5833113, 5833340,
#                5815961, 5851482, 5772257, 5834024, 5841637, 5840532, 5840462, 5815954, 5815948, 5833673, 5866249,
#                5857867, 5814058, 5848164, 5866247, 5840916, 5866246, 5833126, 5833124, 5866245, 5865783, 5782445,
#                5866243, 5866241, 5866240, 5866239, 5866139, 5866138, 5866137, 5846473, 5757748, 5851472, 5841032,
#                5756634, 5840534, 5765099, 5814927, 5830182, 5846472, 5850565, 5850904, 5764203, 5851524, 5845506,
#                5850906, 5831667, 5850981, 5762077, 5856983, 5857000, 5851473, 5775966, 5781149, 5831666, 5852461,
#                5754049, 5841304, 5833167, 5756617, 5757675, 5850868, 5857178, 5851477, 5834430, 5850953, 5754050,
#                5853286, 5832153, 5782735]
doctor_ids = ["59a41df6bb6547e39f9e1fe360ea6f92", "01764e5a49ec48c7b90437d4a915badf",
              "59a41df6bb6547e39f9e1fe360ea6f92",
              "ecfdd59b5e8a482594119acf51c6c799", "3505628dace74e408066919df4990128",
              "59a41df6bb6547e39f9e1fe360ea6f92",
              "9918ad7eb8f511e58f8200163e000a4a", "c649d17ebe6e4e5cbc2592671d48b535",
              "34d7c13f2cb045f3891dcf85f5f43ba0", "db1ea0c2b84e11e5aeb000163e000a4a",
              "8902e50ba18d45ca993518b86341e336", "11a5011bb8a54ae6bef5f0c790d49d28",
              "3e00f028f81d11e6af9e00163e0051d4", "8ff6d6a58e5b4cc18272b8324188ba19",
              "9734add0e897442bad7d56bde527df20", "d46a39c1f7814b638e0955b1f3020510",
              "6ec247882dc749bfb5762442c448436d", "5bd9f05cad51403d853ba8c881989e23",
              "59a41df6bb6547e39f9e1fe360ea6f92", "3e00f028f81d11e6af9e00163e0051d4",
              "59a41df6bb6547e39f9e1fe360ea6f92"]

division_skus = []
for item in doctor_ids:
    division_skus.append({"group": item, 'city': 328})

variousness_per_10 = functools.partial(variousness, variety_size=10)
sss = region_division(division_skus, 328)
division_reranks = map(variousness_per_10, sss)
# print(division_reranks)
sku_rerank = [sku for skus in division_reranks for sku in skus]
doctor_ids = [sku['group'] for sku in sku_rerank]
print(doctor_ids)
