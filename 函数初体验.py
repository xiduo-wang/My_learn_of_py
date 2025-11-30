# 组织好的 可重复使用的 用来实现特定功能的代码段
name = "wangxiduo"
length = len(name)
print(length)
# 本质
count = 0
for i in name:
    count += 1
# 使用函数来优化过程
def my_length(data):
    count = 0
    for i in data:
        count += 1
    print(f"字符串{data}的长度是{count}")
my_length(name)
# 函数可以针对特定需求 重复利用 提高开发效率