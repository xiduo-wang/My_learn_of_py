my_goods = ['apple','banana','cherry']
my_goods.append('grape')
my_goods.append('orange')
my_goods.remove('orange')
my_goods.remove(my_goods[1])
my_goods[-1] = 'pear'
for i in my_goods:
    print(i)
import random
n = random.randint(3,100)
my_list = []
for i in range(n):
    my_list.append(random.randint(1,100))
m = sum(my_list) / n
print(m)
d1 = sum((x-m)**2 for x in my_list) / (n - 1)
d2 = d1 ** 0.5
print(d2)

stu_info = []
n1 = int(input("请输入学生学号："))
n2 = input("请输入学生姓名：")
n3 = int(input("请输入学生成绩："))
print(n1, n2, n3)
student = []
# 检查学号是否已存在
student_exists = False
for student in stu_info:
    if student[0] == n1:  # 检查学号是否已存在
        student_exists = True
        print("该学生已存在！")
        break

if not student_exists:
    stu_info.append([n1, n2, n3])
    print("学生信息添加成功！")
n4 = input("请输入查找学生学号：")
print(n4)
for student in stu_info:
    if student[0] == n4:  # 查找学生信息
        print("学号：", student[0])
        print("姓名：", student[1])
        print("成绩：", student[2])
        break
else:
    print("该学生不存在！")
# 删除学生信息
n5 = input("请输入删除学生学号：")
for i in range(len(stu_info)):
    if stu_info[i][0] == n5:
        del stu_info[i]
        print("学生信息删除成功！")
        break
else:
    print("该学生不存在！")