#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'定制类'

__author__ = 'Ma Yanqiong'

class Student(object):
    '__str__ __repr__'
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Student object (name: %s)' % self.name

    __repr__ = __str__

    def __getattr__(self, attr):
        if attr=='score':
            return 99
        if attr=='age':
            return lambda: 25
        raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)

    def __call__(self):
        print('My name is %s.' % self.name)

print(Student('Michael'))

s = Student('Michael')
print(s.name)
print(s.score)
print(s.age())
# AttributeError: 'Student' object has no attribute 'grade'
# print(s.grade)

s()
print(callable(s)) # True

class Fib(object):
    '__iter__ __next__'
    def __init__(self):
        # 初始化两个计数器a，b
        self.a, self.b = 0, 1 

    def __iter__(self):
        return self # 实例本身就是迭代对象，故返回自己

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b # 计算下一个值
        if self.a > 100000: # 退出循环的条件
            raise StopIteration()
        return self.a # 返回下一个值

    def __getitem__(self, n):
        if isinstance(n, int):
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice):
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L

for n in Fib():
    print(n)

f = Fib()
print(f[0])
print(f[5])
print(f[100])
print(f[0:5])
print(f[:10])
