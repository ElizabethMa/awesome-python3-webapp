# awesome-python3-webapp

## python3 实验课

[廖雪峰官网 python](http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000) 练习+笔记

### 基础 `/lessons/basic/*.py`

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

|字符|ASCII|Unicode|UTF-8|
|---|---|---|---|
|A|`01000001`|`00000000 01000001`|`01000001`|
|中|x|`01001110 00101101`|`11100100 10111000 10101101`|
||一个字节，无法表示中文等语言|每个字符都用两个字节表示，表示英文时太浪费空间|一个字节表示英文，三个字节表示中文|

搞清楚了ASCII、Unicode和UTF-8的关系，我们就可以总结一下现在计算机系统通用的字符编码工作方式：

在计算机内存中，统一使用Unicode编码，当需要保存到硬盘或者需要传输的时候，就转换为UTF-8编码。

用记事本编辑的时候，从文件读取的UTF-8字符被转换为Unicode字符到内存里，编辑完成后，保存的时候再把Unicode转换为UTF-8保存到文件：

7. list and tuple `list_tuple.py`
8. 条件和循环 `statements.py`
9. dict and set `dict_set.py`

### 函数 `lessons/functions/functions.py`

+ [python3 文档](https://docs.python.org/3/index.html) [abs 函数在线说明](https://docs.python.org/3/library/functions.html#abs)
+ 命令行 `help(abs)` 查看 abs 函数的帮助说明

1. 数据类型转换函数
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