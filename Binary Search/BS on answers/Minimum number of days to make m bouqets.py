# Approach: Linearly check for all possible days
def daysNeededBruteForce(bloomDay, m, k):
    # Helper function: Finding minimum in array
    def findMin():
        ans = float('inf')
        for i in bloomDay:
            if i < ans:
                ans = i
        return ans

    # Helper function: Finding maximum in array
    def findMax():
        ans = -float('inf')
        for i in bloomDay:
            if i > ans:
                ans = i
        return ans

    # Helper function: Checking if we can make m bouqets on ith day
    def isPossible(day):
        n = len(bloomDay)
        bouqets = 0
        count = 0

        for i in range(n):
            if bloomDay[i] <= day:   count += 1
            else:
                bouqets += count // k
                count = 0
        
        bouqets += count // k
        return bouqets >= m
    
    # Driver code
    if m*k > len(bloomDay): return -1

    mini = findMin()
    maxi = findMax()

    # Checking all possible days
    for i in range(mini, maxi+1):
        if isPossible(i):
            return i
            
    return -1
# T(n)= O(n * (maxi - mini))

# Approach: Optimize the checking process using Binary search
def daysNeededOptimal(bloomDay, m, k):
    # Helper function: Finding minimum in array
    def findMin():
        ans = float('inf')
        for i in bloomDay:
            if i < ans:
                ans = i
        return ans

    # Helper function: Finding maximum in array
    def findMax():
        ans = -float('inf')
        for i in bloomDay:
            if i > ans:
                ans = i
        return ans

    # Helper function: Checking if we can make m bouqets on ith day
    def isPossible(day):
        n = len(bloomDay)
        bouqets = 0
        count = 0

        for i in range(n):
            if bloomDay[i] <= day:   count += 1
            else:
                bouqets += count // k
                count = 0
        
        bouqets += count // k
        return bouqets >= m
    
    # Driver code
    if m*k > len(bloomDay): return -1

    low, high = findMin(), findMax()
    ans = 0

    # Using binary search to find the lower
    # bound of the answer
    while low <= high:
        mid = low + (high-low)//2
        if not isPossible(mid):
            low = mid + 1
        else:
            ans = mid
            high = mid - 1
    
    return ans
# T(n)= O(n * log(maxi - mini))

bloomDay = [7,7,7,7,12,7,7]
bouqets = 2
flowersInBouqet = 3

print(daysNeededBruteForce(bloomDay, bouqets, flowersInBouqet))
print(daysNeededOptimal(bloomDay, bouqets, flowersInBouqet))
