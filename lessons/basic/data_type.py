#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""data_type"""

# 整数
print(100)
print('十六进制 0xff :', 0xff)

# 浮点数
print(1.23)
print(1.2e6)

# 字符串
print("I'm ok.", 'I\'m ok.')
# 转义字符 \n \t \\
print('I\'m learning\nPython.')
# r'' 表示 '' 内部字符不转义
print('\\\t\\')
print(r'\\\t\\')
# '''...''' 表示多行内容
print('''line1
line2
line3''')

# 单个字符的编码
# Python提供了 ord() 函数获取字符的整数表示， chr() 函数把编码转换为对应的字符：
print("ord('A') =", ord('A'))
print("ord('中') =", ord('中'))
print("chr(66) =", chr(66))
print("chr(25991) =", chr(25991))
print(r"'\u4e2d\u6587' =", '\u4e2d\u6587') # 十六进制

# str vs bytes
# Python的字符串类型是str，在内存中以Unicode表示，一个字符对应若干个字节。如果要在网络上传输，或者保存到磁盘上，就需要把str变为以字节为单位的bytes。
# Python 对 bytes 类型的数据用带 b 前缀的单引号或双引号表示
print(b'ABC')
# print(b'中文') # error
print('ABC'.encode('ascii'))
print('中文'.encode('utf-8')) # b'\xe4\xb8\xad\xe6\x96\x87'
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')) # 中文
print(len('ABC')) # 3
print(len('中文')) # 2
print(len('中文'.encode('utf-8'))) # 6
print(len(b'\xe4\xb8\xad\xe6\x96\x87')) # 6


# 格式化输出占位符
print('Hello, %s' % 'world!')
print('Hello, %s, you have $%d' % ('world!', 2000))
# %s 字符串
# %d 整数 %f 浮点数 %x 十六进制数 --- 整数可以指定是否补零， 浮点数可以指定小数位数
print('%3d, %03d, %03d' % (3, 5, 77))
print('%.2f, %.1f, %.1f' % (3, 5, 77))
print('0x%x' % (77))
R = (85 - 72) / 72 * 100
print('%.1f%%' % R) # 18.1%

# 布尔值
# True False and or not
print(True, False)
print('1 > 4 :', 1 > 4)
print(True and False, True or False, not True)

# 空值
# None
print(None)

# 变量
# python 是动态语言
A = 'ABC'
B = A
A = 'XYZ'
print('A ->', A, ', B ->', B)

# 常量
# 在 Python 中，通常用全部大写的变量名表示常量
PI = 3.14159265359

# 除法
print('10 / 3 =', 10 / 3)
print('11 / 3 =', 11 / 3)
print('10 // 3 =', 10 // 3) # 地板除
print('11 // 3 =', 11 // 3)
print('10 % 3 =', 10 % 3)
print('11 % 3 =', 11 % 3)
