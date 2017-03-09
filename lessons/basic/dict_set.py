#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""dict and set"""

# dict {key:value} 无序
D = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
D['Adam'] = 67
print(D)

# 判断 key 是否存在
print('Thomas' in D) # False
print(D.get('Thomas')) # None
print(D.get('Thomas', -1)) # -1, 不存在就返回指定值

# 删除 key
D.pop('Adam')
print(D)

# list vs dict:
# dict(用空间来换取时间) 查找和插入的速度极快，不会随着key的增加而变慢；
# dict 需要占用大量的内存，内存浪费多。
# list 查找和插入的时间随着元素的增加而增加；
# list 占用空间小，浪费内存很少。

# dict 的 key 必须是不可变对象, 通过对 key 哈希算法（Hash）计算存储位置
# 在 Python 中，字符串、整数等都是不可变的

# set 一组 key 的集合, 不存储 value, key 不可以重复 无序
# set 的 key 也必须是不可变对象
S = set([1, 2, 3])
print(S)
S = set([1, 1, 2, 3, 3])
print(S)
S.add(4) # 添加元素
print(S)
S.remove((4)) # 删除元素
print(S)

# set 可以做集合运算
S1 = set([1, 2, 3])
S2 = set([2, 3, 4])
print(S1 & S2) # 交集
print(S1 | S2) # 并集

# 对于 str 来说，str 是不变对象，调用对象自身的任何方法，都不会改变该对象自身的内容。相反，这些方法会创建新的对象并返回
A = 'abc'
B = A.replace('a', 'A')
print('A: %s, B: %s' % (A, B))
