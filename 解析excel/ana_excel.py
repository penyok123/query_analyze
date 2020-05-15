#!/usr/bin/env python
# -*- coding: utf-8 -*-
import redis
import json
import redis
from django.conf import settings

data = open("second_demands", "r", encoding="utf-8")

all_data = []
for item in data:
    word = item.strip()
    all_data.append(word)

print(all_data)
print(len(all_data))