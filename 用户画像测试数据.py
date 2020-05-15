import redis
import json


def items_gt_score(d):
    new_d = dict(sorted(d.items(), key=lambda x: x[1], reverse=True))
    res = {tag: float(score) for tag, score in new_d.items() if float(score) >= 0}
    return list(res.keys())


def get_portrait(key):
    user_portrait = json.loads(redis_client2.get(key))
    first_demands = items_gt_score(user_portrait.get("first_demands", {}))
    second_demands = items_gt_score(user_portrait.get("second_demands", {}))
    first_solutions = items_gt_score(user_portrait.get("first_solutions", {}))
    second_solutions = items_gt_score(user_portrait.get("second_solutions", {}))
    first_positions = items_gt_score(user_portrait.get("first_positions", {}))
    second_positions = items_gt_score(user_portrait.get("second_positions", {}))
    projects = items_gt_score(user_portrait.get("projects", {}))

    return {
        "first_demands": first_demands,
        "second_demands": second_demands,
        "first_solutions": first_solutions,
        "second_solutions": second_solutions,
        "first_positions": first_positions,
        "second_positions": second_positions,
        "projects": projects
    }


if __name__ == '__main__':
    REDIS_URL = "redis://redis.paas-test.env:6379/0"
    redis_client2 = redis.StrictRedis.from_url(REDIS_URL)
    key = "doris:user_portrait:tag3:device_id:12345"
    icm_key = "doris:user_portrait:tag3:increment_update:device_id:12345"

    values = {"first_positions": {"水光针": 335.99129525333456, "玻尿酸": 204.88820150455518},
              "second_positions": {"水光针": 57.40054672225983, "隆鼻": 13.445181124363316},
              "second_solutions": {"塑形": 9.60727846321718, "吸脂": 180.96381030885658},
              "projects": {"玻尿酸丰眼窝": 13.361579304010746},
              "second_demands": {"双眼皮": 1117.6390444525601335, "祛眼袋": 13.833256200094708,
                                 "水光针": 1117.6390444525601335, "隆鼻": 13.833256200094708,
                                 "瘦脸": 7.6390444525601335, "垫下巴": 13.833256200094708,
                                 "硅胶垫下巴": 7.6390444525601335, "瘦脸针": 3.833256200094708,
                                 "自体脂肪丰太阳穴": 7.6390444525601335, "祛黑眼圈": 3.833256200094708},
              "first_demands": {"美白": 21.380230904675187, "祛黑眼圈": 191.39697103128782},
              "first_solutions": {"隆胸": 270.84839302614574, "祛痘": 480.56623766391414}}

    redis_client2.set(key, json.dumps(values))
    redis_client2.set(icm_key, json.dumps(values))

    ss = redis_client2.keys(key)
    for item in ss:
        key = str(item, encoding="utf-8")
        data = get_portrait(key)
        print(data)

    values = ['祛颊脂垫', '祛黑头', '祛晒斑', '祛肿眼泡', '祛斑', '颧骨提升', '修眉', '生眉毛', '祛黑眼圈', '缩鼻翼', '祛眼袋', '除抬头纹', '嘴角上扬', '补水',
              '缩鼻头',
              '缩眼距', '祛痣', '祛痘印', '薄唇', '下眼睑下至', '眼线', '面部消脂', '除眉间纹', '控油', '垫下巴', '缩毛孔', '瘦脸', '祛雀斑', '缩下颌角', '洁面',
              '除眼纹',
              '祛黄褐斑', '双眼皮', '填充苹果肌', '缩咬肌', '隆鼻', '美白', '除法令纹', '丰太阳穴', '颧骨内推', '开眼角', '丰唇', '填充下颌缘', '祛痘', '祛痘坑',
              '缩短下巴', "水光针"]
    key = "ai_channel_feed_demands"
    redis_client2.set(key, json.dumps(values))
    print(json.loads(redis_client2.get(key)))

    print(str("徐学东").encode("utf-8"))
