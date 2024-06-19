print("AND 位元運算")
print(f"0 AND 0 : {0 & 0}")
print(f"0 AND 1 : {0 & 1}")
print(f"1 AND 0 : {1 & 0}")
print(f"1 AND 1 : {1 & 1}")


print("OR 位元運算")
print(f"0 OR 0 : {0 | 0}")
print(f"0 OR 1 : {0 | 1}")
print(f"1 OR 0 : {1 | 0}")
print(f"1 OR 1 : {1 | 1}")

print("XOR 位元運算")
print(f"0 XOR 0 : {0 ^ 0}")
print(f"0 XOR 1 : {0 ^ 1}")
print(f"1 XOR 0 : {1 ^ 0}")
print(f"1 XOR 1 : {1 ^ 1}")

number = 3
print("乘以2的次方")
print(f"{number} 乘以2的0次方 : {number << 0}")
print(f"{number} 乘以2的1次方 : {number << 1}")
print(f"{number} 乘以2的2次方 : {number << 2}")
print(f"{number} 乘以2的3次方 : {number << 3}")

number = 7
print("除以2的次方")
print(f"{number } 除以2的1次方 : {number >> 1}")


numbers = [1,4,2,4,1]

output = numbers[0]

for i in range(1, len(numbers)):
    output ^= numbers[i]

print(output)


