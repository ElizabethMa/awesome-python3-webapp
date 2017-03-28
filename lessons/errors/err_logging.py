#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'记录错误'

__author__ = 'Ma Yanqiong'

import logging
import logging.config

def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    'Configure the logging system'
    # 使用硬编码的方式把 logging 配置写在程序中
    logging.basicConfig(
        filename='logs/app.log',
        level=logging.INFO,
        format='%(levelname)s:%(asctime)s:%(message)s'
        )

    # 使用配置文件
    logging.config.fileConfig('config/logconfig.ini')

    # Variables (to make the calls that follow work)
    hostname = 'www.python.org'
    item = 'spam'
    filename = 'data.csv'
    mode = 'r'

    # basicConfig() 在程序中只能被执行一次。
    # 如果你稍后想改变日志配置， 就需要先获取 root logger ，然后直接修改它。例如：
    logging.getLogger().level = logging.DEBUG

    # Example logging calls (insert into your program)
    logging.critical('Host %s unknown', hostname)
    logging.error("Couldn't find %r", item)
    logging.warning('Feature is deprecated')
    logging.info('Opening file %r, mode=%r', filename, mode)
    logging.debug('Got here')

    try:
        bar('0')
    except Exception as e:
        logging.exception(e)

main()
print('END')
