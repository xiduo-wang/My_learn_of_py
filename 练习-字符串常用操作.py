my_str = "itheima itcast boxuegu"
num = my_str.count("it")
print(f"字符串中有{num}个it字符")

new_str = my_str.replace(" ","|")
print(f"替换后的新字符串为{new_str}")

new_list = new_str.split("|")
print(f"通过split方法得到的列表为{new_list}")