#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''函数高级'''

from functools import reduce

# 1 map 返回 list / reduce 返回依次求值后的结果
print('=== list / reduce ===')

def normalize(name):
    '''
    把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字
    '''
    return name.capitalize()

L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

def prod(list_param):
    '''
    求积
    '''
    def mult(m_a, m_b):
        '''两个数的乘积'''
        return m_a * m_b
    return reduce(mult, list_param)

print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))

print('2 * 4 = %d, 2 ** 4 = %d' % (2 * 4, 2 ** 4))

def str2float(string_parma):
    '''
    把字符串'123.456'转换成浮点数123.456
    '''
    l_map = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    def ch2num(char):
        '''ch2num'''
        return l_map[char]
    def genint(big, small):
        '''得到整数'''
        return big * 10 + small
    dot_index = string_parma.index('.')
    string1, string2 = string_parma[:dot_index], string_parma[dot_index-len(string_parma)+1:]
    return reduce(genint, list(map(ch2num, string1))) \
        + reduce(genint, list(map(ch2num, string2))) * 0.1 ** len(string2)

print('str2float(\'123.456\') =', str2float('123.456'))


# 2 filter 过滤序列，过滤函数返回 True/False
# filter() 函数返回的是一个 Iterator，也就是一个惰性序列，所以要强迫 filter() 完成计算结果，需要用 list() 函数获得所有结果并返回 list。
print('=== filter ===')

def is_odd(num):
    '''判断奇数'''
    return num % 2 == 1
ODD_LIST = list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15]))
print('判断奇数', ODD_LIST)

def not_empty(string):
    '''去掉空字符串'''
    return string and string.strip()

NO_EMPTY = list(filter(not_empty, ['A', '', 'B', None, 'C', '  ']))
print('去掉空字符串', NO_EMPTY)

# 用 filter 求素数 埃氏筛法

def _odd_iter():
    '''生成从 3 开始的奇数数列，这是一个生成器，是无限序列，返回 Iterator。'''
    num = 1
    while True:
        num = num + 2
        yield num

def _not_divisible(num):
    '''筛选函数'''
    return lambda x: x %  num > 0

def primes():
    '''素数序列'''
    yield 2
    list_init = _odd_iter() # 初始序列
    while True:
        next_prime = next(list_init) # 返回序列的第一个数
        yield next_prime
        list_init = filter(_not_divisible(next_prime), list_init) # 构造新序列

print('start: 1000 以内素数')
for n in primes():
    if n < 1000:
        print(n)
    else:
        break
print('end: 1000 以内素数')

# 3 sorted

sorted([36, 5, -12, 9, -21]) # [-21, -12, 5, 9, 36]

# key 指定的函数将作用于 list 的每一个元素上，并根据 key 函数返回的结果进行排序

sorted([36, 5, -12, 9, -21], key=abs) # [5, 9, -12, -21, 36]

sorted(['bob', 'about', 'Zoo', 'Credit']) # ['Credit', 'Zoo', 'about', 'bob']

# 忽略大小写排列
sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower) # ['about', 'bob', 'Credit', 'Zoo']

# 要进行反向排序，不必改动key函数，可以传入第三个参数reverse=True：

sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True)
# ['Zoo', 'Credit', 'bob', 'about']

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
# 按名字排序
def by_name(stu):
    '''按名字排序, 返回名字'''
    return stu[0]

L1 = sorted(L, key=by_name)
print(L1)

# 按成绩从高到低排序
def by_score(stu):
    '''按成绩排序, 返回成绩'''
    return stu[1]

L2 = sorted(L, key=by_score, reverse=True)
print(L2)

# 返回函数 / 闭包

def calc_sum(*args):
    '''直接计算求和'''
    temp_sum = 0
    for num in args:
        temp_sum = temp_sum + num
    return temp_sum

def lazy_sum(*args):
    '''返回求和函数'''
    def  clac_sum():
        '''求和函数'''
        temp_sum = 0
        for num in args:
            temp_sum = temp_sum + num
        return temp_sum
    return clac_sum

MY_SUM1 = lazy_sum(1, 3, 5) # 返回求和函数
MY_SUM2 = lazy_sum(1, 3, 5) # 返回求和函数
print(MY_SUM1())
print('MY_SUM1 == MY_SUM2:', MY_SUM1 == MY_SUM2)

# 闭包
# 返回的函数在其定义内部引用了局部变量args，所以，当一个函数返回了一个函数后，其内部的 **局部变量** 还被新函数引用
# 返回的函数并没有立刻执行，而是直到调用了 f() 才执行。

def count1():
    '''返回的函数引用了局部变量 i , 在函数调用时 i 已经变成 3'''
    fun_s = []
    for i in range(1, 4):
        def fun():
            '''平方'''
            return i * i
        fun_s.append(fun)
    return fun_s

f1, f2, f3 = count1()

print(f1()) # 9
print(f2()) # 9
print(f3()) # 9

def count2():
    '''再定义一个函数接受循环变量'''
    def f(j):
        def g():
            return j * j
        return g
    fun_s = []
    for i in range(1, 4):
        fun_s.append(f(i))
    return fun_s

f1, f2, f3 = count2()

print(f1()) # 1
print(f2()) # 4
print(f3()) # 9

# 匿名函数 lambda
# 匿名函数有个限制，就是只能有一个表达式，不用写return，返回值就是该表达式的结果。
# 匿名函数也是一个函数对象
list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
# [1, 4, 9, 16, 25, 36, 49, 64, 81]

F = lambda x, y: x * y
print(F(2, 3)) # 6

def count2_new():
    '''把 count2 用 lambda 重写'''
    fun_s = []
    for i in range(1, 4):
        fun_s.append(lambda x: x * x(i))
    return fun_s

f1, f2, f3 = count2()

print(f1()) # 1
print(f2()) # 4
print(f3()) # 9
