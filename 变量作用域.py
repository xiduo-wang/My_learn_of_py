# for循环中的临时变量 其作用域限定范围为循环内部 如需要访问临时变量 可以先在循环外对其进行定义
i = 0
for i in range(10):
    print(i)
print(i)