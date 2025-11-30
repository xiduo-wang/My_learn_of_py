# 掌握通过注释对函数进行解释说明
# 语法如下
def add(x,y):
    """
    add函数可以接收两个参数 进行两数相加的功能
    :param x: 形参x表示相加的其中一个数字
    :param y: 形参y表示相加的其中一个数字
    :return:返回值是2数相加的结果
    """
    result = x + y
    print(f"2数相加的结果是：{result}")
    return result

