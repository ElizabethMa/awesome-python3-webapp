#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''条件判断和循环'''

AGE = 3
if AGE >= 18:
    print('your age is', AGE)
    print('adult')
else:
    print('your age is', AGE)
    print('teenager')

if AGE >= 18:
    print('adult')
elif AGE >= 6:
    print('teenager')
else:
    print('kids')

A = input() # input 收到的是 str
BIRTH = int(A) # str 转 int
if BIRTH >= 2000:
    print('00 后')
else:
    print('00 前')

# 练习
height = 1.73
weight = 56
bmi = weight / height / height
print(bmi)
if bmi >= 32:
    print('严重肥胖')
elif bmi >= 28:
    print('肥胖')
elif bmi >= 25:
    print('过重')
elif bmi >= 18.5:
    print('正常')
else:
    print('过轻')


# 循环
# 1 for ... in
NAMES = ['Michael', 'Bob', 'Tracy']
for name in NAMES:
    print(name)

# range() 生成整数序列, 通过 list() 转换成 有序列表
print(list(range(5)))
# print(list(range(101)))

SUM = 0
for x in list(range(101)):
    SUM = SUM + x
print(SUM)

# 2 while
SUM = 0
N = 99
while N > 0:
    SUM += N
    N = N - 2
print(SUM)

# 3 break 提前结束循环
for x in list(range(101)):
    if x > 10:
        break
    print(x)
print('END')

# 4 continue 提前结束本轮循环，并直接开始下一轮循环
for x in list(range(15)):
    if x == 10:
        continue
    print(x)
print('END')
