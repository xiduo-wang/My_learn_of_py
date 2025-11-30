# 掌握使用构造方法向成员变量赋值
# 之前一个一个赋值过于麻烦 这里我们可以使用更简洁的方式赋值
"""
Python类可以使用：__init__()方法 称之为构造方法
可以实现：
在创建类对象(构造类)的时候，会自动执行
在创建类对象(构造类)的时候，将传入参数自动传递给__init__方法使用
"""
# 演示：
class Student:
    def __init__(self,name,age,tel):
        self.name = name  # 完成了成员变量的命名和赋值
        self.age = age
        self.tel = tel
        print("Student类创建了一个类对象")
stu = Student('xiduo',18,111222)
print(stu.name,stu.age,stu.tel)