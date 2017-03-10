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
    练习题: 解一元二次方程
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


# 函数参数 参数类型检查
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

# 位置参数(必选参数)

def power(x):
    return x * x

# 默认参数
def power_advanced(x, n = 2):
    '''
    1 必选参数在前，默认参数在后
    2 默认参数必须指向不变对象  
    '''
    summ = 1
    while n > 0:
        n = n - 1
        summ = summ * x
    return summ

power_advanced(5) # 25
power_advanced(5, 3) # 125

def enroll(name, gender, age=6, city='Beijing'):
    '''
    默认参数顺序与函数提供的顺序不一样时，要把参数名写上。
    '''
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)

enroll('Sarah', 'F')
enroll('Bob', 'M', 7)
enroll('Adam', 'M', city='Tianjin')

def add_end(line=[]):
    '''
    默认参数要指向不可变对象，函数定义的时候，就分配好了 line 指向的地址，
    每次函数调用的时候，都会修改 line 指向的地址存放的内容，而 line 本身没有改变
    '''
    line.append('END')
    return line

add_end([1, 2, 3]) # [1, 2, 3, 'END']
add_end() # ['END']
add_end() # ['END', 'END']
add_end() # ['END', 'END', 'END']

def add_to_end(line=None):
    '''
    str None 都是不可变对象
    '''
    if line is None:
        line = []
    line.append('END')
    return line

add_to_end() # ['END']
add_to_end() # ['END']
add_to_end() # ['END']

# 可变参数

def calc(*numbers):
    '''
    参数 numbers 接收到的是一个 tuple
    调用该函数时，可以传入任意个参数，包括 0 个参数
    '''
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

calc(1,2,3)
calc()
nums = [1, 2, 3]
calc(*nums) # *nums 表示把 nums 这个 list 的所有元素作为可变参数传进去
nums = (1, 2, 3)
calc(*nums)

# 关键字参数
# 可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个 `tuple`(有序不可变列表)。
# 而关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个 `dict`(无序 k-v 对)。

def person(name, age, **kw):
    print('name:', name, ', age:', age, ', other:', kw)

person('Michael', 30) 
# name: Michael , age: 30 , other: {}
person('Bob', 35, city='Beijing') 
# name: Bob , age: 35 , other: {'city': 'Beijing'}
person('Adam', 45, gender='M', job='Engineer')
# name: Adam , age: 45 , other: {'gender': 'M', 'job': 'Engineer'}
extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, **extra)
# name: Jack , age: 24 , other: {'city': 'Beijing', 'job': 'Engineer'}

# `**extra` 表示把 extra 这个 dict 的所有 key-value 用关键字参数传入到函数的 `**kw` 参数，`**kw` 将获得 `**extra` 的一份 copy

# 命名关键字参数
# 如果要限制关键字参数的名字，就可以用命名关键字参数，例如，只接收city和job作为关键字参数。这种方式定义的函数如下：
def person(name, age, *, city, job):
    '''
    命名关键字参数需要一个特殊分隔符 * ，* 后面的参数被视为命名关键字参数。
    '''
    print(name, age, city, job)

person('Jack', 24, city='Beijing', job='Engineer')

def person(name, age, *args, city, job):
    '''
    如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符 * 了
    '''
    print(name, age, args, city, job)

# 命名关键字参数必须传入参数名，这和位置参数不同。如果没有传入参数名，调用将报错
person('Jack', 24, 'Beijing', 'Engineer') # error

def person(name, age, *, city='Beijing', job):
    '''
    命名关键字参数可以有缺省值, 调用时不用出入此参数
    '''
    print(name, age, city, job)

person('Jack', 24, job='Engineer')

# 参数组合
# 参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
# 在函数调用的时候，Python解释器自动按照参数位置和参数名把对应的参数传进去。
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)

# 通过一个 tuple 和 dict，你也可以调用上述函数

args = (1, 2, 3, 4)
kw = {'d': 99, 'x': '#'}
f1(*args, **kw)
# a = 1 b = 2 c = 3 args = (4,) kw = {'d': 99, 'x': '#'}

args = (1, 2, 3)
kw = {'d': 88, 'x': '#'}
f2(*args, **kw)
# a = 1 b = 2 c = 3 d = 88 kw = {'x': '#'}

# 对于任意函数，都可以通过类似 `func(*args, **kw)` 的形式调用它，无论它的参数是如何定义的。
# `*args` 是可变参数，`args` 接收的是一个 `tuple`；`**kw`是关键字参数，`kw` 接收的是一个 `dict`。

# 递归函数
def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)
        
# 尾递归优化
def fact(n):
    return fact_iter(n, 1)

def fact_iter(num, product):
    '''
    尾递归优化，尾递归是指，在函数返回的时候，调用自身本身，并且，return语句不能包含表达式。
    '''
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)

