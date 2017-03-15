#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' @property 既能检查参数，又可以用类似属性的方式来访问类的变量'

__author__ = 'Ma Yanqiong'

class Student(object):
    'class Student'

    @property
    def score(self):
        'getter'
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

s = Student()
s.score = 60
print(s.score)

# s.score = 9999
# ValueError: score must between 0 ~ 100!

# 只定义getter方法，不定义setter方法就是一个只读属性：
class Student2(object):

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        return 2015 - self._birth

# 练习
class Screen(object):

    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError('score must be a number!')
        self._width = value

    @property
    def height(self):
        return self._height
    
    @height.setter
    def height(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError('score must be a number!')
        self._height = value
   
    @property
    def resolution(self):
        return self._width * self._height

s = Screen()
s.width = 1024
s.height = 768
print(s.resolution)
assert s.resolution == 786432, '1024 * 768 = %d ?' % s.resolution

# 多重继承
# 通常主线都是单一继承下来的，再用 Maxin 混入额外功能
class Mammal(object):
    pass
class RunnableMixIn(object):
    pass
class CarnivorousMixIn(object):
    pass
class Dog(Mammal, RunnableMixIn, CarnivorousMixIn):
    pass
