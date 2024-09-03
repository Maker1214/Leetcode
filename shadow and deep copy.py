# shadow copy : 先建構一個新的物件，再將原始物件中的"子物件參照"插入其中，用list()的效果跟copy()相同

a = [[0,1],2,3]
b = a.copy()
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