# json数据格式
# 什么是json 如何使用json进行数据格式转换
# json是一种轻量级的数据交互格式 可以按照json指定的格式去组织和封装数据
# 本质上是一个带有特定格式的字符串
# json就是一种在各种编程语音中流通的数据格式，负责不同编程语言中的数据传递和交互
# 语法格式为python中的字典或者列表(嵌套的元素为字典)
import json
# 准备一个列表 内部嵌套字典 将其转换为json格式
data = [{"name":"xiduo","age":18},{"name":"zsq","age":19},{"name":"zsc","age":18}]
json_str = json.dumps(data) # 如果需要转换中文 在data后传入一个ensure_ascii = False的参数
print(type(json_str))
print(json_str)
# 准备一个字典 将其转换为json格式
d = {"name":"nb","age":19,"gender":'男'}
json_str2 = json.dumps(d,ensure_ascii= False)
print(type(json_str2))
print(json_str2)
# 将json格式转换回python
s = '[{"name":"xiduo","age":18},{"name":"zsq","age":19},{"name":"zsc","age":18}]'
i = json.loads(s)
print(type(i))
print(i)