

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


