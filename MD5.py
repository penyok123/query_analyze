import logging
import traceback
import hashlib
import json


def recommed_service_category_device_id(device_id, real_cary=False):
    try:
        '''
        设备品类显示, 是否命中灰度
        '''
        categroy_select_cary = ["0", "1", "2", "3", "4", "a", "b", "c", "e"]
        if real_cary:
            categroy_select_cary_v2 = ["0", "1", "2", "3", "4", "a", "b", "c"]

        if not device_id:
            return False

        hd_id = hashlib.md5(str(device_id).encode()).hexdigest()
        is_gray = hd_id[-1] in categroy_select_cary

        return is_gray
    except:
        logging.error("catch exception,err_msg:%s" % traceback.format_exc())
        return False


def recommed_service_category_device_id_2(device_id):
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



ss = recommed_service_category_device_id_2(device_id='867961035707277')
print(ss)
