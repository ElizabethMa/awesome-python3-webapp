# awesome-python3-webapp

## python3 实验课

[廖雪峰官网 python](http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000) 练习+笔记

## 一、基础 `/lessons/basic/*.py`

1. python 文件以 `.py` 为后缀
2. python 两种运行方法
    - 交互模式 -> 命令行里敲 `$ python3` 一行一行地输入源代码，每输入一行就执行一行
    - 直接运行 -> 命令行里敲 `$ python3 {filename}` 一行一行地输入源代码，每输入一行就执行一行
3. 如何直接运行 python 文件
    - 文件第一行加 `#!/usr/bin/env python3`
    - 命令行运行 `$ chmod a+x {filename}` 修改执行权限
    - 命令行运行文件 `$ ./{filename}`
4. 输入输出 `input_output.py`
5. 数据类型 `data_type.py`
6. 字符串和编码
7. list and tuple `list_tuple.py`
8. 条件和循环 `statements.py`
9. dict and set `dict_set.py`

#### 补充: ASCII、Unicode和UTF-8的关系
|字符|ASCII|Unicode|UTF-8|
|---|---|---|---|
|A|`01000001`|`00000000 01000001`|`01000001`|
|中|x|`01001110 00101101`|`11100100 10111000 10101101`|
||一个字节，无法表示中文等语言|每个字符都用两个字节表示，表示英文时太浪费空间|一个字节表示英文，三个字节表示中文|

在计算机内存中，统一使用Unicode编码，当需要保存到硬盘或者需要传输的时候，就转换为UTF-8编码。

用记事本编辑的时候，从文件读取的UTF-8字符被转换为Unicode字符到内存里，编辑完成后，保存的时候再把Unicode转换为UTF-8保存到文件。

## 二、函数 `lessons/functions/functions.py`

### 0. 如何获取帮助说明

方法1: 官网文档 [python3 文档](https://docs.python.org/3/index.html) [abs 函数在线说明](https://docs.python.org/3/library/functions.html#abs)

方法2: 命令行 `help(abs)` 查看 abs 函数的帮助说明

### 1. 数据类型转换函数

```py
int(123.64) # 123
float('123.64') # 123.64
str(1.23) # '1.23'
str(100) # '100'
bool('') # False
bool(1) # True
hex(100) # '0x64'
hex(255) # '0xff'
```

### 2. 定义函数 空函数 返回多个值(tuple) 

### 3. 函数参数

#### 3.0 参数类型检查

#### 3.1 位置参数(必选参数)

```py
def power(x):
    return x * x
```

#### 3.2 默认参数

```py
def power(x, n = 2):
    '''
    1 必选参数在前，默认参数在后
    2 默认参数必须指向不变对象  
    '''
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

power(5) # 25
power(5, 3) # 125
```

```py
def enroll(name, gender, age=6, city='Beijing'):
    '''
    默认参数顺序与函数提供的顺序不一样时，要把参数名写上。
    '''
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)

enroll('Sarah', 'F')
enroll('Bob', 'M', 7)
enroll('Adam', 'M', city='Tianjin')
```

```py
def add_end(L=[]):
    '''
    默认参数要指向不可变对象，函数定义的时候，就分配好了 L 指向的地址，
    每次函数调用的时候，都会修改 L 指向的地址存放的内容，而 L 本身没有改变
    '''
    L.append('END')
    return L

add_end([1,2,3]) # [1, 2, 3, 'END']
add_end() # ['END']
add_end() # ['END', 'END']
add_end() # ['END', 'END', 'END']

def add_end(L=None):
    '''
    str None 都是不可变对象
    '''
    if L is None:
        L = []
    L.append('END')
    return L

add_end() # ['END']
add_end() # ['END']
add_end() # ['END']
```

#### 3.3 可变参数

```py
def calc(*numbers):
    '''
    参数 numbers 接收到的是一个 tuple
    调用该函数时，可以传入任意个参数，包括 0 个参数
    '''
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

calc(1,2,3)
calc()
nums = [1, 2, 3]
calc(*nums) # *nums 表示把 nums 这个 list 的所有元素作为可变参数传进去
nums = (1, 2, 3)
calc(*nums)
```

#### 3.4 关键字参数

可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个 `tuple`(有序不可变列表)。

而关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个 `dict`(无序 k-v 对)。

```py
def person(name, age, **kw):
    print('name:', name, ', age:', age, ', other:', kw)

person('Michael', 30) 
# name: Michael , age: 30 , other: {}
person('Bob', 35, city='Beijing') 
# name: Bob , age: 35 , other: {'city': 'Beijing'}
person('Adam', 45, gender='M', job='Engineer')
# name: Adam , age: 45 , other: {'gender': 'M', 'job': 'Engineer'}
extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, **extra)
# name: Jack , age: 24 , other: {'city': 'Beijing', 'job': 'Engineer'}
# `**extra` 表示把 extra 这个 dict 的所有 key-value 用关键字参数传入到函数的 `**kw` 参数，`**kw` 将获得 `**extra` 的一份 copy
```

#### 3.5 命名关键字参数

如果要限制关键字参数的名字，就可以用命名关键字参数，例如，只接收city和job作为关键字参数。这种方式定义的函数如下：

```py
def person(name, age, *, city, job):
    '''
    命名关键字参数需要一个特殊分隔符 * ，* 后面的参数被视为命名关键字参数。
    '''
    print(name, age, city, job)

person('Jack', 24, city='Beijing', job='Engineer')

def person(name, age, *args, city, job):
    '''
    如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符 * 了
    '''
    print(name, age, args, city, job)

# 命名关键字参数必须传入参数名，这和位置参数不同。如果没有传入参数名，调用将报错
person('Jack', 24, 'Beijing', 'Engineer') # error

def person(name, age, *, city='Beijing', job):
    '''
    命名关键字参数可以有缺省值, 调用时不用出入此参数
    '''
    print(name, age, city, job)

person('Jack', 24, job='Engineer')
```

#### 3.6 参数组合

参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。

```py
# 在函数调用的时候，Python解释器自动按照参数位置和参数名把对应的参数传进去。
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)

# 通过一个 tuple 和 dict，你也可以调用上述函数

args = (1, 2, 3, 4)
kw = {'d': 99, 'x': '#'}
f1(*args, **kw)
# a = 1 b = 2 c = 3 args = (4,) kw = {'d': 99, 'x': '#'}

args = (1, 2, 3)
kw = {'d': 88, 'x': '#'}
f2(*args, **kw)
# a = 1 b = 2 c = 3 d = 88 kw = {'x': '#'}
```

对于任意函数，都可以通过类似 `func(*args, **kw)` 的形式调用它，无论它的参数是如何定义的。

`*args` 是可变参数，`args` 接收的是一个 `tuple`；`**kw`是关键字参数，`kw` 接收的是一个 `dict`。

### 4. 递归函数
```py
def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)
```
```py
def fact(n):
    return fact_iter(n, 1)

def fact_iter(num, product):
    '''
    尾递归优化，尾递归是指，在函数返回的时候，调用自身本身，并且，return语句不能包含表达式。
    '''
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)
```

## 三、高级特性 `/lessons/features/features.py`

### 1. 切片(Slice)

### 2. 迭代(Iteration) `for ... in`

### 3. 列表生成式(List Comprehensions)

### 4. 生成器(generator)

通过列表生成式，我们可以直接创建一个列表。但是，受到内存限制，列表容量肯定是有限的。而且，创建一个包含100万个元素的列表，不仅占用很大的存储空间，如果我们仅仅需要访问前面几个元素，那后面绝大多数元素占用的空间都白白浪费了。

所以，如果列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元素呢？这样就不必创建完整的list，从而节省大量的空间。在Python中，这种一边循环一边计算的机制，称为生成器：generator。

要创建一个 generator，有很多种方法。第一种方法很简单，只要把一个列表生成式的[]改成()，就创建了一个 generator

### 5. 迭代器

`for ... in` 循环可用的数据类型 可迭代对象 `Iterable`:

    可以使用 `isinstance()` 判断一个对象是否是可迭代 `Iterable` 对象  
    可以被 `next()` 函数调用并不断返回下一个值的对象称为迭代器：Iterator，可以使用 `isinstance()` 判断一个对象是否是 Iterator 对象。
    Python 的 `Iterator` 对象表示的是一个数据流，`Iterator` 对象可以被 `next()` 函数调用并不断返回下一个数据，直到没有数据时抛出 `StopIteration` 错误。可以把这个数据流看做是一个有序序列，但我们却不能提前知道序列的长度，只能不断通过 `next()` 函数实现按需计算下一个数据，所以`Iterator` 的计算是惰性的，只有在需要返回下一个数据时它才会计算。
    `Iterator` 甚至可以表示一个无限大的数据流，例如全体自然数。而使用 `list` 是永远不可能存储全体自然数的。

+ 集合数据类型: `list` `tuple` `dict` `set` `str` ...
+ `generator`: 生成器 或者 带 `yield` 的 generator function

    生成器都是 `Iterator` 对象
    `list`、`dict`、`str` 虽然是 `Iterable`，却不是 `Iterator`, 把 `list`、`dict`、`str` 等 `Iterable` 变成 `Iterator` 可以使用 `iter()` 函数

```s
>>> isinstance([], Iterable)
True
>>> isinstance({}, Iterable)
True
>>> isinstance('abc', Iterable)
True
>>> isinstance((x for x in range(10)), Iterable)
True
>>> isinstance(100, Iterable)
False
```

```s
>>> isinstance((x for x in range(10)), Iterator)
True
>>> isinstance([], Iterator)
False
>>> isinstance({}, Iterator)
False
>>> isinstance('abc', Iterator)
False
```

```s
>>> isinstance(iter([]), Iterator)
True
>>> isinstance(iter({}), Iterator)
True
>>> isinstance(iter('abc'), Iterator)
True
```

## 四、高级函数 `lessons/functions/functions_a.py`

### 1. 高阶函数

    把函数作为参数传入，这样的函数称为高阶函数，函数式编程就是指这种高度抽象的编程范式。

#### 1.1 map/reduce

#### 1.2 filter

#### 1.3 sorted
