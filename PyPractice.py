

# import heapq

# points = [[5,-1],[-2,4],[3,3],[1,1]]
# minHeap = []

# for x,y in points: # x = points[0][0] , y = points[0][1]
#     print(x , y)
#     heapq.heappush(minHeap, [(x ** 2 + y ** 2), x, y])

# while minHeap:
#     # 根據第一個element的值來做Min heap
#     print(heapq.heappop(minHeap))



# test = ["A","B"]
# word = "CD"

# test.lower()
# word.lower()

# print(test, word)

# comprehension for initializetion
a = [i for i in range(5)] # [0,1,2,3,4]
b = {i: [i] for i in range(5)}

for key in b:
    print(key, b[key])



accounts = ["John","Aohnsmith@mail.com","john_newyork@mail.com", "john00@mail.com", "johna@mail.com"]

accounts[1:].sort()

print(accounts)

<<<<<<< HEAD
for i in range(9):
    print(f"{i} binary : {i:b}")
    print(f"{-1 * i} binary : {(-1 * i):b}")
=======
a = 3
>>>>>>> 8d275610f1742ecaa2f8f14025187db84f9c02d1


print(~a + 1)

b = -3
print(~((b ^ 0xf) & 0xf))
