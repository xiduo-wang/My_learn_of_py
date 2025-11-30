# 如果函数没有使用return语句返回数据 那么函数有返回值吗
# 有的兄弟 有的 会返回字面量None 代表无意义 空的
def say_hello():
    print("你好吗")
result = say_hello()
print(result)
print(f"内容类型为{type(result)}")

def say_bye():
    print("拜拜")
    return None
result2 = say_bye()
"""
None可用于if判断 等同与False
一般用于在函数中主动返回None 配合if做相关处理

定义变量 但暂时不需要变量有具体值时 可以使用None来替代
"""
def check_age(age):
    if age > 18:
        return "SUCCESS"
    else:
        return None
result3 = check_age(16)
if not result3:
    print("未成年 不能进入")
# if not 的含义是 结果是False时才执行 与if 相反
