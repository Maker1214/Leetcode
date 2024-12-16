prices = [7,3,5,1,4,6]

profit, buy = 0, prices[0]

for p in prices:
    if p >= buy:
        profit = max(profit, p - buy)        
    else:
        buy = p
        

print(profit)