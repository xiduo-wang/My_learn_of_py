# 掌握lambda函数的语法
# def关键字可以定义带有名称的函数 lambda关键字可以定义匿名的函数(无名称)
# 有名称的函数 可以多次调用 无名称的函数只能临时使用一次
# 语法：lambda 传入参数:函数体(代码) 函数体满足一行能够结束
"""
def test_func(computer):
    result = computer(3,4)
    print(f"computer的类型是{type(computer)}")
    print(result)
def computer(x,y):
    return x + y
"""
# 相同输出
def test_func(computer):
    result = computer(3,4)
    print(result)
test_func(lambda x,y:x + y)