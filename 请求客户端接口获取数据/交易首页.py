"""

美购首页 精选feed 打散

"""
import requests
import urllib3

urllib3.disable_warnings()


class Test():

    def __init__(self):
        self.uri = "https://backend.igengmei.com"
        self.city = "xiamen"
        self.s = requests.session()
        self.offset = ""

    def FeedTest(self, nu):
        url = self.uri + "/api/service/home/feed"

        parm = {
            "tab_value": "service",
            "first_load": "0",
            "offset": self.offset,
            "app_name": "com.wanmeizhensuo.zhensuo",
            "version": "7.23.6",
            "platform": "android",
            "device_id": "865277037750070",
            "os_version": "9",
            "model": "VCE-AL00",
            "screen": "1080x2208",
            "lat": "40.000393",
            "lng": "116.487144",
            "channel": "huawei",
            "manufacturer": "HUAWEI",
            "uuid": "eb8d3838-bf0b-4f57-9caf-87d0e259698b",
            "android_device_id": "androidid_6678aa299bedb49a",
            "current_city_id": self.city
        }

        dataAll = self.s.get(url, params=parm, verify=False).json()
        servicesAll = dataAll['data']['services']

        hospitalAll = []
        for i in range(len(servicesAll)):
            hospitalAll.append(servicesAll[i]['id'])
        print("第{}页数据，机构名称: {}".format(nu + 1, hospitalAll))
        print(f'\033[1;30;41m===第%s页数据，重复机构名称: %s===\033[0m' % (nu + 1, set(hospitalAll)))

        self.offset = dataAll['data']['offset']


if __name__ == '__main__':
    app = Test()
    for i in range(100):
        app.FeedTest(i)
