#!/usr/bin/env python
# -*- coding: utf-8 -*-
import redis
import json
import redis
from django.conf import settings

import datetime

today = datetime.datetime.now() - datetime.timedelta(days=1)
lastday = str(datetime.datetime(today.year, today.month, today.day))
lastday = lastday.split(" ")
date_change = lastday[0]
print(date_change)
print(str(date_change))
print(type(date_change))
