# 用 "=" 將a1 賦值給 b1時，b1的記憶體位置跟a1的記憶體位置相同，因此若修改b1的值，a1的值也會跟著修改
a1 = [1,2,3]
b1 = a1

print("a1:", id(a1))
print("b1:", id(b1))

b1[0] = 4
print("a1's value:", a1)
print("b1's value:", b1)

# shadow copy : 先建構一個新的物件，再將原始物件中的"子物件參照"插入其中，用list()的效果跟copy()相同

a = [[0,1],2,3]
b = a.copy() #b的記憶體位置跟 a 不同，但因為是 shadow sopy，所以b[0]的記憶體位置與a[0]的記憶體位置依然相同，要解決這個問題需要使用deep copy
c = list(a)
b[0][0] = 1 #原始物件中的物件(子物件)
b[2] = 4 #原始物件
b[1] = 5 #原始物件
c[1] = 6
c[2] = 7

print('a:', id(a), id(a[0]), id(a[1]), id(a[2]), a)
print('b:', id(b), id(b[0]), id(b[1]), id(b[2]), b)
print('c:', id(c), id(c[0]), id(c[1]), id(c[2]), c)

# deep copy
import copy
d = [1, []]
e = copy.deepcopy(a)
print('d:', id(d), id(d[0]), id(d[1]))
print('e:', id(e), id(e[0]), id(e[1]))

# 多維陣列初始化方式
f = [[i] for i in range(5)]
f[0][0] = 1
print("f's value:", f)
for j in range(5):
    print(f"f's add is {id(f[j][0])}")

# https://docs.python.org/3.10/faq/programming.html#faq-multidimensional-list
# 不work的多維陣列初始化方式
# The reason is that replicating a list with * doesn’t create copies, it only creates references to the existing objects. 
# The *3 creates a list containing 3 references to the same list of length two. Changes to one row will show in all rows, which is almost certainly not what you want.
g = [[0]] * 5
g[0][0] = 1
print("g's value:", g)
for k in range(5):
    print(f"g's add is {id(g[k][0])}")


a = [1,2]
b = [3,4]
c = [[5,6]]

print(a + b) # [1,2,3,4]
print(a + c) #[1,2,[5,6]]
a.append(b)
print(a) # [1,2,[3,4]]

# unpacking
nums = [1,2,3]
a, b, c = nums
print(f"a's value is {a}, b's value is {b}, c's value is {c}")
