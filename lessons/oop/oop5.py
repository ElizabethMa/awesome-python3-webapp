#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'枚举类'

__author__ = 'Ma Yanqiong'

from enum import Enum, unique

MONTH = Enum('Month', \
('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))


print(MONTH)
print(MONTH.Jan)
print(MONTH.__members__)

for name, member in MONTH.__members__.items():
    print(name, '=>', member, ',', member.value)
# value 属性则是自动赋给成员的 int 常量，默认从 1 开始计数

# @unique 装饰器可以帮助我们检查保证没有重复值
@unique
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

# 访问的方法
D1 = Weekday.Mon
print(D1)
print(Weekday.Mon)
print(Weekday['Mon'])
print(Weekday.Mon.value)
print(D1 == Weekday.Mon)
print(D1 == Weekday.Tue)
print(Weekday(1))
print(D1 == Weekday(1))

for name, member in Weekday.__members__.items():
    print(name, '=>', member)
