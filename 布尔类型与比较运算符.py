# 掌握布尔类型用于表示：真和假
# 掌握比较运算符用于计算：真和假
# 布尔类型只有两类 ture false
"""
比较运算符：
1.== 比较是否相等
2.!= 比较是否不相等
3.>
4.<
5.>=
6.<=
"""
# 定义变量存储布尔类型的数据
# 字面量True Flase 首字母大写
bool_1 = True
bool_2 = False
print(f"bool_1变量的内容是：{bool_1}",f"类型是：{type(bool_1)}")
print(f"bool_2变量的内容是：{bool_2}",f"类型是：{type(bool_2)}")
# 比较运算符的使用
num_1 = 10
num_2 = 10
print(f"10 == 10的结果是：{num_1 == num_2}")
num_3 = 10
num_4 = 20
print(f"10 == 20的结果是：{num_3 == num_4}")
name_1 = "wang xi duo"
name_2 = "li bo hao"
print(f"两人名字是否相同的结果为：{name_1 == name_2}")
num_5 = 10
num_6 = 15
print(f"10 > 15结果是：{num_5 > num_6}")
print(f"10 < 15结果是：{num_5 < num_6}")
num_7 = 10
print(f"10 >= 10结果是：{num_5 >= num_7}")