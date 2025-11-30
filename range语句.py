# for循环中的待处理数据集指的是序列类型 包括但不限于字符串 元组等
# 语法1
# range(num) 获取一个从0开始 到num结束的数字序列(不含num本身)
for x in range(5):
    print(x,end='')
# 语法2
# range(num1,num2) 获取一个从num1开始 到num2结束的数字序列 同语法1
for x in range(5,10):
    print(x,end='')
# 语法3
# range(num1,num2,step) 同2 数字之间步长以step为准 step默认为1
for x in range(5,10,2):
    print(x,end='')