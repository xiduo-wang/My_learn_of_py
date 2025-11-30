# 通过判断语句完成猜数字的案例代码编写
"""
定义一个数字(1-10)随机产生，通过三次判断猜出数字
案例要求：1.数字随机产生
2.有3次机会猜测数字 通过3层if嵌套判断实现
3.每次猜不中，会提示大了或小了
"""
# 通过如下代码，可定义一个变量储存一个1-10的随机数字
import random
num = random.randint(1,10)
guess_num = int(input("输入你猜测的数字："))
if guess_num == num:
    print("恭喜你，一次就猜对了")
else:
    if guess_num > num:
        print("猜大了，再猜一次：")
    else:
        print("猜小了，再猜一次")
guess_num = int(input("再次输入你猜测的数字："))
if guess_num == num:
    print("恭喜你，第二次猜对了")
else:
    if guess_num > num:
        print("猜大了，还有一次机会")
    else:
        print("猜小了，还有一次机会")
guess_num = int(input("最后一次输入你猜测的数字："))
if guess_num == num:
    print("最后一次猜对了，恭喜你")
else:
    if guess_num > num:
        print("猜大了，机会用尽")
    else:
        print("猜小了，机会用尽")
        