# 使用while循环嵌套打印99乘法表
# 额外知识点1 想要让print语句输出不换行 只需在语句后加上end=''
# 如 print("hello",end='')
# 额外知识点2 在字符串中的符号\t 效果等同于按下tab键 可以让多行字符串对齐
"""print("hello",end='')
print("world",end='')
"""

"""print("Hello\tworld")
print("xi\tduo")
"""
# 控制行的循环 i <= 9 控制每一行输出的循环 j <= i
i = 1
while i <= 9:
    j = 1
    while j <= i:
        print(f"{j}*{i}={j*i}\t",end='')
#终止内层循环
        j += 1
# 终止外层循环
    i += 1
    # 换行
    print()