wrong_str = "nohtyP习学，多喜王，逼牛真"
# 要求：得到字符串"王喜多"
true_str = wrong_str[::-1]
true_str2 = true_str[4:8:1]
print(f"任务完成力{true_str2}")


# 法2
first_list = wrong_str.split("，")
true_str = first_list[1]
true_str2 = true_str[::-1]
print(f"ok{true_str2}")