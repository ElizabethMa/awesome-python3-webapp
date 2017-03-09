#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""list_tuple"""

# list 是一个可变的有序列表 []
# tuple 元组，不可变的有序列表 ()

classmates = ['Michael', 'Bob', 'Tracy']
print(len(classmates))
print(classmates[0])
print(classmates[-1])
print(classmates[-2])
print(classmates[-3])

classmates.append('Adam') # 末尾追加
print(classmates)
classmates.insert(1, 'Jack') # 指定位置追加
print(classmates)
classmates.pop() # 删除末尾元素
print(classmates)
classmates.pop(1) # 删除指定位置元素
print(classmates)
classmates[1] = 'Apple' # 替换元素
print(classmates)

# list里面的元素的数据类型也可以不同
L = ['Apple', 123, True]
print(L)

# tuple
MATES = ('Michael', 'Bob', 'Tracy')
T = (1, 2)
print(T, T[0], T[1])

T = (1) # 计算出括号里面的数字值，按小括号计算
print(T)

T = (1,) # 定义只有一个元素的 tuple， 加 ,
print(T)

T = () # 定义空 tuple
print(T)

# “可变” tuple
T = ('a', 'b', ['A', 'B'])
print(T)
T[2][0] = 'C'
T[2][1] = 'D'
print(T) # 只是 T[2] 的指向不会变
