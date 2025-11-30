money = 5000000
name = None
name = input("请输入您的姓名")
# 查询函数
def check_money(show_header):
    if show_header == True:  # 用if来判断是否输出查询余额
       print("---------查询余额----------")
    print(f"{name}，您好，您的余额剩余{money}元")
# 存款函数
def saving(num):
    global money
    money += num
    print("---------存款----------")
    print(f"{name}，您好，您存款{num}元成功")
    # 调用check函数查询余额
    check_money(False)
# 取款函数
def get_money(num):
    global money
    money -= num
    print("---------取款----------")
    print(f"{name}，您好，您取款{num}元成功")
    # 同存款函数
    check_money(False)
# 主菜单
def main():
    print("---------主菜单----------")
    print(f"{name}，您好，欢迎来到xiduoATM，请选择操作")
    print("查询余额\t【输入1】")
    print("存款\t\t【输入2】")
    print("取款\t\t【输入3】")
    print("退出\t\t【输入4】")
    return input("请输入您的选择：")
# 设置无限循环 确保程序不会退出
while True:
    keyboard_input = main()
    if keyboard_input == "1":
        check_money(True)
        continue  # 通过continue继续下一次循环
    elif keyboard_input == "2":
        num = int(input("您想要存多少钱："))
        saving(num)
        continue
    elif keyboard_input == "3":
        num = int(input("您想要取多少钱："))
        get_money(num)
        continue
    else:
        print("程序已退出")
        break   # 通过break退出循环
