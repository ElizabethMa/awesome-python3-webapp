#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'线程池'

__author__ = 'Ma Yanqiong'

import subprocess

print('$ nslookup www.python.org')
RESULT = subprocess.call(['nslookup', 'www.python.org'])
print('Exit code:', RESULT)

print('$ nslookup')
# set q=mx
# python.org
# exit
SUB = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, \
stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output, err = SUB.communicate(b'set q=mx\npython.org\nexit\n')
print(output.decode('utf-8'))
print('Exit code:', SUB.returncode)
