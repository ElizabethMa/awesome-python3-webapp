#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'进程间通信'

__author__ = 'Ma Yanqiong'

from multiprocessing import Process, Queue
import os
import time
import random

def write(q):
    '写进程执行的代码'
    print('Process to wirte: %s' % os.getpid())
    for value in ['A', 'B', 'C']:
        print('Put %s to queue...' % value)
        q.put(value)
        time.sleep(random.random())

def read(q):
    '读进程执行的代码'
    print('Process to read: %s' % os.getpid())
    while True:
        value = q.get(True)
        print('Get %s from queue.' % value)

if __name__ == '__main__':
    # 父进程创建 Queue, 并传给各个子进程
    Q = Queue()
    PW = Process(target=write, args=(Q,))
    PR = Process(target=read, args=(Q,))
    PW.start()
    PR.start()
    PW.join()
    PR.terminate()

