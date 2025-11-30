# 掌握函数作为参数传递的方法
def test_func(computer):
    result = computer(3,4)
    print(f"computer的类型是{type(computer)}")
    print(result)
def computer(x,y):
    return x + y
test_func(computer)
# 这是一种计算逻辑的传递 而非数据的传递
