#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""装饰器 - Decorator"""

import functools

def log(func):
    '''装饰器函数，在执行函数前打印信息'''
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

@log # 相当于执行了 now = log(now)
def now():
    print('2017-03-13')

now()

# Decorator 本身需要 参数

def log2(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@log2('execute') # now = log('execute')(now)
def now2():
    print('2017-03-13')

now2()

print(now.__name__) # wrapper
print(now2.__name__) # wrapper

# 解决函数名作变化的问题，有些依赖函数签名的代码执行就会出错

def log3(func):
    '''一个完整的decorator的写法'''
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

def log4(text):
    '''针对带参数的decorator'''
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

# 练习
# 请编写一个decorator，能在函数调用的前后打印出'begin call'和'end call'的日志。
# 再思考一下能否写出一个 @log 的 decorator，使它既支持： @log 又支持 @log('execute')

def logger(text):
    if callable(text):
        @functools.wraps(text)
        def wrapper(*args, **kw):
            print('begin %s %s():' % ('call', text.__name__))
            result = text(*args, **kw)
            print('end %s %s():' % ('call', text.__name__))
            return result
        return wrapper
    else:
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kw):
                print('begin %s %s():' % (text, func.__name__))
                result = func(*args, **kw)
                print('end %s %s():' % (text, func.__name__))
                return result
            return wrapper
        return decorator

@logger
def greet_en(name):
    print('hello,', name)

greet_en('yanqiong')

@logger('execute')
def greet_ch(name):
    print('你好,', name)

greet_ch('艳琼')

print(greet_en.__name__)
print(greet_ch.__name__)

hasattr(abs, '__call__')
callable(abs)
