import redis
import json


def save_service_tag(query, closure_tags_name_list):
    REDIS_URL = 'redis://:ReDis!GmTx*0aN6@172.16.40.133:6379'
    redis_client = redis.StrictRedis.from_url(REDIS_URL)
    key_service_closure_tags = "service_closure_tags"
    redis_client.hset(key_service_closure_tags, query, json.dumps(list(closure_tags_name_list)))
    service_closure_tags = redis_client.hget(key_service_closure_tags, query)
    closure_tags = json.loads(service_closure_tags)

    return closure_tags


if __name__ == '__main__':
    query = ""
    closure_tags_name_list = []
    closure_tags = save_service_tag(query, closure_tags_name_list)
    print(closure_tags)
#
# REDIS_URL = 'redis://redis.paas-test.env:6379/0'

# closure_tags_name_list = ["玻尿酸除皱", "肉毒素除皱", "自体脂肪除皱", "激光除皱", "埋线除皱", "热玛吉", "热拉提"]
# query = "除皱套餐"

# closure_tags_name_list = ["假体隆胸", "脂肪隆胸", "自体脂肪丰胸", "自体脂肪隆胸", "胸部塑身", "胸部提升", "隆胸套餐", "硅胶隆胸", "埋线提升胸部"]
# query = "隆胸套餐"

# closure_tags_name_list = ["红蓝光祛痘", "祛痘", "祛痘祛痘印", "清洁祛痘", "果酸焕肤", "微针祛痘坑", "黄金微针"]
# query = "祛痘套餐"

# closure_tags_name_list =["光子嫩肤","白瓷娃娃","皮秒","超皮秒","激光祛斑","祛斑"]
# query = "祛斑套餐"

# closure_tags_name_list = ["美白针", "水光针", "光子嫩肤", "白瓷娃娃", "皮秒", "超皮秒", "美白嫩肤"]
# query = "美白套餐"

# closure_tags_name_list = ["开内眼角", "开外眼角", "重睑术", "翘睫术", "上睑提肌", "眼角提升", "眼部提肌"]
# query = "眼部套餐"


# 类目	相关项目
# 祛斑	光子嫩肤/白瓷娃娃/皮秒/超皮秒/
# 隆胸	脂肪隆胸/假体隆胸
# 祛痘	红蓝光/果酸焕肤/黄金微针
# 美白	美白针/水光针/光子嫩肤/白瓷娃娃/皮秒/超皮秒
# 眼部	开内眼角/开外眼角/重睑术/翘睫术/上睑提肌
# 除皱	肉毒素/热玛吉/玻尿酸/胶原蛋白/热拉提


# closure_tags_name_list = ["开内眼角", "开外眼角", "切眉术", "埋线双眼皮", "切开双眼皮", "定点双眼皮", "外切双眼皮","内切双眼皮","眶隔脂肪释放","上眼睑去脂","上睑提肌","下眼下至术","眼部修复"]
# query = "眼综合"


# query = "鼻部综合"
# closure_tags_name_list = ["膨体(硅胶)隆鼻术", "鼻头缩小术", "鼻翼缩小术", "鼻被整形术", "鼻孔缩小术", "鼻小柱延长术", "朝天鼻矫正术”，"驼峰修复术","失败隆鼻手术再修复"]


# closure_tags_name_list = ["开内眼角", "开外眼角", "重睑术", "翘睫术", "上睑提肌", "眼角提升", "眼部提肌"]
# query = "眼部套餐"


# closure_tags_name_list = ["开内眼角", "开外眼角", "重睑术", "翘睫术", "上睑提肌", "眼角提升", "眼部提肌"]
# query = "眼部套餐"
