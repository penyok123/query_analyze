data = {
    'a_b_h': 1,
    'a_b_i': 2,
    'a_c_j': 3,
    'a_d': 4,
    'a_c_k': 5,
    'a_e': 6
}

new_data = {
    'a': {
        'b': {
            'h': 1,
            'i': 2
        },
        'c': {
            'j': 3,
            'k': 5
        },
        'd': 4,
        'e': 6
    }
}

# new_data = {}
# tmp = {}
# new_data['a'] = tmp
# print(new_data)  # {'a': {}}
# tmp['b'] = 1
# print(new_data)  # {'a': {'b': 1}}
#
# data = {
#     'a_b_h': 1,
#     'a_b_i': 2,
#     'a_c_j': 3,
#     'a_d': 4,
#     'a_c_k': 5,
#     'a_e': 6
# }
#
# new_data = {}
#
# for key, value in data.items():
#     keys = key.split('_')
#     tmp = new_data
#     last = len(keys) - 1  # 最后一个 key 的索引值
#     for i, k in enumerate(keys):
#         print(k)
#         print(i)
#         print("----")
#         if i == last:
#             tmp[k] = value
#             continue
#         if k not in tmp:
#             sub_tmp = {}
#             tmp[k] = sub_tmp
#             tmp = sub_tmp
#         else:
#             tmp = tmp[k]
#             print(tmp)
#
# print(new_data)

##enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中。


for field, value in data.items():
    keys = field.split('_')
    tmp = new_data
    for k in keys[:-1]:
        tmp = tmp.setdefault(k, {})
        print(tmp)
    tmp[keys[-1]] = value

print(new_data)