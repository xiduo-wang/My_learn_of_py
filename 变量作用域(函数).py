# 局部变量 全局变量
# 局部变量指的是定义于函数体内部的变量 只在函数体内生效 在函数调用时用于临时储存数据
def test_a():
    num = 100
    print(num)
test_a()
# 单独print(num)会报错 出了函数体 局部变量就被销毁
# 全局变量在函数外定义即可
num = 100
def test_b():
    print(num)
def test_c():
    print(num)
test_b()
test_c()
print(num)
# 在函数内定义的变量修改为全局变量 global关键字
num = 200
def test_d():
   print(f"{num}")
def test_e():
    global num
    num = 500
test_d()
test_e()
print(num)
