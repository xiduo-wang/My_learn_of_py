"""
class 类名称:
      类的属性(定义在类中的变量)
      类的行为(定义在类中的函数)
创建类对象：对象 = 类名称()
"""
# 成员方法的定义方法
"""
def 方法名(self,形参1,形参2,.......形参n)
    方法体
self关键字是成员方法定义时必须填写的
它表示类对象自身的意思
当我们使用类对象调用方法时，self会被python自动传入
在方法内部想要访问成员变量时必须使用self关键字
传参的时候可以忽略self
"""
class Student:
    name = None
    gender = None
    age = None
    def say_hi(self):
        print(f"大家好，我是{self.name}")
    def say_hi2(self,msg):
        print(f"大家好，我是{self.name},{msg}")
stu_1 = Student()
stu_1.name = 'xiduo'
stu_1.say_hi()

stU_2 = Student()
stU_2.name = 'zsq'
stU_2.say_hi2('我是傻逼')

