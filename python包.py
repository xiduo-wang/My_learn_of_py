# 掌握如何自定义包和如何安装第三方包
# python包本质上是一个文件夹 里面包含了许多文件(模块)
# 在逻辑上将一批模块归为一类
# python包 = _init.py_ 文件 + 模块
# 导入包
# 语法：import.包名.模块名
# 包名.模块名.目标
import my_package.my_module1
import my_package.my_module2

my_package.my_module1.info_print1()
my_package.my_module2.info_print2()
# ------------------------------------
from my_package import my_module1
from my_package import my_module2
my_module1.info_print1()
my_module2.info_print2()

# ------------------------------------
from my_package.my_module1 import info_print1
info_print1()
from my_package.my_module2 import info_print2
info_print2()

# 通过all变量(在文件init中控制) 控制import *
from my_package import *
my_module1.info_print1()
my_module2.info_print2()


# 第三方包
# 使用pip安装第三方包 打开命令符提示程序 在里面输入：pip install 包名称
import 模块1