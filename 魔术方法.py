# 掌握几种常用的类内置方法
# 之前学习的__init__方法就是内置方法的一种
# 这里只记录几个常用的方法
# __str__字符串方法
# 通过该方法可以控制对象转换为字符串
class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
# __str__方法将类对象转换为字符串
    def __str__(self):
        return f'Student类对象，name：{self.name}，age：{self.age}'
# __lt__ 小于符号比较方法
# 直接两个对象比较是不可以的，但可以在类中实现__lt__方法 同时完成：小于符号和大于符号两种比较
    def __lt__(self, other):
        return self.age < other.age
stu1 = Student('xd',11)
stu2 = Student('sq',115)
print(stu1 > stu2)
print(stu1 < stu2)
# __le__ 小于等于or大于等于(用法同lt)
# __eq__ 相等判断，同上