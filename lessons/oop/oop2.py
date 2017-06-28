#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'面向对象高级 __slots__'

__author__ = 'Ma Yanqiong'

from types import MethodType

class Student(object):
    'class Student'
    pass

S = Student()

# 动态给实例绑定方法
S.name = "Mic"
print(S.name)

def set_age(self, age):
    '定义一个函数作为实例方法'
    self.age = age

S.set_age = MethodType(set_age, S)
S.set_age(30)
print(S.age)

# 给一个实例绑定的方法，对另一个实例是不起作用的
S2 = Student()
# S2.set_age(30)
# # AttributeError: 'Student' object has no attribute 'set_age'

# 动态给类绑定方法
# 为了给所有实例都绑定方法，可以给 class 绑定方法
def set_score(self, score):
    '定义一个函数作为 class 方法'
    self.score = score

Student.set_score = set_score

S.set_score(100)
print(S.score)
S2.set_score(99)
print(S2.score)

# 使用 __slots__ 可以限制实例属性
# __slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的
# 除非在子类中也定义__slots__，这样，子类实例允许定义的属性就是自身的__slots__加上父类的__slots__。
# 只允许对 Kid 实例添加 name 和 age 属性
class Kid(object):
    __slots__ = ('name', 'age')

K = Kid()
K.name = 'nik'
K.age = 5
# K.score = 90
# AttributeError: 'Kid' object has no attribute 'score'
