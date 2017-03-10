#!/usr/bin/env python3
# -*- coding: utf-8 -*-

r'''
features
'''
import os
from collections import Iterable
from collections import Iterator

# 切片 (list tuple str)
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
print(L[0:3]) # 从索引 0开始取，直到索引 3 为止，但不包括索引 3
print(L[:3]) # 第一个索引是 0，可以省略
print(L[1:3]) # 索引 1 开始，取出 2 个元素
print(L[-2:-1]) # 倒数第一个元素的索引是 -1
print(L[-2:]) # 取出最后 2 个元素

L = list(range(100))
print(L[:10]) # 前 10 个数
print(L[-10:]) # 后 10 个数
print(L[10:20]) # 前 11-20 个数
print(L[0:20:2]) # 前 20 个数，每两个取一个
print(L[::5]) # 所有数，每 5 个取一个
print(L[:]) # 复制 list

T = tuple(range(10)) # tuple 切片操作结果仍是 tuple
print(T[:3]) # 取出前 3 个元素

print('ABCDEFG'[:3]) # str 切片操作结果仍是字符串
print('ABCDEFG'[::2])

# 迭代(Iteration) `for ... in`
# 判断可迭代对象(Iterable) from collections import Iterable

isinstance('abc', Iterable)
isinstance([1, 2, 3], Iterable)
isinstance(123, Iterable)

DICT = {'a': 1, 'b': 2, 'c': 3}
for key in DICT:
    print(key)
for value in DICT.values():
    print(value)
for key, value in DICT.items():
    print(key, value)

# 怎么样取得下标
# Python 内置的 enumerate 函数可以把一个 list 变成 索引-元素对
for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)

# 列表生成器

# 生成列表
print(list(range(10)))
print([x for x in range(10)])

LIST = [x * x for x in range(1, 11)]
print(LIST) # 1 - 10 平方
LIST = [x * x for x in range(1, 11) if x % 2 == 0]
print(LIST) # 1 - 10 中偶数的平方
LIST = [m + n for m in 'ABC' for n in 'XYZ']
print(LIST) # 两层循环全排列

# 列出当前目录下的所有文件和目录名
DIRS = [d for d in os.listdir('.')]
print(DIRS)

# 使用两个变量生成 list
LIST = [k + '=' + str(v) for k, v in DICT.items()]
print(LIST)

L = ['Hello', 'World', 'IBM', 'Apple']
LIST = [s.lower() for s in L] # 把 list 中所有的字符串变成小写
print(LIST)

L1 = ['Hello', 'World', 18, 'Apple', None] # 不同类型
L2 = [s.lower() for s in L1 if isinstance(s, str)]
print(L2)

# 生成器(generator)
G = (x * x for x in range(10))
# 通过 next() 函数获得 generator 的下一个返回值
print(next(G))
print(next(G)) # 最后一个之后调用 next() 会抛出 StopIteration 错误

for num in G:
    print(num)

# 斐波拉契数列
def fib(max_num):
    '''
    定义generator的另一种方法: 函数定义中包含 yield 关键字，那么这个函数就不再是一个普通函数，而是一个 generator
    '''
    n_num, a_num, b_num = 0, 0, 1
    while n_num < max_num:
        yield b_num
        a_num, b_num = b_num, a_num + b_num
        n_num = n_num + 1

F = fib(6)
while True:
    try:
        X = next(F)
        print('g:', X)
    except StopIteration as error:
        print('Generator return value:', error.value)
        break

def triangles():
    '''
    print 杨辉三角
    '''
    list_res = []
    while True:
        list_res.insert(0, 1)
        index = 1
        while index < (len(list_res) - 1):
            list_res[index] = list_res[index] + list_res[index + 1]
            index = index + 1
        yield list_res

# 期待输出:
# [1]
# [1, 1]
# [1, 2, 1]
# [1, 3, 3, 1]
# [1, 4, 6, 4, 1]
# [1, 5, 10, 10, 5, 1]
# [1, 6, 15, 20, 15, 6, 1]
# [1, 7, 21, 35, 35, 21, 7, 1]
# [1, 8, 28, 56, 70, 56, 28, 8, 1]
# [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]

nn = 0
for t in triangles():
    print(t)
    nn = nn + 1
    if nn == 10:
        break

# 迭代器



