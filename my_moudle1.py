# 与python模块共同食用
__all__ = ['test_a']
def test_a(a,b):
    print(a + b)
    return a + b
def test_b(a,b):
    print(a - b)
if __name__ == '__main__':   # 测试模块 当作为模块导入时不被调用
    test_a(1,2)
# all变量  __all__ = [] 列表类型变量 在模块导入后使用*时 只能调用all变量中的
# 可以简单理解为 all变量定义了"全部"这个概念