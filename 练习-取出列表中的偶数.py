my_list = [1,2,3,4,5,6,7,8,9,10]
index = 0
empty_list = []
while index < len(my_list):
    if my_list[index] % 2 == 0:
        empty_list.append(my_list[index])
        print(f"新列表为{empty_list}")
    index += 1
