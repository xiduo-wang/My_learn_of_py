num_list = [21,25,21,23,22,20]
num_list.append(31)
two_list = [29,33,30]
num_list.extend(two_list)
print(num_list)
print(num_list[0])
print(num_list[-1])
index = num_list.index(31)
print(f'31的位置是{index}')