import requests
import urllib3


# from threading import Thread
#
# urllib3.disable_warnings()

class gengmei():

    def __init__(self):
        self.s = requests.session()
        self.uri = "https://ibackend.igengmei.com"
        self.offset = ""
        self.city = "zhanjiang"
        self.version = "7.15.2"  # "7.15.2"
        self.device_id = "868080041007173"

    def v3(self):
        url = self.uri + "/api/service/home/v3/list"

        body = {
            "platform": "iPhone",
            "os_version": "11.4.1",
            "version": "7.15.3",
            "model": "iPhone 6s",
            "release": "1",
            "idfa": "B6712382-69D5-4B12-9810-5F266411C4CF",
            "idfv": "1155D041-0F3A-4648-81B0-4255592A168B",
            "device_id": self.device_id,
            "channel": "App Store",
            "app_name": "gengmeiios",
            "current_city_id": self.city,
            "lat": "40.00450809772233",
            "lng": "116.4882250488191",
            "is_WiFi": "1",
            "hardware_model": "iPhone8,1",
            "area_id": "",
            "count": "10",
            "first_load": "1",
            "max_price": "",
            "min_price": "",
            "more_filters": "",
            "offset": self.offset,
            "order_by": "0",
            "tag_id": "",
            "tag_ids": "",
        }
        dataAll = self.s.get(url, data=body, verify=False)
        print(dataAll)
        mgListAll = dataAll['data.txt']['services']

        server_id = []  # 美购id
        service_name = []  # 美购名称
        for i in range(len(mgListAll)):
            server_id.append(mgListAll[i]['id'])
            service_name.append(mgListAll[i]['service_name'])
        print(server_id)
        print(dataAll['data.txt']['offset'])
        self.offset = dataAll['data.txt']['offset']


if __name__ == '__main__':
    page = 0
    app = gengmei()

    for i in range(100):
        app.v3()
