a = 1
b = 1
k = 0
while k < 98:
    c = a + b
    a = b
    b = c
    k += 1
print(c)