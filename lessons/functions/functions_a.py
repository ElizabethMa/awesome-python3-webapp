#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''函数高级'''

from functools import reduce

# 1 map/reduce

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
        print(m_a * m_b)
        return m_a * m_b
    return reduce(mult, list_param)

print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))

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


# 2 filter



# 3 sorted


