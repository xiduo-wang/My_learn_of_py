# 知道函数如何返回多个返回值
# 一个函数由于return会直接退出函数 想要有多返回值 按照返回值的顺序 用逗号隔开即可
# 用变量接收返回值时 需按照返回值的排序接收 支持不同数据类型的数据进行return
def test_return():
    return 1,2,'xiduo'
x,y,z = test_return()
print(x)
print(y)
print(z)