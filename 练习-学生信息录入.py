class Student:
    def __init__(self,name,age,address):
        self.name = name
        self.age = age
        self.address = address
        for i in range(1,11):
            print(f"当前录入第{i}位学生信息，总共需录入10位学生信息")
            self.name = input("请输入当前学生姓名：")
            self.age = input("请输入当前学生年龄：")
            self.address = input("请输入当前学生地址：")
            print(f"学生{i}信息录入完成，信息为：【学生姓名：{self.name}，年龄：{self.age},地址：{self.address}】")
stu_1 = Student(1,1,1) # 瞎传两个参让程序能跑