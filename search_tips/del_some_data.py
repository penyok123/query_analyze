import hashlib


def recommed_service_category_device_id(device_id):
    try:
        '''
        设备品类显示, 是否命中灰度 
        '''
        categroy_select_cary1 = ["0", "1", "2", "3", "c", "d", "e", "f"]
        categroy_select_cary2 = ["4", "5", "6", "a"]
        categroy_select_cary3 = ["9", "8", "7", "b"]

        if not device_id:
            return 1

        hd_id = hashlib.md5(str(device_id).encode()).hexdigest()
        is_gray = hd_id[-1]

        if is_gray in categroy_select_cary2:
            return 2
        elif is_gray in categroy_select_cary3:
            return 3
        else:
            return 1
    except:
        return 1


print(recommed_service_category_device_id(device_id="F3F4C95F-BF76-4F82-9CC6-B5A8933A6BD9"))
