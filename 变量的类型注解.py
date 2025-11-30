# 理解为什么使用类型注解
# 掌握变量的类型注解语法
# 调用方法进行传参时，使用ctrl+p可以弹出传参提示
# pycharm无法通过代码确定传参类型，这时需要用到类型注解
"""
类型注解语法：
基础数据类型注解
  变量：类型
    a:int
    b:float
    类对象也可以进行类型注解
  stu:Student = Student()
  数据容器也可以进行类型注解
  基础语法同上
  数据容器也可进行详细注解，对存储的数据也可以进行注解
  注意：元组进行注解时需要将每一个元素都进行标记 字典类型设置详细注解 需要2个类型(key,value)
"""
# 基础数据类型实例
var_1:int = 10
var_2:str = 'xiduo'
var_3:float = 2.5
var_4:bool = True
# 类对象进行注解
class Student:
    name = None
stu:Student = Student()
# 数据容器注解
my_list:list[int] = [1,2,3]
my_tuple:tuple[int,str,bool] = (1,'xiduo',True)
my_set:set[int] = {1,2,5,6}
my_dict:dict[str,int] = {'xiduo':1,'zsq':2}
my_str:str = 'nb'
# 第二种方法
# 使用注释中进行注解
i = 1 # type:int
list_1 = [1,2,3] # type:list[int]

# 函数和方法类型注解
# 形参的类型注解
"""
def 函数方法名(形参名:类型.......)
"""
def add(x:int,y:int):
    return x + y
add(1,2)
# 返回值类型注解
"""
def 函数方法名(形参名:类型.......) -> 返回值类型
"""
def add(x:int,y:int) -> int:
    return x + y
n = add(1,2)
print(n)
# Union类型联合注解
# 处理混合类型参数
# 使用Union[类型1,类型2,....] 可以定义联合类型注解
from typing import Union
my_list3:Union[list[int],list[str]] = [1,2,3]
my_dict3:Union[dict[str,int],dict[str,str]] = {'xiduo':1,'zsq':2,3:'3'}