def maxProfitNaive(stocks):
    maxProfit = 0
    for i in range(len(stocks)):
        for j in range(i, len(stocks)):
            maxProfit = max(maxProfit, stocks[j] - stocks[i])
    return maxProfit
            

def maxProfit(stocks):
    left, right = 0, 1
    maxProfit = 0
    while right < len(stocks):
        currProfit = stocks[right] - stocks[left]
        if stocks[left] < stocks[right]:
            maxProfit = max(maxProfit, currProfit)
        else:   left = right
        right += 1
        
    return maxProfit

stock = [7, 3, 2, 1, 6]
print(maxProfit(stock))