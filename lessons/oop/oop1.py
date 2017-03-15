#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'类 实例 继承 多态'

__author__ = 'Ma Yanqiong'

import sys
import types

class Animal(object):
    'class Animal'
    def run(self):
        'Animal.run()'
        print('Animal is running ...')

class Dog(Animal):
    '继承 Animal'
    def run(self):
        'Dog.run() 子类的run()覆盖了父类的run()'
        print('Dog is running ...')

class Cat(Animal):
    '继承 Animal'
    def run(self):
        'Cat.run() 子类的run()覆盖了父类的run()'
        print('Cat is running ...')

animal = Animal()
animal.run()

dog = Dog()
dog.run()

cat = Cat()
cat.run()

print(isinstance(dog, list)) # False
print(isinstance(dog, Dog)) # True
print(isinstance(dog, Animal)) # True
print(isinstance(animal, Animal)) # True
print(isinstance(animal, Dog)) # False

# 多态
# 对扩展开放, 对修改封闭

def run_twice(animal):
    '多态'
    animal.run()
    animal.run()

run_twice(Animal())
run_twice(Dog())

# 动态语言的鸭子类型特点决定了继承不像静态语言那样是必须的。

# 获取对象信息 - type()
print(type(123)) # <class 'int'>
print(type('string')) # <class 'str'>
print(type(None)) # <class 'NoneType'>
print(type(abs)) # <class 'builtin_function_or_method'>
print(type(Animal)) # <class 'type'>
print(type(Dog)) # <class 'type'>
print(type(animal)) # <class '__main__.Animal'>
print(type(dog)) # <class '__main__.Dog'>
print(type(run_twice)) # <class 'function'>

print(type(123) == int) # True
print(type(123) == type(456)) # True
print(type('abc') == type('123')) # True
print(type('abc') == str) # True
print(type('abc') == type(123)) # False
print(type(run_twice) == types.FunctionType) # True
print(type(abs) == types.BuiltinFunctionType) # True
print(type(lambda x: x) == types.LambdaType) # True
print(type((x for x in range(10))) == types.GeneratorType) # True

# 获取对象信息 - isinstance()

# 获取对象信息 - dir()
# dir() - 获得一个对象的所有属性和方法

print(dir(123))

# 类属性与实例属性

class Student(object):
    'class Student'
    name = 'Student'

s = Student()
print(s.name) # Student
print(Student.name) # Student
s.name = 'Asa'
print(s.name) # Asa
print(Student.name) # Student
del s.name
print(s.name) # Student
print(Student.name) # Student

def test():
    'test func'
    args = sys.argv
    if len(args) == 1:
        print('Hello, world!')
    elif len(args) == 2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')

if __name__ == '__main__':
    test()
