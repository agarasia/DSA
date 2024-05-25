import math

# Approach: Linearly check for all possible times and find
#           the most feasible one.
def minTimeToEat(piles, time):
    # Find the maximum number of bananas in a pile
    def maximum():
        ans = -float('inf')
        for i in piles:
            if i > ans:
                ans = i
        return ans
    
    # Find the total tme needed to finish all bananas
    def requiredTime(hourly):
        n = len(piles)
        ans = 0
        for i in range(n):
            ans += math.ceil(piles[i]/hourly)
        
        return ans

    maxI = maximum()
    
    # Check for the most feasible rate of eating
    for i in range(1, maxI + 1):
        totalTime = requiredTime(i)
        if totalTime <= time:
            return i
    
    return maxI
# T(n) = O(n * maxI)

# Approach: Employ Binary Search to prune the search space
def minTimeToEatOptimal(piles, time):
    def maximum():
        ans = -float('inf')
        for i in piles:
            if ans < i:
                ans = i
        
        return ans
    
    def requiredTime(hourly):
        totalTime = 0
        for i in range(len(piles)):
            totalTime += math.ceil(piles[i] / hourly)
        return totalTime
    
    low, high = 1, maximum()

    while low <= high:
        mid = low + (high-low)//2
        if requiredTime(mid) <= time:
            high = mid - 1
        else:
            low = mid + 1
    
    return low
# T(n) = O(n * log(maxI))

piles = [3, 6, 7, 11]
time = 8

print(minTimeToEat(piles, time), minTimeToEatOptimal(piles, time))