score = {
    "_shard": "[gm-dbmw-service][4]",
    "_node": "h4Cf18UVS0OAtsfkFigw2w",
    "_index": "gm-dbmw-service",
    "_type": "_doc",
    "_id": "5801316",
    "_score": 71.06288,
    "_source": {
        "id": 5801316
    },
    "_explanation": {
        "value": 71.06288,
        "description": "sum of:",
        "details": [
            {
                "value": 1.6619924,  # is_online
                "description": "weight(is_online:T in 117676) [PerFieldSimilarity], result of:",
                "details": [
                    {
                        "value": 1.6619924,
                        "description": "score(doc=117676,freq=1.0 = termFreq=1.0\n), product of:",
                        "details": [
                            {
                                "value": 1.6619924,
                                "description": "idf, computed as log(1 + (docCount - docFreq + 0.5) / (docFreq + 0.5)) from:",
                                "details": [
                                    {
                                        "value": 3074.0,
                                        "description": "docFreq",
                                        "details": []
                                    },
                                    {
                                        "value": 16201.0,
                                        "description": "docCount",
                                        "details": []
                                    }
                                ]
                            },
                            {
                                "value": 1.0,
                                "description": "tfNorm, computed as (freq * (k1 + 1)) / (freq + k1) from:",
                                "details": [
                                    {
                                        "value": 1.0,
                                        "description": "termFreq=1.0",
                                        "details": []
                                    },
                                    {
                                        "value": 1.2,
                                        "description": "parameter k1",
                                        "details": []
                                    },
                                    {
                                        "value": 0.0,
                                        "description": "parameter b (norms omitted for field)",
                                        "details": []
                                    }
                                ]
                            }
                        ]
                    }
                ]
            },
            {
                "value": 4.0,
                "description": "Score based on 4 child docs in range from 236547 to 236619, best match:",
                "details": [
                    {
                        "value": 4.0,
                        "description": "sum of:",
                        "details": [
                            {
                                "value": 4.0,
                                "description": "sum of:",
                                "details": [
                                    {
                                        "value": 1.0,
                                        "description": "sku_list.start_time:[-9223372036854775808 TO 1575618946752]",
                                        "details": []
                                    },
                                    {
                                        "value": 1.0,
                                        "description": "sku_list.end_time:[1575618946753 TO 9223372036854775807]",
                                        "details": []
                                    },
                                    {
                                        "value": 1.0,
                                        "description": "sku_list.start_time:[-9223372036854775808 TO 1575618946752]",
                                        "details": []
                                    },
                                    {
                                        "value": 1.0,
                                        "description": "sku_list.end_time:[1575618946753 TO 9223372036854775807]",
                                        "details": []
                                    }
                                ]
                            },
                            {
                                "value": 0.0,
                                "description": "match on required clause, product of:",
                                "details": [
                                    {
                                        "value": 0.0,
                                        "description": "# clause",
                                        "details": []
                                    },
                                    {
                                        "value": 1.0,
                                        "description": "_type:__sku_list",
                                        "details": []
                                    }
                                ]
                            }
                        ]
                    }
                ]
            },
            {
                "value": 65.40089,
                "description": "sum of:",
                "details": [
                    {
                        "value": 38.634663,
                        "description": "max of:",
                        "details": [
                            {
                                "value": 38.634663,
                                "description": "weight(short_description:紧 in 117676) [PerFieldSimilarity], result of:",
                                "details": [
                                    {
                                        "value": 38.634663,
                                        "description": "score(doc=117676,freq=9.0 = termFreq=9.0\n), product of:",
                                        "details": [
                                            {
                                                "value": 8.0,
                                                "description": "boost",
                                                "details": []
                                            },
                                            {
                                                "value": 2.4878378,
                                                "description": "idf, computed as log(1 + (docCount - docFreq + 0.5) / (docFreq + 0.5)) from:",
                                                "details": [
                                                    {
                                                        "value": 255.0,
                                                        "description": "docFreq",
                                                        "details": []
                                                    },
                                                    {
                                                        "value": 3074.0,
                                                        "description": "docCount",
                                                        "details": []
                                                    }
                                                ]
                                            },
                                            {
                                                "value": 1.9411767,
                                                "description": "tfNorm, computed as (freq * (k1 + 1)) / (freq + k1) from:",
                                                "details": [
                                                    {
                                                        "value": 9.0,
                                                        "description": "termFreq=9.0",
                                                        "details": []
                                                    },
                                                    {
                                                        "value": 1.2,
                                                        "description": "parameter k1",
                                                        "details": []
                                                    },
                                                    {
                                                        "value": 0.0,
                                                        "description": "parameter b (norms omitted for field)",
                                                        "details": []
                                                    }
                                                ]
                                            }
                                        ]
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        "value": 26.766226,
                        "description": "max of:",
                        "details": [
                            {
                                "value": 26.766226,
                                "description": "weight(short_description:致 in 117676) [PerFieldSimilarity], result of:",
                                "details": [
                                    {
                                        "value": 26.766226,
                                        "description": "score(doc=117676,freq=5.0 = termFreq=5.0\n), product of:",
                                        "details": [
                                            {
                                                "value": 8.0,
                                                "description": "boost",
                                                "details": []
                                            },
                                            {
                                                "value": 1.8858021,
                                                "description": "idf, computed as log(1 + (docCount - docFreq + 0.5) / (docFreq + 0.5)) from:",
                                                "details": [
                                                    {
                                                        "value": 466.0,
                                                        "description": "docFreq",
                                                        "details": []
                                                    },
                                                    {
                                                        "value": 3074.0,
                                                        "description": "docCount",
                                                        "details": []
                                                    }
                                                ]
                                            },
                                            {
                                                "value": 1.7741936,
                                                "description": "tfNorm, computed as (freq * (k1 + 1)) / (freq + k1) from:",
                                                "details": [
                                                    {
                                                        "value": 5.0,
                                                        "description": "termFreq=5.0",
                                                        "details": []
                                                    },
                                                    {
                                                        "value": 1.2,
                                                        "description": "parameter k1",
                                                        "details": []
                                                    },
                                                    {
                                                        "value": 0.0,
                                                        "description": "parameter b (norms omitted for field)",
                                                        "details": []
                                                    }
                                                ]
                                            }
                                        ]
                                    }
                                ]
                            }
                        ]
                    }
                ]
            }
        ]
    }
}

sum_num = 1.6619924 + 4.0 + 65.40089
print(sum_num)

tf_jin = 9.0 * 2.2 / 10.2
print(tf_jin)

print(2.4878378 * 8 * 1.9411767)

# --------------------
old_score = {
    "took": 22,
    "timed_out": False,
    "_shards": {
        "total": 8,
        "successful": 8,
        "failed": 0
    },
    "hits": {
        "total": 7928,
        "max_score": 61.39953,
        "hits": [{
            "_shard": 2,
            "_node": "CJ9-rLApQlaOCcQLL_TnEw",
            "_index": "gm-dbmw-service_ngram_v1",
            "_type": "service",
            "_id": "5837971",
            "_score": 61.39953,
            "_source": {
                "id": 5837971
            },
            "_explanation": {
                "value": 61.39953,
                "description": "sum of:",
                "details": [{
                    "value": 61.39953,
                    "description": "sum of:",
                    "details": [{
                        "value": 61.02436,
                        "description": "sum of:",
                        "details": [{
                            "value": 39.11938,
                            "description": "max of:",
                            "details": [{
                                "value": 39.11938,
                                "description": "weight(short_description:紧 in 117125) [PerFieldSimilarity], result of:",
                                "details": [{
                                    "value": 39.11938,
                                    "description": "score(doc=117125,freq=54.0), product of:",
                                    "details": [{
                                        "value": 0.72814745,
                                        "description": "queryWeight, product of:",
                                        "details": [{
                                            "value": 8.0,
                                            "description": "boost",
                                            "details": []
                                        }, {
                                            "value": 7.3109827,
                                            "description": "idf(docFreq=1102, maxDocs=607296)",
                                            "details": []
                                        }, {
                                            "value": 0.012449548,
                                            "description": "queryNorm",
                                            "details": []
                                        }]
                                    }, {
                                        "value": 53.724533,
                                        "description": "fieldWeight in 117125, product of:",
                                        "details": [{
                                            "value": 7.3484693,
                                            "description": "tf(freq=54.0), with freq of:",
                                            "details": [{
                                                "value": 54.0,
                                                "description": "termFreq=54.0",
                                                "details": []
                                            }]
                                        }, {
                                            "value": 7.3109827,
                                            "description": "idf(docFreq=1102, maxDocs=607296)",
                                            "details": []
                                        }, {
                                            "value": 1.0,
                                            "description": "fieldNorm(doc=117125)",
                                            "details": []
                                        }]
                                    }]
                                }]
                            }, {
                                "value": 8.30921,
                                "description": "weight(closure_tags:紧 in 117125) [PerFieldSimilarity], result of:",
                                "details": [{
                                    "value": 8.30921,
                                    "description": "score(doc=117125,freq=39.0), product of:",
                                    "details": [{
                                        "value": 0.18201429,
                                        "description": "queryWeight, product of:",
                                        "details": [{
                                            "value": 2.0,
                                            "description": "boost",
                                            "details": []
                                        }, {
                                            "value": 7.310076,
                                            "description": "idf(docFreq=1103, maxDocs=607296)",
                                            "details": []
                                        }, {
                                            "value": 0.012449548,
                                            "description": "queryNorm",
                                            "details": []
                                        }]
                                    }, {
                                        "value": 45.651413,
                                        "description": "fieldWeight in 117125, product of:",
                                        "details": [{
                                            "value": 6.244998,
                                            "description": "tf(freq=39.0), with freq of:",
                                            "details": [{
                                                "value": 39.0,
                                                "description": "termFreq=39.0",
                                                "details": []
                                            }]
                                        }, {
                                            "value": 7.310076,
                                            "description": "idf(docFreq=1103, maxDocs=607296)",
                                            "details": []
                                        }, {
                                            "value": 1.0,
                                            "description": "fieldNorm(doc=117125)",
                                            "details": []
                                        }]
                                    }]
                                }]
                            }]
                        }, {
                            "value": 21.904978,
                            "description": "max of:",
                            "details": [{
                                "value": 21.904978,
                                "description": "weight(short_description:致 in 117125) [PerFieldSimilarity], result of:",
                                "details": [{
                                    "value": 21.904978,
                                    "description": "score(doc=117125,freq=22.0), product of:",
                                    "details": [{
                                        "value": 0.6820049,
                                        "description": "queryWeight, product of:",
                                        "details": [{
                                            "value": 8.0,
                                            "description": "boost",
                                            "details": []
                                        }, {
                                            "value": 6.8476877,
                                            "description": "idf(docFreq=1752, maxDocs=607296)",
                                            "details": []
                                        }, {
                                            "value": 0.012449548,
                                            "description": "queryNorm",
                                            "details": []
                                        }]
                                    }, {
                                        "value": 32.118504,
                                        "description": "fieldWeight in 117125, product of:",
                                        "details": [{
                                            "value": 4.690416,
                                            "description": "tf(freq=22.0), with freq of:",
                                            "details": [{
                                                "value": 22.0,
                                                "description": "termFreq=22.0",
                                                "details": []
                                            }]
                                        }, {
                                            "value": 6.8476877,
                                            "description": "idf(docFreq=1752, maxDocs=607296)",
                                            "details": []
                                        }, {
                                            "value": 1.0,
                                            "description": "fieldNorm(doc=117125)",
                                            "details": []
                                        }]
                                    }]
                                }]
                            }, {
                                "value": 5.8386693,
                                "description": "weight(closure_tags:致 in 117125) [PerFieldSimilarity], result of:",
                                "details": [{
                                    "value": 5.8386693,
                                    "description": "score(doc=117125,freq=25.0), product of:",
                                    "details": [{
                                        "value": 0.17051545,
                                        "description": "queryWeight, product of:",
                                        "details": [{
                                            "value": 2.0,
                                            "description": "boost",
                                            "details": []
                                        }, {
                                            "value": 6.8482585,
                                            "description": "idf(docFreq=1751, maxDocs=607296)",
                                            "details": []
                                        }, {
                                            "value": 0.012449548,
                                            "description": "queryNorm",
                                            "details": []
                                        }]
                                    }, {
                                        "value": 34.24129,
                                        "description": "fieldWeight in 117125, product of:",
                                        "details": [{
                                            "value": 5.0,
                                            "description": "tf(freq=25.0), with freq of:",
                                            "details": [{
                                                "value": 25.0,
                                                "description": "termFreq=25.0",
                                                "details": []
                                            }]
                                        }, {
                                            "value": 6.8482585,
                                            "description": "idf(docFreq=1751, maxDocs=607296)",
                                            "details": []
                                        }, {
                                            "value": 1.0,
                                            "description": "fieldNorm(doc=117125)",
                                            "details": []
                                        }]
                                    }]
                                }]
                            }]
                        }]
                    }, {
                        "value": 0.31292006,
                        "description": "weight(is_online:T in 117125) [PerFieldSimilarity], result of:",
                        "details": [{
                            "value": 0.31292006,
                            "description": "score(doc=117125,freq=1.0), product of:",
                            "details": [{
                                "value": 0.06241565,
                                "description": "queryWeight, product of:",
                                "details": [{
                                    "value": 5.0134873,
                                    "description": "idf(docFreq=10973, maxDocs=607296)",
                                    "details": []
                                }, {
                                    "value": 0.012449548,
                                    "description": "queryNorm",
                                    "details": []
                                }]
                            }, {
                                "value": 5.0134873,
                                "description": "fieldWeight in 117125, product of:",
                                "details": [{
                                    "value": 1.0,
                                    "description": "tf(freq=1.0), with freq of:",
                                    "details": [{
                                        "value": 1.0,
                                        "description": "termFreq=1.0",
                                        "details": []
                                    }]
                                }, {
                                    "value": 5.0134873,
                                    "description": "idf(docFreq=10973, maxDocs=607296)",
                                    "details": []
                                }, {
                                    "value": 1.0,
                                    "description": "fieldNorm(doc=117125)",
                                    "details": []
                                }]
                            }]
                        }]
                    }, {
                        "value": 0.06224774,
                        "description": "Score based on child doc range from 117100 to 117124",
                        "details": []
                    }]
                }, {
                    "value": 0.0,
                    "description": "match on required clause, product of:",
                    "details": [{
                        "value": 0.0,
                        "description": "# clause",
                        "details": []
                    }, {
                        "value": 0.012449548,
                        "description": "#*:* -_type:__*, product of:",
                        "details": [{
                            "value": 1.0,
                            "description": "boost",
                            "details": []
                        }, {
                            "value": 0.012449548,
                            "description": "queryNorm",
                            "details": []
                        }]
                    }]
                }]
            },
            "inner_hits": {
                "sku_list": {
                    "hits": {
                        "total": 2,
                        "max_score": None,
                        "hits": [{
                            "_index": "gm-dbmw-service_ngram_v1",
                            "_type": "service",
                            "_id": "5837971",
                            "_nested": {
                                "field": "sku_list",
                                "offset": 0
                            },
                            "_score": None,
                            "_source": {
                                "sku_id": 515766,
                                "sku_rank": 0,
                                "end_time": "2029-06-10T12:19:56+08:00",
                                "price_type": 0,
                                "start_time": "2019-06-10T12:19:56+08:00",
                                "name_by_standard_analyzer": "第四代热玛吉.紧致抗衰.全面部",
                                "price": 7800,
                                "name": "第四代热玛吉.紧致抗衰.全面部"
                            },
                            "sort": [2.2360678, 7800]
                        }]
                    }
                }
            }
        }]
    }
}

import math
print(1+math.log(607269/1103))