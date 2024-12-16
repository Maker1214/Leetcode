num = 11

output = 0

while num:
    print(num)
    output += (num >> 1) & 1
    num = num >> 1


print(output)