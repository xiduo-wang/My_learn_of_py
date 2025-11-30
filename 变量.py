# 变量就是在程序运行时记录数据所使用的一个盒子
# 即能储存计算结果或者能表示值的抽象概念
# 格式：变量名称 = 变量值
# 定义一个变量 记录钱包余额
money = 50
print("钱包还有：",money)
# 买了一个冰激淋，花费了十元
money = money - 10
print("买了冰激淋花费了10元，还剩：",money)


# 假设，每隔一小时输出一次钱包余额
print("现在是下午一点，钱包余额剩余：",money)
print("现在是下午二点，钱包余额剩余：",money)
print("现在是下午三点，钱包余额剩余：",money)
print("现在是下午四点，钱包余额剩余：",money)
# 定义变量是为了重复使用它

# 练习：
money = 50
print("当前钱包余额：",money)
ice = 10
cola = 5
print("购买了冰激淋，花费：",ice)
print("购买了可乐，花费：",cola)
money = money - ice - cola
print("最终钱包剩余：",money)