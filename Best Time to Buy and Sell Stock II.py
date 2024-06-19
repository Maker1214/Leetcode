#DP- memoization

prices = [7,1,5,3,6,4]
sell, profit = prices[-1], 0

for p in range(len(prices)-1,-1,-1):    
    if prices[p] < sell:
        buy = prices[p]
        profit += sell - buy
    sell = prices[p]

print(profit)
