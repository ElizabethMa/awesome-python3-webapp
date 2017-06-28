#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'datetime'

from datetime import datetime, timedelta, timezone

print('\n===== 获取当前日期和时间 =====\n')
NOW = datetime.now()
print(NOW)
print(type(NOW))

print('\n===== 获取指定日期和时间 =====\n')
D = datetime(2015, 4, 19, 12, 20)
print(D)

print('\n===== datetime 转换为 timestamp =====\n')
D = datetime(2017, 4, 1, 8, 20)
print(D.timestamp())
# Python 的 timestamp 是一个浮点数。如果有小数位，小数位表示毫秒数。

print('\n===== timestamp 转换为 datetime =====\n')
T = 1491006000.0
print(datetime.fromtimestamp(T)) # 本地时间
print(datetime.utcfromtimestamp(T)) # UTC时间

print('\n===== str 转换为 datetime =====\n')
DAY = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
print(DAY) # 转换后的 datetime 是没有时区信息的

print('\n===== datetime 转换为 str =====\n')
print(NOW.strftime('%a, %b %d %H:%M'))
# https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior

print()
print(NOW + timedelta(hours=10))
print(NOW - timedelta(hours=10))
print(NOW - timedelta(days=5, hours=10))

print('\n===== 本地时间转换为 UTC 时间 =====\n')
# 本地时间是指系统设定时区的时间，例如北京时间是UTC+8:00时区的时间，而UTC时间指UTC+0:00时区的时间。
# 一个 datetime 类型有一个时区属性 tzinfo ，但是默认为 None，所以无法区分这个datetime到底是哪个时区，除非强行给datetime设置一个时区：
tz_utc_8 = timezone(timedelta(hours=8)) # 创建时区UTC+8:00
print(tz_utc_8)
DT = NOW.replace(tzinfo=tz_utc_8) # 强制设置为UTC+8:00
# 如果系统时区恰好是UTC+8:00，那么上述代码就是正确的，否则，不能强制设置为UTC+8:00时区。
print(DT)

print('\n===== 时区转换 =====\n')
# 我们可以先通过 utcnow() 拿到当前的UTC时间，再转换为任意时区的时间
# 拿到 UTC 时间，并强制设置时区为UTC+0:00:
utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
print('UTC 时间：', utc_dt)
# astimezone()将转换时区为北京时间:
BJ_DT = utc_dt.astimezone(timezone(timedelta(hours=8)))
print('UTC 时间转换为北京时间：', BJ_DT)

# astimezone()将转换时区为东京时间:
tokyo_dt = utc_dt.astimezone(timezone(timedelta(hours=9)))
print('UTC 时间转换为东京时间：', tokyo_dt)

# astimezone()将 bj_dt 转换时区为东京时间:
tokyo_dt2 = BJ_DT.astimezone(timezone(timedelta(hours=9)))
print('北京时间转换为东京时间：', tokyo_dt2)

# 时区转换的关键在于，拿到一个datetime时，要获知其正确的时区，然后强制设置时区，作为基准时间。
# 利用带时区的datetime，通过astimezone()方法，可以转换到任意时区。
