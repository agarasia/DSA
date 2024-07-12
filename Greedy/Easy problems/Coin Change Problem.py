# Approach: Our aim is to find the greedy way,
#           NOT the correct number of coins needed.
def numOfCoins(V, coins):
    num = 0
    n = len(coins)
    for i in range(n-1, -1, -1):
        while V >= coins[i]:
            V -= coins[i]
            num += 1
    
    return num
# T(n) = O(V)
# S(n) = O(1)

V = 70
coins = [1, 2, 5, 10, 20, 50, 100, 500, 1000]

print(numOfCoins(V, coins))