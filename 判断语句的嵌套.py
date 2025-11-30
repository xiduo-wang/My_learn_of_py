# 掌握判断语句的嵌套
"""
语法格式：
if 条件1:
    满足——
    不满足——
    if 条件2:
        满足——
        不满足——  其中条件2是在满足条件1的情况下进行判断
        嵌套过程中注意空格缩进，缩进控制着层次关系
"""
# 案例1
"""print("欢迎来到喜多动物园")
if int(input("请输入你的身高(cm)：")) >120:
    print("你的身高大于120cm，不可以免费")
    print("不过如果你的vip等级大于3，可以免费")
    if int(input("请输入你的vip等级(1-5)：")) >3 :
        print("你的vip等级大于3，可以免费")
    else:
        print("您需要补票10元")
else:
    print("欢迎你小朋友，你可以免费游玩")"""
# 案例2
age = 27
year = 1
rank = 5
if age >= 18:
    print("你是成年人")
    if age < 30:
        print("你的年龄达标了")
        if year > 2:
            print("恭喜你，年龄时间均达标，可以领取奖励")
        elif rank > 3:
            print("您的级别符合条件，可以领取奖励")
        else:
            print("对不起，您只有年龄达标")
    else:
        print("你的年龄未达标")
else:
    print("你未成年")
