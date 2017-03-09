#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''函数基础'''
import math

def my_abs(ori):
    '''
    example of define function
    如果没有 return 语句，返回 None
    return None 可以简写为 return
    '''
    if ori >= 0:
        return ori
    else:
        return -ori

Y = my_abs(-9)
print(Y)

# 空函数
def nop():
    '''
     定义一个什么也不做的 空函数
     pass 是占位符，可以让代码先运行起来
     if age >= 18:
         pass
    '''
    pass

# 检查参数
# 参数个数不对 python 解释器 可以自动检查出来
# my_abs (1, 2)

# 参数类型不对
def my_abs_2(ori):
    '''
    检查参数类型
    '''
    if not isinstance(ori, (int, float)):
        raise TypeError('bad operand type')
    if ori >= 0:
        return ori
    else:
        return -ori
# my_abs_2('A')

# 返回多个值
# import math
def move(orix, oriy, step, angle=0):
    '''
    默认参数 angle = 0
    返回值是一个 tuple ，在语法上，返回一个tuple可以省略括号
    '''
    resx = orix + step * math.cos(angle)
    resy = oriy + step * math.sin(angle)
    return resx, resy

X, Y = move(100, 100, 60, math.pi / 6) # 多个变量可以同时接收一个 tuple
R = move(100, 100, 60, math.pi / 6)
print(X, Y)
print(R)

def quadratic(p_a, p_b, p_c):
    r'''
    解一元二次方程
    一行代码太长了可以在前一行用 \ 连接
    '''
    if not (isinstance(p_a, (int, float)) and isinstance(p_b, (int, float)) and \
    isinstance(p_c, (int, float))):
        raise TypeError('Wrong Input Type!')
    if p_a == 0:
        if p_b == 0:
            if p_c == 0:
                print('无穷解')
                return 0, 0
            else:
                print('无解')
                return None, None
        else:
            return -p_c / p_b, None
    else:
        delta = p_b * p_b - 4 * p_a * p_c
        base = - p_b / p_a / 2
        if delta < 0:
            print('无解')
            return None, None
        elif delta == 0:
            return base, base
        else:
            return base + math.sqrt(delta)/ 2 / p_a, base - math.sqrt(delta) / 2 / p_a

# 测试:
print(quadratic(2, 3, 1)) # => (-0.5, -1.0)
print(quadratic(1, 3, -4)) # => (1.0, -4.0)
print(quadratic(0, 0, -4)) # => (1.0, -4.0)
