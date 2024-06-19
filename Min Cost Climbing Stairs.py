costs = [1,100,1,1,1,100,1,1,100,1]
costs.append(0)


for i in range(2,len(costs)):
    costs[i] += min(costs[i-1], costs[i-2])

print(costs[-1])



