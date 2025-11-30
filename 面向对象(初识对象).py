# 使用对象组织数据
# 在程序中可以像生活中一样设计表格、生产表格、填写表格
# 1.在程序中设计表格，我们称之为：设计类
# 2.在程序中打印生产表格，我们称之为：创建对象
# 3.在程序中填写表格，我们称之为：对象属性赋值

# 设计一个类
class Student:
    name = None
    gender = None
    nationality = None
    native_palce = None
    age = None
# 创建一个对象
stu_1 = Student()
# 给对象属性进行赋值
stu_1.name = 'xiduo'
stu_1.gender = '男'
stu_1.age = 18
stu_1.nationality = 'china'
stu_1.native_palce = 'jilin'
# 打印一下
print(stu_1.name)
print(stu_1.gender)
print(stu_1.age)
print(stu_1.nationality)
print(stu_1.native_palce)