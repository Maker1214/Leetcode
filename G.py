"""
#不一樣的binary search : 方法1 每次掃左跟右看是否target字串包含在input_str中, 時間複雜度 : O(n)
input_str = ["a", "aa", "aaa", "aaaa", "aab", "aabc", "aabcc", "ab", "aacc", "bb", "aaccd", "aabb"]

#sorted會複製一份list後，對複製的list做排序後回傳複製的list
#print(f"sorted : {sorted(input_str)}")
#print(f"input_str : {input_str}")
#sort會直接修改原list, 無回傳值
input_str.sort()
print(f"input_str : {input_str}")

target = "bb"

l , r = 0, len(input_str) - 1
lf, rf = False, False

while(not lf or not rf):
    if not lf and target != input_str[l][:len(target)]:
        l += 1
    else:
        lf = True
    if not rf and target != input_str[r][:len(target)]:
        r -= 1
    else:
        rf = True

print(f"the first one is {l}, the last one is {r}") 
"""

#不一樣的binary search : 方法2 binary search 時間複雜度 : O(logn)
input_str = ["a", "aa", "aaa", "aaaa", "aab", "aabc", "aabcc", "ab", "aacc", "bb", "aaccd", "aabb"]
target = "aaa"

input_str.sort()
for i in range(len(input_str)):
    print(f"第{i}個值為{input_str[i]}")

l = 0
r = len(input_str) - 1

def findMid(l, r):
    m = (r + l) // 2
    
    while(target != input_str[m][:len(target)]):
        if target > input_str[m][:len(target)]:
            l = m + 1
            #print("往右邊找")
        else:
            r = m - 1
            #print("往左邊找")
        m = (r + l) // 2
    return m

def L_Bound(l, r):    
    while(r - l > 1):
        m = (r + l) // 2
        if target != input_str[m][:len(target)]:
            l = m
        else:
            r = m
    return r

def R_Bound(l, r):
    
    while(r - l > 1):
        m = (r + l) // 2
        if target != input_str[m][:len(target)]:
            r = m
        else:
            l = m
    return l


middle = findMid(l, r)
print(f"middle is {middle}")


LB = L_Bound(0, middle)
print(f"left bound is {LB}")

RB = R_Bound(middle, len(input_str) - 1)
print(f"right bound is {RB}")



""" 
import random

number = int(input("擲幾次骰子:"))

for i in range(1, number + 1):
    print(f"第{i}次 : {random.randint(1,6)}") """


"""
import random
times = 9

for i in range(10):
    input_number = random.randint(0,times)

    if input_number % times <= 2: print(f"第{i + 1}次, 1")
    elif 3 <= input_number % times <= 4: print(f"第{i + 1}次, 2")
    elif input_number % times == 5: print(f"第{i + 1}次, 3")
    elif input_number % times == 6: print(f"第{i + 1}次, 4")
    elif input_number % times == 7: print(f"第{i + 1}次, 5")
    else: print(f"第{i + 1}次, 6")
"""