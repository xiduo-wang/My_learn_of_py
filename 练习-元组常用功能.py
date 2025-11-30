my_tuple = ('王喜多',18,['basketball','csgo'])
index = my_tuple.index(18)
print(f'年龄的下标位置是{index}')
print(f'学生的姓名是{my_tuple[0]}')
del my_tuple[2][0]
print(f'删除后的结果为{my_tuple}')
my_tuple[2].append('coding')
print(f'增加后的结果为{my_tuple}')