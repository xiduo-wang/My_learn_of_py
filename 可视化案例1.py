import json
# 折线图开发
f_us = open("D:/美国.txt",'r',encoding='UTF-8')
us_data = f_us.read()
# 去掉json数据中不符合格式的开头及结尾(我直接删掉了，像黑马那样整太慢了)
us_data.replace("jsonp_1629344292311_69436(",'')
us_data = us_data[:-2]
# json数据转换为字典
us_data2 = json.loads(us_data)
print(type(us_data2))