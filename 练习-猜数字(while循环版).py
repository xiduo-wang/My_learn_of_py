import random
# 无限次机会 终止条件不宜使用数字累加来判断 应该使用布尔类型本身
# 定义一个变量 记录猜测了多少次
count = 0
flag = True
while flag:
    num = random.randint(1, 100)
    guess_num = int(input("请输入你猜测的数字："))
    count += 1
    if guess_num == num:
        print("猜中了")
        # 增添询问是否再玩一局功能
        n = input("是否再玩一局？")
        if n == '是':
           continue
        else:
            break
    else:
        if guess_num > num:
            print("你猜的大了")
        else:
            print("你猜的小了")
    print(f"你总共猜测了{count}次")
