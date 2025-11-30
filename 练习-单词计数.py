count = 0
with open("D:/word.txt.txt", 'r', encoding='UTF-8') as f: # 注意修正文件名
     for line in f:
# 将行拆分成单词并统计
        words = line.strip("\n").split()
        count += words.count('itheima')
print(f"该文件中有：{count}个'itheima'单词") # 循环结束后输出最终结果