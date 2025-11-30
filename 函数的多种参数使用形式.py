# 函数的多种传参方式
# 掌握位置参数 关键字参数 掌握不定长参数 掌握缺省参数
# 位置参数 传递的参数和定义的参数的顺序及个数必须一样
# 位置参数 调用函数时根据函数定义的参数位置来传递参数
"""
def user_info(name,age,gender):
    print(f'您的名字是{name},您的年龄是{age},您的性别是{gender}')

user_info('Tom',20,'男')
"""
# 关键字参数
# 函数调用时通过'键=值'的形式传递参数
"""
def user_info(name,age,gender):
    print(f"您的名字是{name},年龄是{age},性别是{gender}")
    
关键字传参
user_info(name = '小明',age = 20,gender = "男")
可以不按照固定顺序
user_info(age = 20,name = '男',gender = "男")
可以和位置参数混用 位置参数必须在前 且匹配参数顺序
user_info('小明',age = 20,gender = "男")
"""
# 缺省参数
# 用于定义函数 为参数提供默认值 调用函数时可不传该默认参数的值
# 所有位置参数必须出现在默认参数前 包括函数定义及调用
# 作用：当调用函数时没有传递参数，就会默认是用缺省参数对应的值
def user_info(name,age,gender = '男'):
    print(f"您的名字是{name},年龄是{age},性别是{gender}")
user_info('xiduo',18)
user_info('lsb',18,'女')
# 错误案例 def user_info(name = 'xiduo',age,gender) 报错 因为默认参数必须在最后

# 不定长参数(可变参数) 用于不确定调用的时候会传递多少个参数
# 位置传递 使用*调用
# 注意：传进的所有参数会被参数变量收集 它会根据传进参数的位置合并为一个tuple
def user_info(*args):
    print(f'args的类型是{type(args)},内容是{args}')
user_info('tom',18)
# 关键字传递
# 使用**调用 参数是“键=值”的形式时，所有的“键=值”都会被参数接收 同时组成字典
def user_info(**kwargs):
    print(f'kwargs的类型是{type(kwargs)},内容是{kwargs}')
user_info(name = 'tom',age = 18)