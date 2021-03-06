#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'练习 datetime'

# 假设你获取了用户输入的日期和时间如 2015-1-21 9:01:30，以及一个时区信息如 UTC+5:00，均是 str，请编写一个函数将其转换为 timestamp

import re
from datetime import datetime, timedelta, timezone

def to_timestamp(dt_str, tz_str):
    day = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
    hour_str = re.match(r'^UTC([+-]\d{1,2}):00', tz_str).group(1)
    hour_int = int(hour_str)
    tz_utc = timezone(timedelta(hours=hour_int)) # 创建时区UTC+8:00
    day = day.replace(tzinfo=tz_utc) 
    return day.timestamp()

t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
assert t1 == 1433121030.0, t1

t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
assert t2 == 1433121030.0, t2

print('Pass')
