#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'多线程'

__author__ = 'Ma Yanqiong'

import os
from multiprocessing import Process

print('Process (%s) start...' % os.getpid())
# Only works on Unix/Linux/Mac:
pid = os.fork()  # 返回了两次
if pid == 0:
    print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
else:
    print('I (%s) just created a child process (%s).' % (os.getpid(), pid))

print('========== 华丽的分割线 ==============')

def run_proc(name):
    '子进程要执行的代码'
    print('Run child process %s (%s)... [My parent is (%s)]' % (name, os.getpid(), os.getppid()))

print('Parent process %s.' % os.getpid())
print('Child process (%s)  will start.' % (os.getpid()))
P = Process(target=run_proc, args=('test',))
P.start()
P.join()
# join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步。
print('Child process (%s) end.' % (os.getpid()))

if __name__ == '__main__':
    pass
