# Approach: Check all possible capacities
def capacityBruteForce(weights, days):
    # Helper Function : Find the days needed to 
    #                   transport all the loads.
    def isPossible(capacity):
        daysNeeded, load = 1, 0
        
        for i in range(len(weights)):
            if load + weights[i] > capacity:
                daysNeeded += 1
                load = weights[i]
            else:
                load += weights[i]

        return daysNeeded <= days

    # Driver Code
    mini = -float('inf')
    maxi = 0
    
    for i in weights:
        mini = max(mini, i)
        maxi += i
    
    for i in range(mini, maxi+1):
        if isPossible(i):
            return i
    
    return maxi
# T(n) = O(n * (sum(arr) - max(arr)))

# Approach: Optimize the pruning process by
#           binary search
def capacityOptimal(weights, days):
    # Helper function: Check if days needed with
    #                  current capacity is lesser.
    def isPossible(capacity):
        daysNeeded, load = 1, 0
        for i in range(len(weights)):
            if load + weights[i] > capacity:
                daysNeeded += 1
                load = weights[i]
            else:
                load += weights[i]
        
        return daysNeeded <= days
    
    # Driver Code
    low = -float('inf')
    high = 0
    
    for i in weights:
        low = max(low, i)
        high += i

    while low <= high:
        mid = low + (high-low)//2
        if not isPossible(mid):
            low = mid + 1
        else:
            high = mid - 1
    
    return low
    
weights = [1,2,3,4,5,6,7,8,9,10]
days = 5

print(capacityBruteForce(weights, days))
print(capacityOptimal(weights, days))