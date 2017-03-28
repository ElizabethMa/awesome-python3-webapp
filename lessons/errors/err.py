#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'pdb 调试'

__author__ = 'Ma Yanqiong'

# python3 -m pdb err.py

import pdb

s = '0'
n = int(s)
pdb.set_trace() # 运行到这里会自动暂停
print(10 / n)
