# 了解模块的导入及自定义模块
"""
Python模块(Module)，是一个Python文件，以.py结尾
模块能定义函数 类 和变量 模块里也能包含可执行的代码
作用：python中的模块可以帮我们快速实现一些功能
例如实现时间相关的功能可以使用time模块
我们可以认为一个模块就是一个工具包 每一个工具包有它不同的功能
帮我们实现不同的需求
"""
# 模块的导入方式
# 语法：[from 模块名] import [模块 | 类 | 变量 | 函数 |*][as 别名]
# import 模块名
# import 模块名1,模块名2
# 模块名.功能名()

# 导入时间模块并使用程序睡眠功能
import time
print("你好")
time.sleep(5)   # .后面的代表模块内部的函数
print("我是王喜多")

# 使用from模块名导入time模块
# from 模块名 import 功能名
# 功能名()
print("你好吗")
from time import sleep
sleep(3)
print("我很好")

# from 模块名 import *
# 代表导入模块中所有的功能
i = 0
print(i)
from time import *
sleep(3)
print(f"zsq是{i}")

# as[别名] 起到给模块完成改名的效果
print("nb")
import time as t
t.sleep(1)
print("克拉斯")

# 完成程序时 一般在开头进行模块的导入

# 自定义模块
"""
import my_moudle1
my_moudle1.test(1,2)
"""
# 注意：当导入多个模块时 且模块内有同名功能 当调用这个同名功能时 调用的是后面导入的模块
"""
from my_moudle1 import test
from my_moudle2 import test
test(3,4)
"""
from my_moudle1 import *
test_a(1,2)
# test_b(1,2)  由于all变量的设置 test_b不能被调用