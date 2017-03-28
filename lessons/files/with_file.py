#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
操作文件和目录
'''

from datetime import datetime
import os

with open('test.txt', 'w') as f:
    f.write('今天是 ')
    f.write(datetime.now().strftime('%Y-%m-%d'))

with open('test.txt', 'r') as f:
    s = f.read()
    print('open for read...')
    print(s)

with open('test.txt', 'rb') as f:
    s = f.read()
    print('open as binary for read...')
    print(s)


# 利用os模块编写一个能实现 dir -l 输出的程序。

PWD = os.path.abspath('.')

print('      Size     Last Modified  Name')
print('------------------------------------------------------------')

for f in os.listdir('.'):
    fsize = os.path.getsize(f)
    mtime = datetime.fromtimestamp(os.path.getmtime(f)).strftime('%Y-%m-%d %H:%M')
    flag = '/' if os.path.isdir(f) else ''
    print('%10d  %s  %s%s' % (fsize, mtime, f, flag))

# 编写一个程序，能在当前目录以及当前目录的所有子目录下查找文件名包含指定字符串的文件，并打印出相对路径。

SEARCH_STR = input('请输入想搜索的字符串: ')

# 查找当前目录下所有包含关键字的文件
# def findFile(dir, filekw):
    # return [x for x in os.listdir(dir) if os.path.split(x)[1].find(filekw) > -1]

# 获取指定目录下的次级目录
# def findDir(path):
    # return [os.path.join(path, x) for x in os.listdir(path) if SEARCH_STR(os.path.join(path, x))]

# 遍历所有子目录文件
def listAll(p, k):
    '遍历所有子目录文件'
    if os.path.isdir(p):
        for f in os.listdir(p):
            listAll(os.path.join(p, f), k)
    elif os.path.isfile(p):
        if os.path.split(p)[1].find(k) > -1:
            print(p)

print('搜索结果 \'%s\' : ' % (SEARCH_STR))

listAll('.', SEARCH_STR)

