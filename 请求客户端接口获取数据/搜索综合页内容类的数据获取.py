import requests
import urllib3


# from threading import Thread
#
# urllib3.disable_warnings()

class gengmei():

    def __init__(self):
        self.s = requests.session()
        self.uri = "https://backend.igengmei.com"
        self.offset = ""
        self.city = "changsha"
        self.version = "7.15.0"  # "7.15.2"
        self.device_id = "868080041007173"

    def GM_SSmeigou(self):
        """搜索美购"""
        url = self.uri + "/api/search/v2/service"
        body = {
            "q": "厚唇改薄",
            "input_type": "2",
            "offset": self.offset,
            "tag_ids": "",
            "is_gray": "1",
            "app_name": "com.wanmeizhensuo.zhensuo",
            "version": self.version,
            "platform": "android",
            "device_id": self.device_id,
            "os_version": "8.1.0",
            "model": "V1809T",
            "screen": "1080x2340",
            "lat": "40.00047",
            "lng": "116.487148",
            "channel": "benzhan",
            "current_city_id": self.city,
            "manufacturer": "vivo",
            "uuid": "efc40934-ef78-49e3-ad1b-5df072249289",
            "android_device_id": "androidid_233708112de9a151"
        }
        dataAll = self.s.get(url, params=body, verify=False).json()
        # print(dataAll)
        mgListAll = dataAll['data.txt']['services']
        # print(mgListAll)
        server_id = []  # 美购id
        service_name = []  # 美购名称
        for i in range(len(mgListAll)):
            server_id.append(mgListAll[i]['id'])
            service_name.append(mgListAll[i]['service_name'])
        print(server_id)

        self.offset = dataAll['data.txt']['offset']


if __name__ == '__main__':
    page = 0
    app = gengmei()

    for i in range(100):
        app.GM_SSmeigou()


###
# 5393226