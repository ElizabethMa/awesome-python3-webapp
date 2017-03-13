#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""偏函数 -  Partial Functions"""

import functools

print(int('12345'))
print(int('12345', base=8))

# 固定函数转换为 二进制
int_to_2 = functools.partial(int, base=2)

print(int_to_2('101010')) # 42
print(int_to_2('101010', base=10)) # 101010

# 创建偏函数时，实际上可以接收 函数对象、*args 和 **kw 这 3 个参数

#  base=2 表示 {base： 2} 作为 **kw 这个参数
print(int_to_2('101010')) # 42
kw = { 'base': 2 }
print('相当于', int('101010', **kw)) # 42

max_with_10 = functools.partial(max, 10) # 10 作为 *args 的一部分自动加到左边
print(max_with_10(1, 3, 5))
print('相当于', max_with_10(10, 1, 3, 5))

