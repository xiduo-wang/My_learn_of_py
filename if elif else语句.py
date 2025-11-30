# 掌握用if elif else语句进行多条件判断
print("欢迎来到喜多动物园。")
height = int(input("请输入您的身高(cm)："))
vip_level = int(input("请输入您的vip等级(1~5)："))
day = int(input("请告诉我今天几号"))
if height < 120:
    print("您的身高小于120，可以免费游玩")
elif vip_level > 3:
    print("您的vip等级大于3，可以免费游玩")
elif day == 1:
    print("今天是免费日，可以免费游玩")
else:
    print("不好意思，所有条件都不符合，需要购票10元")
print("祝您游玩愉快")
"""
elif可以多次使用 且判断是有顺序且互斥的 满足1就不会理会2和3
满足2就不会理会3 都不符合就进入else 
若不写else 则等同于3个独立的if判断
不要忽略空格缩进
"""
# 简洁写法 不定义变量 节省代码量
"""
print("欢迎来到喜多动物园。")
if int(input("请输入您的身高(cm)：")) < 120:
    print("您的身高小于120，可以免费游玩")
elif int(input("请输入您的vip等级(1~5)：")) > 3:
    print("您的vip等级大于3，可以免费游玩")
elif int(input("请告诉我今天几号")) == 1:
    print("今天是免费日，可以免费游玩")
else:
    print("不好意思，所有条件都不符合，需要购票10元")
print("祝您游玩愉快")
"""