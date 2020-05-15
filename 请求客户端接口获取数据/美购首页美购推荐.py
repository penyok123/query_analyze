"""
1、拿到画像的tag_id 、及对应id 的分值
2、a = count(len(tag_id))
3、100% / a
4、获取 美购列表 热门推荐的接口， 获取每个美购的id
5、es 搜索 该id  是否有cpc、是否在线、拿到对应的tag_id 并判断是否在画像的tag_id中
6、打印 美购id+tag_id+位置+cpc状态+是否在线
"""
import requests


class Test():

    def __init__(self):
        self.s = requests.session()
        self.uri = "https://backend.igengmei.com"  # "http://backend.paas.env"  "https://backend.igengmei.com"
        self.city = "xiamen"
        self.device = "867961030707205"
        self.offset = ""

    def meigou_re(self):
        url = self.uri + "/api/service/home/v3"

        param = {
            "first_load": "1",
            "offset": self.offset,
            "app_name": "com.wanmeizhensuo.zhensuo",
            "version": "7.16.1",
            "platform": "android",
            "device_id": self.device,
            "os_version": "8.1.0",
            "model": "V1809T",
            "screen": "1080x2340",
            "lat": "40.000485",
            "lng": "116.487086",
            "channel": "benzhan",
            "manufacturer": "vivo",
            "uuid": "231286b4-2544-449e-95f2-7e1a7bc0867f",
            "android_device_id": "androidid_233708112de9a151",
            "current_city_id": self.city
        }

        dataAll = self.s.get(url, params=param, verify=False).json()['data.txt']
        servicesALL = dataAll['services']

        serviceId = []
        for i in range(len(servicesALL)):
            serviceId.append(servicesALL[i]['id'])
        self.offset = dataAll['offset']
        print(self.offset)
        print(serviceId)
        # self.offset = dataAll['data.txt']['offset']
        return serviceId


if __name__ == '__main__':
    tag = [1, 47, 22]

    app = Test()

    for i in range(5000):
        app.meigou_re()
    # id = app.meigou_re()
    # closure_tag_ids = []
    # for i in id:
    #     a, b, c = app.search(i)
    #     closure_tag_ids.append(b)
    #     print("美购id ：{}, is_online: {}, closure_tag_ids:{}, is_promote:{}".format(i, a, b, c))
    #
    # print(closure_tag_ids)
    # for cl in closure_tag_ids:
    #     for tg in tag:
    #         if tg in cl:
    #             print(tg)
    #             pass
    #         else:
    #             print(f'\033[1;30;41m===%s===\033[0m' % cl)

