#
#
#
# 6329571274787944449   18514d6aa98e4b229db0a538bda7c5a4
# 0 |                      30 |           562 |          166 |                592 | 20180720
# 刚刚
# +----------+----------------------------------+--------------+-----------------------+-----------------------+----------------+
# | id       | doctor_id                        | expert_pv_30 | expert_exposure_pv_30 | expert_message_num_30 | partition_date |
# +----------+----------------------------------+--------------+-----------------------+-----------------------+----------------+
# | 11153549 | 18514d6aa98e4b229db0a538bda7c5a4 |          178 |                   777 |                     5 | 20191106       |
# +----------+----------------------------------+--------------+-----------------------+-----------------------+----------------+
#
# mysql> select * from statistic_merchant_rank_factor  where merchant_id = 6329571274787944449  and partition_date = 20191106;
# +---------+---------------------+-------------------------+-------------------------+---------------+--------------+--------------------+----------------+
# | id      | merchant_id         | doctor_ad_money_30_days | doctor_discount_30_days | service_pv_30 | expert_pv_30 | organization_pv_30 | partition_date |
# +---------+---------------------+-------------------------+-------------------------+---------------+--------------+--------------------+----------------+
# | 3945119 | 6329571274787944449 |                       0 |                    8481 |           553 |           90 |                712 | 20191106       |
# +---------+---------------------+-------------------------+-------------------------+---------------+--------------+--------------------+----------------+


# --+
# | id      | merchant_id         | doctor_ad_money_30_days | doctor_discount_30_days | service_pv_30 | expert_pv_30 | organization_pv_30 | partition_date |
# +---------+---------------------+-------------------------+-------------------------+---------------+--------------+--------------------+----------------+
# | 3946605 | 6328834428978124832 |                   45990 |                    8433 |          5477 |          172 |               5852 | 20191106       |
#
# | id       | doctor_id                        | expert_pv_30 | expert_exposure_pv_30 | expert_message_num_30 | partition_date |
# +----------+----------------------------------+--------------+-----------------------+-----------------------+----------------+
# | 11142396 | 8f18b2e3bdcd4deea53a356d4b3751e4 |          836 |                   444 |                    20 | 20191106       |
# +----------+----------------------------------+--------------+-----------------------+-----------------------+----------------+
#
# import math
#
# d_expert_message_num_30 = 20
# m_service_pv_30 = 5477
data = {
    "took": 49,
    "timed_out": False,
    "_shards": {
        "total": 8,
        "successful": 8,
        "failed": 0
    },
    "hits": {
        "total": 260,
        "max_score": 0000000000,
        "hits": [{
            "_index": "gm-dbmw-service_ngram_v1",
            "_type": "service",
            "_id": "5835980",
            "_score": 1.0,
            "_source": {
                "doctor": {
                    "name": "刘大猛",
                    "famous_doctor": False,
                    "id": "40fa252fee9148cab384536477f834fe",
                    "hospital": {
                        "city_province_name": "江苏",
                        "hospital_type2": "1",
                        "city_province_country_tag_id": 259,
                        "is_high_quality": False,
                        "hospital_type": "1",
                        "city_count": 0,
                        "officer_name": "南京奇致医疗美容医院",
                        "chain_count": 0,
                        "city_name": "南京",
                        "name": "南京华韩奇致美容医院",
                        "area_count": 0,
                        "id": "njqzmr",
                        "city_tag_id": 542,
                        "city_province_tag_id": 277
                    },
                    "title": "0"
                },
                "group": "nanjingqizhiyiliaomeirongyiyuan",
                "id": 5835980
            },
            "sort": [0.0, 1.0, 0.0, 2.0, 1, 217.439, 10000, 1559014164000, 1.0],
            "inner_hits": {
                "new_sku_special": {
                    "hits": {
                        "total": 1,
                        "max_score": 0000000000,
                        "hits": [{
                            "_index": "gm-dbmw-service_ngram_v1",
                            "_type": "service",
                            "_id": "5835980",
                            "_nested": {
                                "field": "new_sku_special",
                                "offset": 2
                            },
                            "_score": 0000000000,
                            "_source": {
                                "item_id": 6213261,
                                "position": 0,
                                "sku_id": 436113,
                                "has_pos": False,
                                "id": 6289
                            },
                            "sort": [10.191309, 9223372036854775807]
                        }]
                    }
                },
                "sku_list": {
                    "hits": {
                        "total": 5,
                        "max_score": 0000000000,
                        "hits": [{
                            "_index": "gm-dbmw-service_ngram_v1",
                            "_type": "service",
                            "_id": "5835980",
                            "_nested": {
                                "field": "sku_list",
                                "offset": 2
                            },
                            "_score": 0000000000,
                            "_source": {
                                "sku_id": 436113,
                                "name": "【特价】【到院礼送E光白瓷娃娃】无痕切开双眼皮",
                                "price_type": 1,
                                "price": 199,
                                "sku_rank": 0,
                                "end_time": "2019-11-30T23:59:59+08:00",
                                "start_time": "2019-11-03T00:22:52+08:00"
                            },
                            "sort": [1.4142135, 199]
                        }]
                    }
                }
            }
        }, {
            "_index": "gm-dbmw-service_ngram_v1",
            "_type": "service",
            "_id": "5852066",
            "_score": 1.0,
            "_source": {
                "doctor": {
                    "name": "美国容丽妍南京分院（中国区旗舰院）",
                    "famous_doctor": False,
                    "id": "5b9f74031cbf4d9da5895c755128ce64",
                    "hospital": {
                        "city_province_name": "江苏",
                        "hospital_type2": "1",
                        "city_province_country_tag_id": 259,
                        "is_high_quality": True,
                        "hospital_type": "1",
                        "city_count": 0,
                        "officer_name": "美国容丽妍南京分院（中国区旗舰院）",
                        "chain_count": 0,
                        "city_name": "南京",
                        "name": "美国容丽妍南京分院（中国区旗舰院）",
                        "area_count": 0,
                        "id": "3b1464f3762340db9cd69ed568ffcadd",
                        "city_tag_id": 542,
                        "city_province_tag_id": 277
                    },
                    "title": ""
                },
                "group": "5b9f74031cbf4d9da5895c755128ce64",
                "id": 5852066
            },
            "sort": [0.0, 1.0, 0.0, 2.0, 1, 45.6936, 10000, 1569376139000, 1.0],
            "inner_hits": {
                "new_sku_special": {
                    "hits": {
                        "total": 1,
                        "max_score": 0000000000,
                        "hits": [{
                            "_type": "service",
                            "_id": "5852066",
                            "_nested": {
                                "field": "new_sku_special",
                                "offset": 6
                            },
                            "_score": 0000000000,
                            "_source": {
                                "item_id": 6213255,
                                "position": 0,
                                "sku_id": 490604,
                                "has_pos": False,
                                "id": 6289
                            },
                            "sort": [10.55403, 9223372036854775807]
                        }]
                    }
                },
                "sku_list": {
                    "hits": {
                        "total": 3,
                        "max_score": 0000000000,
                        "hits": [{
                            "_type": "service",
                            "_id": "5852066",
                            "_nested": {
                                "field": "sku_list",
                                "offset": 3
                            },
                            "_score": 0000000000,
                            "_source": {
                                "sku_id": 490602,
                                "name": "无针水光1次",
                                "price_type": 1,
                                "price": 5,
                                "sku_rank": 0,
                                "end_time": "2019-11-13T10:00:00+08:00",
                                "start_time": "2019-11-01T10:00:00+08:00"
                            },
                            "sort": [1.4142135, 5]
                        }]
                    }
                }
            }
        }, {
            "_index": "gm-dbmw-service_ngram_v1",
            "_type": "service",
            "_id": "5844454",
            "_score": 1.0,
            "_source": {
                "doctor": {
                    "name": "南京柠檬医疗美容",
                    "famous_doctor": False,
                    "id": "bc3c067690384303a505f41eb716cb52",
                    "hospital": {
                        "city_province_name": "江苏",
                        "hospital_type2": "1",
                        "city_province_country_tag_id": 259,
                        "is_high_quality": True,
                        "hospital_type": "1",
                        "city_count": 0,
                        "officer_name": "南京柠檬医疗美容",
                        "chain_count": 0,
                        "city_name": "南京",
                        "name": "南京柠檬医疗美容",
                        "area_count": 0,
                        "id": "4f329c4f46fe419f89aed4338ebf1640",
                        "city_tag_id": 542,
                        "city_province_tag_id": 277
                    },
                    "title": ""
                },
                "group": "bc3c067690384303a505f41eb716cb52",
                "id": 5844454
            },
            "sort": [0.0, 1.0, 0.0, 2.0, 0, 93.1752, 10000, 1564132737000, 1.0],
            "inner_hits": {
                "new_sku_special": {
                    "hits": {
                        "total": 1,
                        "max_score": 0000000000,
                        "hits": [{
                            "_type": "service",
                            "_id": "5844454",
                            "_nested": {
                                "field": "new_sku_special",
                                "offset": 6
                            },
                            "_score": 0000000000,
                            "_source": {
                                "item_id": 6213367,
                                "position": 0,
                                "sku_id": 464743,
                                "has_pos": False,
                                "id": 6289
                            },
                            "sort": [10.025624, 9223372036854775807]
                        }]
                    }
                },
                "sku_list": {
                    "hits": {
                        "total": 4,
                        "max_score": 0000000000,
                        "hits": [{
                            "_type": "service",
                            "_id": "5844454",
                            "_nested": {
                                "field": "sku_list",
                                "offset": 4
                            },
                            "_score": 0000000000,
                            "_source": {
                                "sku_id": 464743,
                                "name": "欣可聆水光针2ml（限1支）",
                                "price_type": 1,
                                "price": 199,
                                "sku_rank": 1,
                                "end_time": "2019-11-30T23:59:59+08:00",
                                "start_time": "2019-11-03T00:22:52+08:00"
                            },
                            "sort": [1.4142135, 199]
                        }]
                    }
                }
            }
        }, {
            "_index": "gm-dbmw-service_ngram_v1",
            "_type": "service",
            "_id": "5757713",
            "_score": 1.0,
            "_source": {
                "doctor": {
                    "name": "南京艺星医疗美容",
                    "famous_doctor": False,
                    "id": "c4e818d43ce646599f15c4b42d1be614",
                    "hospital": {
                        "city_province_name": "江苏",
                        "hospital_type2": "1",
                        "city_province_country_tag_id": 259,
                        "is_high_quality": True,
                        "hospital_type": "1",
                        "city_count": 0,
                        "officer_name": "南京艺星医疗美容",
                        "chain_count": 0,
                        "city_name": "南京",
                        "name": "南京艺星医疗美容",
                        "area_count": 0,
                        "id": "fb32833d473240fba50e4afa764a7d00",
                        "city_tag_id": 542,
                        "city_province_tag_id": 277
                    },
                    "title": ""
                },
                "group": "c4e818d43ce646599f15c4b42d1be614",
                "id": 5757713
            },
            "sort": [0.0, 1.0, 0.0, 2.0, 0, 90.4924, 10000, 1527761255000, 1.0],
            "inner_hits": {
                "new_sku_special": {
                    "hits": {
                        "total": 1,
                        "max_score": 0000000000,
                        "hits": [{
                            "_type": "service",
                            "_id": "5757713",
                            "_nested": {
                                "field": "new_sku_special",
                                "offset": 8
                            },
                            "_score": 0000000000,
                            "_source": {
                                "item_id": 6213411,
                                "position": 0,
                                "sku_id": 390765,
                                "has_pos": False,
                                "id": 6289
                            },
                            "sort": [10.55403, 9223372036854775807]
                        }]
                    }
                },
                "sku_list": {
                    "hits": {
                        "total": 5,
                        "max_score": 0000000000,
                        "hits": [{
                            "_type": "service",
                            "_id": "5757713",
                            "_nested": {
                                "field": "sku_list",
                                "offset": 5
                            },
                            "_score": 0000000000,
                            "_source": {
                                "sku_id": 256985,
                                "name": "红蓝光祛痘 医学祛痘 1次",
                                "price_type": 1,
                                "price": 90,
                                "sku_rank": 0,
                                "end_time": "2019-11-13T10:00:00+08:00",
                                "start_time": "2019-11-01T10:00:00+08:00"
                            },
                            "sort": [1.4142135, 90]
                        }]
                    }
                }
            }
        }, {
            "_index": "gm-dbmw-service_ngram_v1",
            "_type": "service",
            "_id": "5835979",
            "_score": 1.0,
            "_source": {
                "doctor": {
                    "name": "章宏伟",
                    "famous_doctor": False,
                    "id": "0b350b3ffc2b4c819f9cab56455332cc",
                    "hospital": {
                        "city_province_name": "江苏",
                        "hospital_type2": "1",
                        "city_province_country_tag_id": 259,
                        "is_high_quality": False,
                        "hospital_type": "1",
                        "city_count": 0,
                        "officer_name": "南京奇致医疗美容医院",
                        "chain_count": 0,
                        "city_name": "南京",
                        "name": "南京华韩奇致美容医院",
                        "area_count": 0,
                        "id": "njqzmr",
                        "city_tag_id": 542,
                        "city_province_tag_id": 277
                    },
                    "title": "4"
                },
                "group": "nanjingqizhiyiliaomeirongyiyuan",
                "id": 5835979
            },
            "sort": [0.0, 1.0, 0.0, 2.0, 0, 17.5793, 10000, 1559013156000, 1.0],
            "inner_hits": {
                "new_sku_special": {
                    "hits": {
                        "total": 1,
                        "max_score": 0000000000,
                        "hits": [{
                            "_type": "service",
                            "_id": "5835979",
                            "_nested": {
                                "field": "new_sku_special",
                                "offset": 1
                            },
                            "_score": 0000000000,
                            "_source": {
                                "item_id": 6213260,
                                "position": 0,
                                "sku_id": 436109,
                                "has_pos": False,
                                "id": 6289
                            },
                            "sort": [10.492683, 9223372036854775807]
                        }]
                    }
                },
                "sku_list": {
                    "hits": {
                        "total": 4,
                        "max_score": 0000000000,
                        "hits": [{
                            "_type": "service",
                            "_id": "5835979",
                            "_nested": {
                                "field": "sku_list",
                                "offset": 2
                            },
                            "_score": 0000000000,
                            "_source": {
                                "sku_id": 436109,
                                "name": "【特价】【到院礼送E光白瓷娃娃】无痕切开双眼皮",
                                "price_type": 1,
                                "price": 199,
                                "sku_rank": 0,
                                "end_time": "2019-11-30T23:59:59+08:00",
                                "start_time": "2019-11-03T00:22:52+08:00"
                            },
                            "sort": [1.4142135, 199]
                        }]
                    }
                }
            }
        }, {
            "_index": "gm-dbmw-service_ngram_v1",
            "_type": "service",
            "_id": "5799378",
            "_score": 1.0,
            "_source": {
                "doctor": {
                    "name": "江苏施尔美整形美容医院",
                    "famous_doctor": False,
                    "id": "e86a6c4636c642d09d91da1ff269b4ea",
                    "hospital": {
                        "city_province_name": "江苏",
                        "hospital_type2": "1",
                        "city_province_country_tag_id": 259,
                        "is_high_quality": True,
                        "hospital_type": "1",
                        "city_count": 0,
                        "officer_name": "江苏施尔美整形美容医院",
                        "chain_count": 0,
                        "city_name": "南京",
                        "name": "江苏施尔美整形美容医院",
                        "area_count": 0,
                        "id": "5905b0b6002f4e3f8510124fa03cecdb",
                        "city_tag_id": 542,
                        "city_province_tag_id": 277
                    },
                    "title": ""
                },
                "group": "e86a6c4636c642d09d91da1ff269b4ea",
                "id": 5799378
            },
            "sort": [0.0, 1.0, 0.0, 2.0, 0, 3.84775, 10000, 1535791941000, 1.0],
            "inner_hits": {
                "new_sku_special": {
                    "hits": {
                        "total": 1,
                        "max_score": 0000000000,
                        "hits": [{
                            "_type": "service",
                            "_id": "5799378",
                            "_nested": {
                                "field": "new_sku_special",
                                "offset": 3
                            },
                            "_score": 0000000000,
                            "_source": {
                                "item_id": 6213485,
                                "position": 0,
                                "sku_id": 434633,
                                "has_pos": False,
                                "id": 6289
                            },
                            "sort": [10.55403, 9223372036854775807]
                        }]
                    }
                },
                "sku_list": {
                    "hits": {
                        "total": 2,
                        "max_score": 0000000000,
                        "hits": [{
                            "_type": "service",
                            "_id": "5799378",
                            "_nested": {
                                "field": "sku_list",
                                "offset": 3
                            },
                            "_score": 0000000000,
                            "_source": {
                                "sku_id": 304350,
                                "name": "国产衡力.除皱.面部提升.20u",
                                "price_type": 0,
                                "price": 140,
                                "sku_rank": 2,
                                "end_time": "2028-09-01T16:52:21+08:00",
                                "start_time": "2018-09-01T16:52:21+08:00"
                            },
                            "sort": [1.4142135, 140]
                        }]
                    }
                }
            }
        }, {
            "_index": "gm-dbmw-service_ngram_v1",
            "_type": "service",
            "_id": "5197073",
            "_score": 1.0,
            "_source": {
                "doctor": {
                    "name": "南京连天美医疗美容医院",
                    "famous_doctor": False,
                    "id": "853965a8296d11e6be9c00163e000d0b",
                    "hospital": {
                        "city_province_name": "江苏",
                        "hospital_type2": "1",
                        "city_province_country_tag_id": 259,
                        "is_high_quality": False,
                        "hospital_type": "1",
                        "city_count": 0,
                        "officer_name": "南京连天美医疗美容医院",
                        "chain_count": 0,
                        "city_name": "南京",
                        "name": "南京连天美医疗美容医院",
                        "area_count": 0,
                        "id": "njltmylmryy",
                        "city_tag_id": 542,
                        "city_province_tag_id": 277
                    },
                    "title": ""
                },
                "group": "853965a8296d11e6be9c00163e000d0b",
                "id": 5197073
            },
            "sort": [0.0, 1.0, 0.0, 2.0, 0, 0.91385, 0, 1468306486000, 1.0],
            "inner_hits": {
                "new_sku_special": {
                    "hits": {
                        "total": 1,
                        "max_score": 0000000000,
                        "hits": [{
                            "_type": "service",
                            "_id": "5197073",
                            "_nested": {
                                "field": "new_sku_special",
                                "offset": 125
                            },
                            "_score": 0000000000,
                            "_source": {
                                "item_id": 6213247,
                                "position": 0,
                                "sku_id": 54264,
                                "has_pos": False,
                                "id": 6289
                            },
                            "sort": [10.492683, 9223372036854775807]
                        }]
                    }
                },
                "sku_list": {
                    "hits": {
                        "total": 3,
                        "max_score": 0000000000,
                        "hits": [{
                            "_type": "service",
                            "_id": "5197073",
                            "_nested": {
                                "field": "sku_list",
                                "offset": 2
                            },
                            "_score": 0000000000,
                            "_source": {
                                "sku_id": 54264,
                                "name": "润月雅水光2.0ml",
                                "price_type": 1,
                                "price": 69,
                                "sku_rank": 1,
                                "end_time": "2019-11-13T10:00:00+08:00",
                                "start_time": "2019-11-01T10:00:00+08:00"
                            },
                            "sort": [1.4142135, 69]
                        }]
                    }
                }
            }
        }, {
            "_index": "gm-dbmw-service_ngram_v1",
            "_type": "service",
            "_id": "5752949",
            "_score": 1.0,
            "_source": {
                "doctor": {
                    "name": "南京连天美医疗美容医院",
                    "famous_doctor": False,
                    "id": "853965a8296d11e6be9c00163e000d0b",
                    "hospital": {
                        "city_province_name": "江苏",
                        "hospital_type2": "1",
                        "city_province_country_tag_id": 259,
                        "is_high_quality": False,
                        "hospital_type": "1",
                        "city_count": 0,
                        "officer_name": "南京连天美医疗美容医院",
                        "chain_count": 0,
                        "city_name": "南京",
                        "name": "南京连天美医疗美容医院",
                        "area_count": 0,
                        "id": "njltmylmryy",
                        "city_tag_id": 542,
                        "city_province_tag_id": 277
                    },
                    "title": ""
                },
                "group": "853965a8296d11e6be9c00163e000d0b",
                "id": 5752949
            },
            "sort": [0.0, 1.0, 0.0, 2.0, 0, 0.0372225, 0, 1506823160000, 1.0],
            "inner_hits": {
                "new_sku_special": {
                    "hits": {
                        "total": 1,
                        "max_score": 0000000000,
                        "hits": [{
                            "_type": "service",
                            "_id": "5752949",
                            "_nested": {
                                "field": "new_sku_special",
                                "offset": 43
                            },
                            "_score": 0000000000,
                            "_source": {
                                "item_id": 6213391,
                                "position": 0,
                                "sku_id": 205035,
                                "has_pos": False,
                                "id": 6289
                            },
                            "sort": [9.965385, 9223372036854775807]
                        }]
                    }
                },
                "sku_list": {
                    "hits": {
                        "total": 1,
                        "max_score": 0000000000,
                        "hits": [{
                            "_type": "service",
                            "_id": "5752949",
                            "_nested": {
                                "field": "sku_list",
                                "offset": 2
                            },
                            "_score": 0000000000,
                            "_source": {
                                "sku_id": 205035,
                                "name": "M22祛斑1次",
                                "price_type": 1,
                                "price": 99,
                                "sku_rank": 1,
                                "end_time": "2019-11-13T10:00:00+08:00",
                                "start_time": "2019-11-01T10:00:00+08:00"
                            },
                            "sort": [1.4142135, 99]
                        }]
                    }
                }
            }
        }, {
            "_index": "gm-dbmw-service_ngram_v1",
            "_type": "service",
            "_id": "5805178",
            "_score": 1.0,
            "_source": {
                "doctor": {
                    "name": "南京普瑞缇医疗美容",
                    "famous_doctor": False,
                    "id": "82dd0f416f4947f6b2aed7c428b480e9",
                    "hospital": {
                        "city_province_name": "江苏",
                        "hospital_type2": "1",
                        "city_province_country_tag_id": 259,
                        "is_high_quality": True,
                        "hospital_type": "1",
                        "city_count": 0,
                        "officer_name": "南京普瑞缇医疗美容",
                        "chain_count": 0,
                        "city_name": "南京",
                        "name": "南京普瑞缇医疗美容",
                        "area_count": 0,
                        "id": "44f108f88c344e2a866a5bbc2bfcce5b",
                        "city_tag_id": 542,
                        "city_province_tag_id": 277
                    },
                    "title": ""
                },
                "group": "82dd0f416f4947f6b2aed7c428b480e9",
                "id": 5805178
            },
            "sort": [0.0, 1.0, 0.0, 2.0, 0, 0.0164352, 10000, 1540272653000, 1.0],
            "inner_hits": {
                "new_sku_special": {
                    "hits": {
                        "total": 1,
                        "max_score": 0000000000,
                        "hits": [{
                            "_index": "gm-dbmw-service_ngram_v1",
                            "_type": "service",
                            "_id": "5805178",
                            "_nested": {
                                "field": "new_sku_special",
                                "offset": 2
                            },
                            "_score": 0000000000,
                            "_source": {
                                "item_id": 6213395,
                                "position": 0,
                                "sku_id": 327769,
                                "has_pos": False,
                                "id": 6289
                            },
                            "sort": [10.191309, 9223372036854775807]
                        }]
                    }
                },
                "sku_list": {
                    "hits": {
                        "total": 2,
                        "max_score": 0000000000,
                        "hits": [{
                            "_index": "gm-dbmw-service_ngram_v1",
                            "_type": "service",
                            "_id": "5805178",
                            "_nested": {
                                "field": "sku_list",
                                "offset": 5
                            },
                            "_score": 0000000000,
                            "_source": {
                                "sku_id": 511014,
                                "name": "【双11狂欢】到院送小气泡净肤",
                                "price_type": 2,
                                "price": 1,
                                "sku_rank": 10,
                                "end_time": "2019-11-13T10:00:00+08:00",
                                "start_time": "2019-11-05T15:17:34+08:00"
                            },
                            "sort": [1.4142135, 1]
                        }]
                    }
                }
            }
        }, {
            "_index": "gm-dbmw-service_ngram_v1",
            "_type": "service",
            "_id": "5708692",
            "_score": 1.0,
            "_source": {
                "doctor": {
                    "name": "北京凯润婷（原史三八）医疗美容医院",
                    "famous_doctor": False,
                    "id": "3e00f028f81d11e6af9e00163e0051d4",
                    "hospital": {
                        "city_province_name": "北京",
                        "hospital_type2": "1",
                        "city_province_country_tag_id": 259,
                        "is_high_quality": False,
                        "hospital_type": "1",
                        "city_count": 8,
                        "officer_name": "北京凯润婷（原史三八）医疗美容医院",
                        "chain_count": 8,
                        "city_name": "北京",
                        "name": "北京凯润婷（原史三八）医疗美容医院",
                        "area_count": 5000,
                        "id": "96ea37eef81d11e692f800163e000a4a",
                        "city_tag_id": 328,
                        "city_province_tag_id": 264
                    },
                    "title": ""
                },
                "group": "3e00f028f81d11e6af9e00163e0051d4",
                "id": 5708692
            },
            "sort": [0.0, 1.0, 0.0, 1.0, 1, 1021.4, 0, 1487673949000, 1.0],
            "inner_hits": {
                "new_sku_special": {
                    "hits": {
                        "total": 1,
                        "max_score": 0000000000,
                        "hits": [{
                            "_type": "service",
                            "_id": "5708692",
                            "_nested": {
                                "field": "new_sku_special",
                                "offset": 33
                            },
                            "_score": 0000000000,
                            "_source": {
                                "item_id": 6213343,
                                "position": 0,
                                "sku_id": 350488,
                                "has_pos": False,
                                "id": 6289
                            },
                            "sort": [10.492683, 9223372036854775807]
                        }]
                    }
                },
                "sku_list": {
                    "hits": {
                        "total": 16,
                        "max_score": 0000000000,
                        "hits": [{
                            "_type": "service",
                            "_id": "5708692",
                            "_nested": {
                                "field": "sku_list",
                                "offset": 26
                            },
                            "_score": 0000000000,
                            "_source": {
                                "sku_id": 350488,
                                "name": "薇力·玻尿酸·太阳穴/法令纹/额头/面颊·填充塑形·0.6ml（限购一次）",
                                "price_type": 1,
                                "price": 199,
                                "sku_rank": 4,
                                "end_time": "2019-11-30T23:59:59+08:00",
                                "start_time": "2019-11-03T00:22:52+08:00"
                            },
                            "sort": [1.4142135, 199]
                        }]
                    }
                }
            }
        }]
    }
}

from collections import deque, OrderedDict
import unittest, random
import itertools


def variousness(items, variety_size):
    src = deque(items)
    dst = []
    while len(src) > 0:
        pos, temp, recover, dup = 0, [], [], []
        while pos < variety_size:
            try:
                item = src.popleft()
                # print(item)
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


inner_hits = True

skus = []
res_hit = data["hits"]["hits"]
for item in res_hit:
    if 'inner_hits' in item:
        hit = item['inner_hits']
        if inner_hits == True and hit["new_sku_special"]['hits']["total"] > 0:
            sku = hit["new_sku_special"]['hits']['hits'][0]
        else:
            sku = hit['sku_list']['hits']['hits'][0]

        sku_id = sku['_source']['sku_id']
        merchant_id = item['_source']['group']
        city = item['_source']['doctor']['hospital']['city_tag_id']
        nearby = [row['tag_id'] for row in item['_source'].get('nearby_city_tags', [])]
        is_promote = item['_source'].get("is_promote", False)
        skus.append({"id": sku_id,
                     "group": merchant_id,
                     "city": city,
                     "nearby": nearby,
                     "is_promote": is_promote})


def region_division(items, current_city):
    city, nearby, other = [], [], []
    for item in items:
        if current_city == item.get("city"):
            city.append(item)
        elif current_city in item.get("nearby"):
            nearby.append(item)
        else:
            other.append(item)
    return [city, nearby, other]


import functools

MAX_LOAD = 200
GROUP_SIZE = 10
sku_rerank = []
variousness_per_10 = functools.partial(variousness, variety_size=GROUP_SIZE)

division_slus = region_division(skus, 542)
division_reranks = map(variousness_per_10, division_slus)
print(division_slus)
sku_rerank = [sku for skus in division_reranks for sku in skus]
sku_ids = [sku['id'] for sku in sku_rerank]
sku_is_promote = [sku['is_promote'] for sku in sku_rerank]
#
# [{\"sku_id\": 436113, \"__src_type\": \"es\", \"position\": 0}, 南京奇致医疗美容医院
# {\"sku_id\": 490604, \"__src_type\": \"es\", \"position\": 0},美国容丽妍南京分院（中国区旗舰院）
#  {\"sku_id\": 464743, \"__src_type\": \"es\", \"position\": 0},南京柠檬医疗美容
#  {\"sku_id\": 390765, \"__src_type\": \"es\", \"position\": 0},南京艺星医疗美容
#  {\"sku_id\": 434633, \"__src_type\": \"es\", \"position\": 0},江苏施尔美整形美容医院"
#  {\"sku_id\": 54264, \"__src_type\": \"es\", \"position\": 0},南京连天美医疗美容医院
#  {\"sku_id\": 327769, \"__src_type\": \"es\", \"position\": 0},南京普瑞缇医疗美容
#  {\"sku_id\": 509964, \"__src_type\": \"es\", \"position\": 0},
#  {\"sku_id\": 504172, \"__src_type\": \"es\", \"position\": 0},
#  {\"sku_id\": 70966, \"__src_type\": \"es\", \"position\": 0}], \"rank_mode\": \"1\"}}"}
#
#
# 436113,
# 490604
# ,464743,
# 390765,
# 436109(南京奇致医疗美容医院”),
# 434633,
# 54264(南京连天美医疗美容医院),
# 205035(南京连天美医疗美容医院),
# 327769(南京普瑞缇医疗美容),
# 350488(北京凯润婷（原史三八）医疗美容医院),
# 5788113, 5347750, 5347077]
[436113,
 490602,
 464743,
 256985,
 304350,
 54264,
 511014,
 436109,
 205035,
 267607],