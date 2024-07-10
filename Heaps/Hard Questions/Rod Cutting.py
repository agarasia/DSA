# Approach: Use dynamic programming and memoization
def value(prices):
    n = len(prices)
    dp = [0] * (n + 1) 
    for i in range(1, n + 1):
        max_value = -float('inf')
        for j in range(1, i + 1):
            max_value = max(max_value, prices[j - 1] + dp[i - j])
        dp[i] = max_value
    
    return dp[n]
# T(n) = O(n**2)
# S(n) = O(n)

price = [1, 5, 8, 9, 10, 17, 17, 20]
print(value(price))