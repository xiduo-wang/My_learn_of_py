credit = 100000
for i in range(1,21):
    import random
    score = random.randint(1, 10)

    if score < 5:
        print(f"员工{i}绩效分为{score}，不满足，不发工资")
        continue

    # 判断余额是否充足
    if credit >= 1000:
        credit -= credit
        print(f"员工{i}，满足条件，发放工资1000元，公司账户余额为{credit}")
    else:
        print(f"余额不足，当前余额：{credit}元")
        break