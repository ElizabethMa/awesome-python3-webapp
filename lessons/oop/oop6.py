#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'元类'

__author__ = 'Ma Yanqiong'

class Hello(object):
    def hello(self, name='world'):
        print('Hello, %s.' % name)

h = Hello()
h.hello()
print(type(Hello)) # class 的 类型是 type
print(type(h))

# type()函数既可以返回一个对象的类型，又可以创建出新的类型
def fn(self, name='world'):
    print('Hello, %s.' % name)

Hello2 = type('Hello2', (object,), dict(hello=fn)) # 创建 Hello2 class
H = Hello2()
H.hello()
print(type(Hello2)) # class 的 类型是 type
print(type(H))

# 要创建一个class对象，type()函数依次传入3个参数：
# class 的名称；
# 继承的父类集合，注意 Python 支持多重继承，如果只有一个父类，别忘了 tuple 的单元素写法；
# class 的方法名称与函数绑定，这里我们把函数 fn 绑定到方法名 hello 上。

# metaclass
# 先定义 metaclass，然后创建类。
# 先定义类，然后创建实例。

# metaclass是类的模板，所以必须从`type`类型派生：
class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)

class MyList(list, metaclass=ListMetaclass):
    pass

# 当我们传入关键字参数metaclass时，魔术就生效了，它指示Python解释器在创建MyList时，要通过
# ListMetaclass.__new__() 来创建，在此，我们可以修改类的定义，比如，加上新的方法，然后，返回修改后的定义。

# __new__()方法接收到的参数依次是：
# 当前准备创建的类的对象；
# 类的名字；
# 类继承的父类集合；
# 类的方法集合。

L = MyList()
L.add(1)
L.add(2)
L.add(3)
L.add('END')
print(L)




