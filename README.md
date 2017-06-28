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

### 2. 装饰器函数 lessons/functions/func_decorator.py

### 3. 偏函数，固定部分参数 lessons/functions/func_partial.py

## 五、模块 

提高代码的可维护性、重用性、避免函数名和变量名冲突

在 Python 中，一个 `.py` 文件就称之为一个模块（`Module`）

为了避免模块名冲突，Python 又引入了按目录来组织模块的方法，称为包（`Package`）。

### 1. 使用模块

[Python 内置函数](https://docs.python.org/3/library/functions.html)

```py
# 包 package, 有 __init__.py 文件，python 就会认为这是一个包，而不是一个普通的目录
mycompany -> __init__.py  # 模块 module  mycompany
          -> abc.py  # 模块 module  mycompany.abc
          -> xyz.py  # 模块 module  mycompany.xyz

mycompany -> __init__.py
          -> abc.py
          -> xyz.py
          -> utils.py 
          -> web -> __init__.py
                 -> utils.py
                 -> www.py # 模块 module mycompany.web.www
```


```py
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'Michael Liao'

import sys


def test():
    args = sys.argv
    if len(args)==1:
        print('Hello, world!')
    elif len(args)==2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')

if __name__=='__main__':
    test()
```

```
> 第1行和第2行是标准注释，
> 第1行注释可以让这个 hello.py 文件直接在 Unix/Linux/Mac 上运行，
> 第2行注释表示 .py 文件本身使用标准 UTF-8 编码；
> 第4行是一个字符串，表示模块的文档注释，任何模块代码的第一个字符串都被视为模块的文档注释；
> 第6行使用 `__author__` 变量把作者写进去，这样当你公开源代码后别人就可以瞻仰你的大名；
> `import sys` 导入该模块
> sys 模块有一个 `argv` 变量，用 list 存储了命令行的所有参数。argv 至少有一个元素，因为第一个参数永远是该 `.py` 文件的名称
> 当我们在命令行运行 `hello` 模块文件时，Python 解释器把一个特殊变量 `__name__` 置为 `__main__`，
> 而如果在其他地方导入该 `hello` 模块时，if 判断将失败，因此，这种 if 测试可以让一个模块通过命令行运行时执行一些额外的代码，最常见的就是运行测试。
```

### 2. 模块作用域

在Python中，是通过 `_` 前缀来实现局部变量

正常的函数和变量名是公开的（public），可以被直接引用，比如：abc，x123，PI等；

类似 `__xxx__` 这样的变量是特殊变量，可以被直接引用，但是有特殊用途，比如上面的 `__author__`，`__name__`就是特殊变量，hello 模块定义的文档注释也可以用特殊变量 `__doc__` 访问，我们自己的变量一般不要用这种变量名；

类似 `_xxx` 和 `__xxx` 这样的函数或变量就是非公开的（private），不应该被直接引用，比如 `_abc` ，`__abc` 等；

private 函数和变量“不应该”被直接引用，而不是“不能”被直接引用，是因为Python并没有一种方法可以完全限制访问 private 函数或变量，但是，从编程习惯上不应该引用 private 函数或变量。

### 3. 安装第三方模块

```s
pip3 -V
pip3 install Pillow
```

## 六、面向对象编程
### 1. 类和实例
### 2. 访问限制
```py
# 在类中定义的函数第一个参数永远是实例变量 self
# 在 Python 中，实例的变量名如果以 __ 开头，就变成了一个私有变量（private），只有内部可以访问，外部不能访问。
# 在 Python 中，变量名类似 __xxx__ 的，也就是以双下划线开头，并且以双下划线结尾的，是特殊变量，特殊变量是可以直接访问的，不是 private 变量。
# 在 Python 中，按照约定俗成的习惯，以 _ 开头的变量， 虽然可以被访问，但是，请当作私有变量，不要随意访问
# 对于双下划线开头的实例变量，Python 解释器对外把 __name 变量改成了 _Student__name，所以，仍然可以通过 _Student__name 来访问 __name 变量
class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.score = score

bart = Student('Ada', 90)
bart.score # 90
bart.__name # error
```
### 3. 继承和多态 `/lessons/oop/oop1.py`
### 4. 获取对象信息

+ type()
+ isinstance()
+ dir()
+ getattr()、setattr()、hasattr()

类似 `__xxx__` 的属性和方法在Python中都是有特殊用途的，比如 `__len__` 方法返回长度。在 Python 中，如果你调用 `len()` 函数试图获取一个对象的长度，实际上，在 `len()` 函数内部，它自动去调用该对象的 `__len__()` 方法，所以，下面的代码是等价的：

```py
len('ABC')
'ABC'.__len__()
```

如果自己写的类想用 `len(myObj)` 的话，就在内部实现 `__len__()` 方法

```py
class MyObj(Object):
    def __len__(self):
        return 1000

obj = MyObj()
len(obj)
```

### 5. 类属性与实例属性

当我们定义了一个类属性后，这个属性虽然归类所有，但类的所有实例都可以访问到。

在编写程序的时候，千万不要把实例属性和类属性使用相同的名字，因为相同名称的实例属性将屏蔽掉类属性，但是当你删除实例属性后，再使用相同的名称，访问到的将是类属

## 七、面向对象高级编程

### 1. 使用 `__slots__` `/lessons/oop/oop2.py`
### 2. 使用 `@property` `/lessons/oop/oop3.py`
### 3. 多重继承 MixIn

```py
# 举例
class MyTCPServer(TCPServer, ForkingMixIn):
    '编写一个多进程模式的TCP服务'
    pass

class MyUDPServer(UDPServer, ThreadingMixIn):
    '编写一个多线程模式的UDP服务'
    pass

class MyTCPServer(TCPServer, CoroutineMixIn):
    '一个更先进的协程模型，可以编写一个CoroutineMixIn'
    pass
```

### 4. 定制类 `/lessons/oop/oop4.py`

[官方文档 Special method names](https://docs.python.org/3/reference/datamodel.html#special-method-names)

+ `__str__` （用 print 打印)
+ `__repr__` (直接命令行输出)
+ `__iter__` `__next__` 用 for in 循环
+ `__getitem__` 用 [] 下标取出数据， 处理 下标、切片对象、step 参数
+ `__setitem__`
+ `__delitem__`
+ `__getattr__` 返回属性或者函数
+ `__call__` 直接调用实例本身 `callable` 对象,通过callable()函数，我们就可以判断一个对象是否是“可调用”对象。

### 5. 枚举类 `/lessons/oop/oop5.py`
### 6. 元类 `/lessons/oop/oop6.py`

+ `type()`
+ `metaclass` 动态创建类 示例: `/lessons/oop/oop_orm.py`

## 八、错误、调试、测试

### 1. `try`

    try ... except ... else ... finally

[Python所有的错误都是从BaseException类派生的，常见的错误类型和继承关系](https://docs.python.org/3/library/exceptions.html#exception-hierarchy)

```py
try:
    print('try...')
    r = 10 / int('2')
    print('result:', r)
except ValueError as e:
    print('ValueError:', e)
except ZeroDivisionError as e:
    print('ZeroDivisionError:', e)
else:
    print('no error!')
finally:
    print('finally...')
print('END')
```

```py
# 所有 Error 都继承自 BaseException，except 会捕获其类型和子类
try:
    foo()
except ValueError as e:
    print('ValueError')
except UnicodeError as e:
    print('UnicodeError')
# 第二个 except 永远也捕获不到 UnicodeError，因为 UnicodeError 是 ValueError 的子类
```

### 2. 调用堆栈

根据错误信息定位错误位置。

### 3. 记录错误 `logging`模块

如果不捕获错误，自然可以让Python解释器来打印出错误堆栈，但程序也被结束了。既然我们能捕获错误，就可以把错误堆栈打印出来，然后分析错误原因，同时，让程序继续执行下去。

`/lessons/errors/err_logging.py`

同样是出错，但程序打印完错误信息后会继续执行，并正常退出。

[错误配置文档](https://docs.python.org/3/howto/logging-cookbook.html)

### 4. 抛出错误 `raise`

只有在必要的时候才定义我们自己的错误类型。如果可以选择 Python 已有的内置的错误类型（比如 ValueError，TypeError），尽量使用 Python 内置的错误类型。

```py
class FooError(ValueError):
    pass

def foo(s):
    n = int(s)
    if n==0:
        raise FooError('invalid value: %s' % s)
    return 10 / n

foo('0')
```
```py
def foo(s):
    n = int(s)
    if n==0:
        raise ValueError('invalid value: %s' % s)
    return 10 / n

def bar():
    try:
        foo('0')
    except ValueError as e:
        print('ValueError!')
        raise

# 此处捕获错误目的只是记录一下，便于后续追踪。但是，由于当前函数不知道应该怎么处理该错误，所以，最恰当的方式是继续往上抛，让顶层调用者去处理。

bar()
```
`raise` 语句如果不带参数，就会把当前错误原样抛出。

```py
try:
    10 / 0
except ZeroDivisionError:
    raise ValueError('input error!')
```
在 except 中 `raise`一个 Error，还可以把一种类型的错误转化成另一种类型：

### 5. 调试

#### 5.1 print()

#### 5.2 assert()
如果断言失败，`assert` 语句本身就会抛出 `AssertionError`。
启动 Python 解释器时可以用 -O 参数来关闭 assert。
```py
def foo(s):
    n = int(s)
    assert n != 0, 'n is zero!'
    return 10 / n

def main():
    foo('0')
```

#### 5.3 logging
可以不同的日志级别，输出到文件等。

#### 5.4 pdb `/lessons/errors/err.py`
启动Python的调试器pdb，让程序以单步方式运行，可以随时查看运行状态。

    python3 -m pdb err.py

输入命令 `l` 来查看代码

输入命令 `n` 可以单步执行代码

任何时候都可以输入命令 `p 变量名` 来查看变量

输入命令 `q` 结束调试

#### 5.5 pdb.set_trace() `/lessons/errors/err.py`

这个方法也是用 pdb，但是不需要单步执行。
我们只需要 import pdb，然后，在可能出错的地方放一个 pdb.set_trace()，就可以设置一个断点。

用命令 `p 变量名` 查看变量

用命令 `c` 继续运行

#### 5.6 IDE

[目前比较好的支持调试功能的 IDE - pycharm](http://www.jetbrains.com/pycharm/)

### 6. 单元测试 `/lessons/tests/unittest_demo.py`

#### 6.1 `unittest`

```
python3 lessons/tests/unittest_demo.py

或者

python3 -m unittest unittest_demo
```

#### 6.2 `setUp` 与 `tearDown`

在单元测试中有两个特殊的 `setUp()` 和 `tearDown()` 方法。这两个方法会分别在每调用一个测试方法的前后分别被执行。

设想你的测试需要启动一个数据库，这时，就可以在setUp()方法中连接数据库，在tearDown()方法中关闭数据库，这样，不必在每个测试方法中重复相同的代码。

### 7. 文档测试 `/lessons/tests/doctest_demo.py`

Python内置的“文档测试”（doctest）模块可以直接提取注释中的代码并执行测试。

`doctest` 严格按照 Python 交互式命令行的输入和输出来判断测试结果是否正确。

```py
def abs(n):
    '''
    Function to get absolute value of number.

    Example:

    >>> abs(1)
    1
    >>> abs(-1)
    1
    >>> abs(0)
    0
    '''
    return n if n >= 0 else (-n)
```


## 八、IO 编程 

`同步 IO` vs `异步 IO`

### 1. 文件读写

#### 1.1 文件读

标示符 `'r'` 表示读

```py
# python 内置函数
# 如果文件不存在，open() 函数就会抛出一个 IOError 的错误，并且给出错误码和详细的信息
# 如果文件打开成功，接下来，调用 read() 方法可以一次读取文件的全部内容，Python 把内容读到内存，用一个str对象表示
# 最后一步是调用close()方法关闭文件。
# 文件使用完毕后必须关闭，因为文件对象会占用操作系统的资源，并且操作系统同一时间能打开的文件数量也是有限的
f = open('/Users/michael/test.txt', 'r')
str = f.read()
f.close()
```
```py
# 为了保证无论是否出错都能正确地关闭文件，我们可以使用 try ... finally 来实现：
try:
    f = open('/path/to/file', 'r')
    print(f.read())
finally:
    if f:
        f.close()

# 但是每次都这么写实在太繁琐，所以，Python 引入了 with 语句来自动帮我们调用 close() 方法
# 和前面的 try ... finally 是一样的，但是代码更佳简洁，并且不必调用f.close()方法
with open('/path/to/file', 'r') as f:
    print(f.read())
```

对于大的文件，可以反复调用 `read(size)` 方法，每次最多读取 `size` 个字节的内容。

调用 `readline()` 可以每次读取一行内容，调用 `readlines()` 一次读取所有内容并按行返回 `list`。

因此，要根据需要决定怎么调用。

如果文件很小，read()一次性读取最方便；如果不能确定文件大小，反复调用read(size)比较保险；如果是配置文件，调用readlines()最方便：

```py
for line in f.readlines():
    print(line.strip()) # 把末尾的'\n'删掉
```

#### 1.2 file-like Object

只要是有 read() 方法的对象就可以

`StringIO` 就是在内存中创建的 `file-like Object`，常用作临时缓冲。

#### 1.3 二进制文件

前面讲的默认都是读取文本文件，并且是UTF-8编码的文本文件。要读取二进制文件，比如图片、视频等等，用'rb'模式打开文件即可：

```bash
>>> f = open('/Users/michael/test.jpg', 'rb')
>>> f.read()
b'\xff\xd8\xff\xe1\x00\x18Exif\x00\x00...' # 十六进制表示的字节
```

#### 1.4 字符编码

要读取非UTF-8编码的文本文件，需要给 `open()` 函数传入 `encoding` 参数，例如，读取 `GBK` 编码的文件：

```bash
>>> f = open('/Users/michael/gbk.txt', 'r', encoding='gbk')
>>> f.read()
# '测试'
# 遇到有些编码不规范的文件，你可能会遇到UnicodeDecodeError，因为在文本文件中可能夹杂了一些非法编码的字符。
# 遇到这种情况，open()函数还接收一个 errors 参数，表示如果遇到编码错误后如何处理。最简单的方式是直接忽略：
>>> f = open('/Users/michael/gbk.txt', 'r', encoding='gbk', errors='ignore')
```

#### 1.5 写文件

写文件和读文件是一样的，唯一区别是调用 `open()` 函数时，传入标识符 `w` 或者 `wb` 表示写文本文件或写二进制文件：

```py
>>> f = open('/Users/michael/test.txt', 'w')
>>> f.write('Hello, world!')
>>> f.close()
```

你可以反复调用write()来写入文件，但是务必要调用 `f.close()` 来关闭文件。

当我们写文件时，操作系统往往不会立刻把数据写入磁盘，而是放到内存缓存起来，空闲的时候再慢慢写入。只有调用close()方法时，操作系统才保证把没有写入的数据全部写入磁盘。

忘记调用close()的后果是数据可能只写了一部分到磁盘，剩下的丢失了。所以，还是用with语句来得保险：

```py
with open('/Users/michael/test.txt', 'w') as f:
    f.write('Hello, world!')
```

要写入特定编码的文本文件，请给open()函数传入encoding参数，将字符串自动转换成指定编码。

### 2. StringIO 和 BytesIO

`StringIO` 和 `BytesIO` 是在内存中操作 `str` 和 `bytes` 的方法，使得和读写文件具有一致的接口。

#### 2.1 StringIO

很多时候，数据读写不一定是文件，也可以在内存中读写。

StringIO 顾名思义就是在内存中读写 str。

要把 str 写入 StringIO，我们需要先创建一个 StringIO，然后，像文件一样写入即可：

```bash
>>> from io import StringIO
>>> f = StringIO()
>>> f.write('hello')
5
>>> f.write(' ')
1
>>> f.write('world!')
6
>>> print(f.getvalue())
hello world!
```

`getvalue()` 方法用于获得写入后的 str。

要读取 `StringIO`，可以用一个 str 初始化 StringIO，然后，像读文件一样读取：

```bash
>>> from io import StringIO
>>> f = StringIO('Hello!\nHi!\nGoodbye!')
>>> while True:
...     s = f.readline()
...     if s == '':
...         break
...     print(s.strip())
...
Hello!
Hi!
Goodbye!
```

#### 2.2 BytesIO

StringIO 操作的只能是 str，如果要操作二进制数据，就需要使用 BytesIO。

BytesIO 实现了在内存中读写 bytes，我们创建一个 BytesIO，然后写入一些 bytes：

```bash
>>> from io import BytesIO
>>> f = BytesIO()
>>> f.write('中文'.encode('utf-8'))
6
>>> print(f.getvalue())
b'\xe4\xb8\xad\xe6\x96\x87'
```

请注意，写入的不是str，而是经过 UTF-8 编码的bytes。

和 StringIO 类似，可以用一个 bytes 初始化 BytesIO，然后，像读文件一样读取：

```bash
>>> from io import BytesIO
>>> f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
>>> f.read()
b'\xe4\xb8\xad\xe6\x96\x87'
```

### 3. 操作文件和目录 `/lessons/tests/with_file.py`

Python 内置的 `os` 模块可以直接调用操作系统提供的接口函数。

```bash
>>> import os
>>> os.name # 操作系统类型
'posix'
# 如果是 `posix`，说明系统是 Linux、Unix 或 Mac OS X，如果是 `nt`，就是 Windows 系统。

# os 模块的某些函数是跟操作系统相关的。
>>> os.uname()
posix.uname_result(sysname='Darwin', nodename='yanqiongs-MacBook-Pro.local', release='15.6.0', version='Darwin Kernel Version 15.6.0: Mon Jan  9 23:07:29 PST 2017; root:xnu-3248.60.11.2.1~1/RELEASE_X86_64', machine='x86
_64')

# 环境变量
>>> os.environ

# 要获取某个环境变量的值，可以调用os.environ.get('key')：
>>> os.environ.get('PATH')
'/Library/Frameworks/Python.framework/Versions/3.4/bin:/Users/yanqiong/Library/Android/sdk/platform-tools:/Library/Frameworks/Python.framework/Versions/3.4/bin:/Users/yanqiong/Library/Android/sdk/platform-tools:/usr/loc
al/bin:/usr/bin:/bin:/usr/sbin:/sbin:/Users/yanqiong/mongodb/bin:/usr/local/deployd/bin:/usr/local/go/bin:/Users/yanqiong/Library/apache-ant-1.9.7/bin:/Users/yanqiong/Library/apache-ant-1.9.7/bin'
>>> os.environ.get('x', 'default')
'default'
```

操作文件和目录的函数一部分放在 `os` 模块中，一部分放在 `os.path` 模块中，这一点要注意一下。查看、创建和删除目录可以这么调用：

```bash
# 查看当前目录的绝对路径:
>>> os.path.abspath('.')
'/Users/michael'
# 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:
>>> os.path.join('/Users/michael', 'testdir')
'/Users/michael/testdir'
# 然后创建一个目录:
>>> os.mkdir('/Users/michael/testdir')
# 删掉一个目录:
>>> os.rmdir('/Users/michael/testdir')
```

把两个路径合成一个时，不要直接拼字符串，而要通过 `os.path.join()` 函数，这样可以正确处理不同操作系统的路径分隔符。

在 Linux/Unix/Mac 下，`os.path.join()` 返回这样的字符串： `part-1/part-2`

而 Windows 下会返回这样的字符串：`part-1\part-2`

同样的道理，要拆分路径时，也不要直接去拆字符串，而要通过 `os.path.split()` 函数，这样可以把一个路径拆分为两部分，后一部分总是最后级别的目录或文件名：

```bash
>>> os.path.split('/Users/michael/testdir/file.txt')
('/Users/michael/testdir', 'file.txt')
```

os.path.splitext()可以直接让你得到文件扩展名，很多时候非常方便：

```bash
>>> os.path.splitext('/path/to/file.txt')
('/path/to/file', '.txt')
```

这些合并、拆分路径的函数并不要求目录和文件要真实存在，它们只对字符串进行操作。

文件操作使用下面的函数。假定当前目录下有一个test.txt文件：

```bash
# 对文件重命名:
>>> os.rename('test.txt', 'test.py')
# 删掉文件:
>>> os.remove('test.py')
```
但是复制文件的函数居然在 `os` 模块中不存在！原因是复制文件并非由操作系统提供的系统调用。理论上讲，我们通过上一节的读写文件可以完成文件复制，只不过要多写很多代码。

幸运的是 `shutil` 模块提供了 `copyfile()` 的函数，你还可以在 `shutil` 模块中找到很多实用函数，它们可以看做是 `os` 模块的补充。

最后看看如何利用 Python 的特性来过滤文件。比如我们要列出当前目录下的所有目录，只需要一行代码：

```bash
>>> [x for x in os.listdir('.') if os.path.isdir(x)]
['.git', 'config', 'lessons', 'logs']
```

要列出所有的.py文件，也只需一行代码：

```bash
>>> [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']
['learning.py']
```

### 4. 序列化 `/lessons/tests/pickling_unpickling.py`

把变量从内存中变成可存储或传输的过程称之为序列化，在 Python 中叫 `pickling`。

序列化之后，就可以把序列化后的内容写入磁盘，或者通过网络传输到别的机器上。

反过来，把变量内容从序列化的对象重新读到内存里称之为反序列化，即 `unpickling`。

Python 提供了 `pickle` 模块来实现序列化。

#### 4.1 pickle

`pickle.dumps` / `pickle.dump`
`pickle.loads` / `pickle.load`

#### 4.2 JSON 

[Python3 JSON 文档](https://docs.python.org/3/library/json.html#json.dumps)

JSON 表示的对象就是标准的 JavaScript 语言的对象，JSON 和 Python 内置的数据类型对应如下：

| JSON类型 | Python类型 |
| --- | --- |
| {} | dict |
| [] | list |
| "string" | str |
| 1234.56 | int或float |
| true/false | True/False |
| null | None |

由于 JSON 标准规定 JSON 编码是 UTF-8，所以我们总是能正确地在 Python 的 str 与 JSON 的字符串之间转换。

通常 class 的实例都有一个 `__dict__` 属性，它就是一个 dict，用来存储实例变量。也有少数例外，比如定义了 `__slots__` 的class。

## 九、进程和线程 `lessons/process`

### 1. 多进程

#### 1.1 `fork()`
 Unix/Linux 操作系统提供了 `fork()` 系统调用， 调用一次，返回两次。分别在父子进程内返回。
 
 子进程永远返回 `0`, 父进程返回子进程的 ID。

 子进程字需要调用 `getppid()` 就可以拿到父进程的 ID。

 python 的 `os` 模块封装了常见的系统调用。Windows 无法使用。

 ```py
import os

print('Process (%s) start...' % os.getpid())
# Only works on Unix/Linux/Mac:
pid = os.fork()
if pid == 0:
    print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
else:
    print('I (%s) just created a child process (%s).' % (os.getpid(), pid))
```

#### 1.2 `multiprocessing` `Process`

`multiprocessing` 模块是跨平台版本的多进程模块。

`multiprocessing` 模块提供了一个 `Process` 类来代表一个进程对象.

`join()` 方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步。

#### 1.3 `Pool`

如果要启动大量的子进程，可以用进程池的方式批量创建子进程

#### 1.4 子进程 `subprocess`

`subprocess` 模块可以让我们非常方便地启动一个子进程，然后控制其输入和输出。

#### 1.5 进程间通信

Python 的 `multiprocessing` 模块包装了底层的机制，提供了 `Queue` 、`Pipes` 等多种方式来交换数据。

### 2. 多线程

进程是由若干线程组成的，一个进程至少有一个线程。

于线程是操作系统直接支持的执行单元，因此，高级语言通常都内置多线程的支持，Python也不例外，并且，Python的线程是真正的Posix Thread，而不是模拟出来的线程。

#### 2.1 `threading` 
进程是由若干线程组成的，一个进程至少有一个线程

Python的标准库提供了两个模块：`_thread` 和 `threading` ，`_thread` 是低级模块，`threading` 是高级模块，对 `_thread` 进行了封装。绝大多数情况下，我们只需要使用 `threading` 这个高级模块。

启动一个线程就是把一个函数传入并创建Thread实例，然后调用start()开始执行：

```py
import time, threading

# 新线程执行的代码:
def loop():
    print('thread %s is running...' % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        print('thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(1)
    print('thread %s ended.' % threading.current_thread().name)

# 任何进程默认会启动一个线程，我们把该线程称为主线程，主线程又可以启动新的线程，Python的 threading 模块有个 current_thread() 函数，它永远返回当前线程的实例。
# 主线程实例的名字叫 MainThread，子线程的名字在创建时指定，我们用 LoopThread 命名子线程。
# 如果不起名字Python就自动给线程命名为Thread-1，Thread-2……

print('thread %s is running...' % threading.current_thread().name)
t = threading.Thread(target=loop, name='LoopThread')
t.start()
t.join()
print('thread %s ended.' % threading.current_thread().name)
```

#### 2.2 `Lock`
多线程编程，模型复杂，容易发生冲突，必须用锁加以隔离，同时，又要小心死锁的发生。

多线程和多进程最大的不同在于，多进程中，同一个变量，各自有一份拷贝存在于每个进程中，互不影响，而多线程中，所有变量都由所有线程共享，

```py
'多线程同时操作同一个变量把内容改乱'

import time, threading

# 假定这是你的银行存款:
balance = 0

def change_it(n):
    # 先存后取，结果应该为0:
    global balance
    balance = balance + n
    balance = balance - n

def run_thread(n):
    for i in range(100000):
        change_it(n)

t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)
```

```py
'多线程同时操作同一个变量 - 加锁'

import time, threading

# 假定这是你的银行存款:
balance = 0
lock = threading.Lock()

def change_it(n):
    # 先存后取，结果应该为0:
    global balance
    balance = balance + n
    balance = balance - n

def run_thread(n):
    for i in range(100000):
        # 先获取锁
        lock.acquire()
        try:
            change_it(n)
        finally:
            lock.release()

# 获得锁的线程用完后一定要释放锁，否则那些苦苦等待锁的线程将永远等待下去，成为死线程。所以我们用try...finally来确保锁一定会被释放。

t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)
```

#### 2.3 多核CPU

因为Python的线程虽然是真正的线程，但解释器执行代码时，有一个GIL锁：Global Interpreter Lock，任何Python线程执行前，必须先获得GIL锁，然后，每执行100条字节码，解释器就自动释放GIL锁，让别的线程有机会执行。这个GIL全局锁实际上把所有线程的执行代码都给上了锁，所以，多线程在Python中只能交替执行，即使100个线程跑在100核CPU上，也只能用到1个核。

GIL是Python解释器设计的历史遗留问题，通常我们用的解释器是官方实现的CPython，要真正利用多核，除非重写一个不带GIL的解释器。

所以，在Python中，可以使用多线程，但不要指望能有效利用多核。如果一定要通过多线程利用多核，那只能通过C扩展来实现，不过这样就失去了Python简单易用的特点。

不过，也不用过于担心，Python虽然不能利用多线程实现多核任务，但可以通过多进程实现多核任务。多个Python进程有各自独立的GIL锁，互不影响。

### 3. ThreadLocal

一个 `ThreadLocal` 变量虽然是全局变量，但每个线程都只能读写自己线程的独立副本，互不干扰。ThreadLocal解决了参数在一个线程中各个函数之间互相传递的问题。

```py
import threading

# 创建全局ThreadLocal对象:
local_school = threading.local()

def process_student():
    # 获取当前线程关联的student:
    std = local_school.student
    print('Hello, %s (in %s)' % (std, threading.current_thread().name))

def process_thread(name):
    # 绑定ThreadLocal的student:
    local_school.student = name
    process_student()

t1 = threading.Thread(target= process_thread, args=('Alice',), name='Thread-A')
t2 = threading.Thread(target= process_thread, args=('Bob',), name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()
```

执行结果：
```
Hello, Alice (in Thread-A)
Hello, Bob (in Thread-B)
```

全局变量 `local_school` 就是一个 `ThreadLocal` 对象，每个 `Thread` 对它都可以读写 student 属性，但互不影响。你可以把 `local_school` 看成全局变量，但每个属性如 `local_school.student` 都是线程的局部变量，可以任意读写而互不干扰，也不用管理锁的问题，ThreadLocal 内部会处理。

可以理解为全局变量 `local_school` 是一个 `dict`，不但可以用 `local_school.student`，还可以绑定其他变量，如 local_school.teacher 等等。

ThreadLocal最常用的地方就是为每个线程绑定一个数据库连接，HTTP请求，用户身份信息等，这样一个线程的所有调用到的处理函数都可以非常方便地访问这些资源。

### 4. 进程 vs 线程

进程更稳定

### 5. 分布式进程

file > task_master.py 

file > task_master.py

Python 的 `multiprocessing` 模块不但支持多进程，其中 `managers` 子模块还支持把多进程分布到多台机器上。一个服务进程可以作为调度者，将任务分布到其他多个进程中，依靠网络通信。由于 `managers` 模块封装很好，不必了解网络通信的细节，就可以很容易地编写分布式多进程程序。

authkey 可以保证两台机器正常通信，不被其他机器恶意干扰。如果 `task_worker.py` 的 `authkey` 和`task_master.py` 的 `authkey` 不一致，肯定连接不上。

Python 的分布式进程接口简单，封装良好，适合需要把繁重任务分布到多台机器的环境下。

注意 Queue 的作用是用来传递任务和接收结果，每个任务的描述数据量要尽量小。比如发送一个处理日志文件的任务，就不要发送几百兆的日志文件本身，而是发送日志文件存放的完整路径，由Worker进程再去共享的磁盘上读取文件。

## 十、正则表达式

### 1. `re` 模块

使用 Python 的 `r` 前缀，就不用考虑转义的问题了：

```py
# \ 在 python str 和 正则表达式里都是 转义字符
# 最好使用 r 前缀
s = r'ABC\-001'
```

|正则表达式|匹配内容|
|---|---|
| `\d` | 一个数字 |
| `\w` | 一个字母或数字 |
| `.` | 一个任意字符 |
| `*` | 0 ~ n 个字符 |
| `+` | 1 ~ n 个字符 |
| `？` | 0 或 1 个字符 |
| `{n}` | n 个字符 |
| `{n, m}` | n ~ m 个字符 |
| `[]` | 表示范围 |
| `A|B` | A 或者 B |
| `^` | 行的开头 |
| `$` | 行的结束 |
| `()` | 提取子串 |

### 2. match 判断匹配

```py
import re
test = '用户输入的字符串'
if re.match(r'正则表达式', test):
    print('ok')
else:
    print('failed')
```

### 3. split 切分字符串

```py
import re

'a b   c'.split(' ') # 普通的切分

re.split(r'\s+', 'a b   c')
re.split(r'[\s\,]+', 'a,b, c  d')
re.split(r'[\s\,\;]+', 'a,b,;; c  d')
```

### 4. 分组 ()

如果正则表达式中定义了组，就可以在Match对象上用group()方法提取出子串来。

注意到group(0)永远是原始字符串，group(1)、group(2)……表示第1、2、……个子串。

```py
import re
m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
m.groups() # ('010', '12345')
m.group(0)
m.group(1)
m.group(2)
```

### 5. 贪婪匹配

正则匹配默认是贪婪匹配，也就是匹配尽可能多的字符。

```py
import re
# 贪婪匹配
re.match(r'^(\d+)(0*)$', '102300').groups()

# 非贪婪匹配
re.match(r'^(\d+?)(0*)$', '102300').groups()
```

### 6. 编译
当我们在Python中使用正则表达式时，re模块内部会干两件事情：

1. 编译正则表达式，如果正则表达式的字符串本身不合法，会报错；
2. 用编译后的正则表达式去匹配字符串。

如果一个正则表达式要重复使用几千次，出于效率的考虑，我们可以预编译该正则表达式，接下来重复使用时就不需要编译这个步骤了，直接匹配：

```py
import re
# 编译:
re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')
# 使用：
# 编译后生成 Regular Expression 对象，由于该对象自己包含了正则表达式，所以调用对应的方法时不用给出正则字符串。
re_telephone.match('010-12345').groups()
('010', '12345')
re_telephone.match('010-8086').groups()
('010', '8086')
```

## 十一、常用内建模块

### 1. datetime

datetime 表示的时间需要时区信息才能确定一个特定的时间，否则只能视为本地时间。

如果要存储 datetime，最佳方法是将其转换为 timestamp 再存储，因为 timestamp 的值与时区完全无关。

### 2. collections

`collections` 模块提供了一些有用的集合类，可以根据需要选用。

#### namedtuple

`namedtuple` 是一个函数，它用来创建一个自定义的 `tuple` 对象，并且规定了 `tuple` 元素的个数，并可以用属性而不是索引来引用 `tuple` 的某个元素。

这样一来，我们用 `namedtuple` 可以很方便地定义一种数据类型，它具备 `tuple` 的不变性，又可以根据属性来引用，使用十分方便。

#### deque

使用 `list` 存储数据时，按索引访问元素很快，但是插入和删除元素就很慢了，因为 `list` 是线性存储，数据量大的时候，插入和删除效率很低。

`deque` 是为了高效实现插入和删除操作的双向列表，适合用于队列和栈。

#### defaultdict

使用 `dict` 时，如果引用的 `Key` 不存在，就会抛出 `KeyError`。如果希望 `key` 不存在时，返回一个默认值，就可以用 `defaultdict`.

#### OrderedDict


#### Counter



### 3. base64


### 4. struct


### 5. hashlib


### 6. itertools


### 7. contextlib


### 8. XML


### 9. HTMLParser


### 10. urllib



## 十二、常用第三方模块

### PIL / Pillow

PIL 仅支持 Python2

安装 Pillow：

    $ sudo pip3 install pillow

## 十三、 virtualenv


## 十四、图形界面


## 十五、网络编程


## 十六、电子邮件


## 十七、访问数据库


## 十八、 web 开发


## 十九、异步 IO


## 二十、实战


