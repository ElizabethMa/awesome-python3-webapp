#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'my dict 测试'

import unittest

from mydict import Dict

class TestDict(unittest.TestCase):
    # 'unit test'
    '以test开头的方法就是测试方法，不以test开头的方法不被认为是测试方法，测试的时候不会被执行。\
    对每一类测试都需要编写一个test_xxx()方法。\
    由于 unittest.TestCase 提供了很多内置的条件判断，我们只需要调用这些方法就可以断言输出是否是我们所期望的。'

    def setUp(self):
        print('setUp...')

    def tearDown(self):
        print('tearDown...')

    def test_init(self):
        d = Dict(a=1, b='test')
        self.assertEqual(d.a, 1)
        self.assertEqual(d.b, 'test')
        self.assertTrue(isinstance(d, dict))

    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertEqual(d.key, 'value')

    def test_attr(self):
        d = Dict()
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEqual(d['key'], 'value')

    def test_keyerror(self):
        d = Dict()
        with self.assertRaises(KeyError):
            value = d['empty']

    def test_attrerror(self):
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.empty

if __name__ == '__main__':
    unittest.main()
