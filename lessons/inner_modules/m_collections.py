#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'namedtuple deque'

from collections import namedtuple, deque, defaultdict, OrderedDict, Counter

print('\n===== namedtuple =====\n')

Point = namedtuple('Ponint', ['x', 'y'])
p = Point(1, 2)

print('namedtuple : %s, %s' % (p.x, p.y))
print('isinstance(p, Point) : %s' % isinstance(p, Point))
print('isinstance(p, tuple) : %s' % isinstance(p, tuple))

# 圆 (坐标 半径)
Circle = namedtuple('Circle', ['x', 'y', 'r'])

print('\n===== deque =====\n')

q = deque(['a', 'b', 'c'])
print(q)
q.append('x')
q.appendleft('y')
print(q)
q.pop()
q.popleft()
print(q)

print('\n===== defaultdict =====\n')
# 除了在Key不存在时返回默认值，defaultdict的其他行为跟dict是完全一样的。
# 注意默认值是调用函数返回的，而函数在创建 `defaultdict` 对象时传入。
dd = defaultdict(lambda: 'N/A')
dd['key1'] = 'abc'
print(dd['key1'] , dd['key2'])
print('isinstance(dd, defaultdict) : %s' % isinstance(dd, defaultdict))
print('isinstance(dd, dict) : %s' % isinstance(dd, dict))

print('\n===== OrderedDict =====\n')
# 使用 `dict` 时，`Key` 是无序的。在对dict做迭代时，我们无法确定Key的顺序。
# 如果要保持 `Key` 的顺序，可以用 `OrderedDict`
d = dict([('a', 1), ('b', 2), ('c', 3)])
print(d)
od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(od) # OrderedDict的Key是有序的
# 注意，OrderedDict的Key会按照插入的顺序排列，不是Key本身排序
od2 = OrderedDict()
od2['z'] = 1
od2['y'] = 2
od2['x'] = 3
print(list(od.keys()))

# OrderedDict 可以实现一个 FIFO（先进先出）的 dict，当容量超出限制时，先删除最早添加的Key:

class LastUpdatedOrderedDict(OrderedDict):

    def __init__(self, capacity):
        super(LastUpdatedOrderedDict, self).__init__()
        self._capacity = capacity

    def __setitem__(self, key, value):
        containsKey = 1 if key in self else 0
        if len(self) - containsKey >= self._capacity:
            last = self.popitem(last=False)
            print('remove:', last)
        if containsKey:
            del self[key]
            print('set:', (key, value))
        else:
            print('add:', (key, value))
        OrderedDict.__setitem__(self, key, value)

print('\n===== Counter =====\n')
# Counter实际上也是dict的一个子类
c = Counter()
for ch in 'programming':
    c[ch] = c[ch] + 1
print(c)
