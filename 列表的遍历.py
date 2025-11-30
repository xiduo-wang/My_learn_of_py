# 列表的遍历-while循环
# 将数据容器中的元素依次取出进行处理的操作 称为遍历
"""
while:
先用变量接收列表下标
循环控制变量通过下标索引来控制，默认为0
每一次循环将下标索引变量+1
循环条件：下标索引变量 < 列表元素数量
"""
my_list = ["wangxiduo","zsq",'thy']
index = 0   # 下标索引初始值默认为0
while index < len(my_list):
    element = my_list[index]
    print(f'列表中的元素为{element}')
    index += 1

"""
for:
for 临时变量 in 数据容器：
    对临时变量进行处理
"""


def list_for_func():
        two_list = [1,2,3,4,5]
        for i in two_list:
            print(f'列表中的元素有{i}')
list_for_func()

# while循环可以制定循环条件 for循环只能一个个从容器中取出数据
