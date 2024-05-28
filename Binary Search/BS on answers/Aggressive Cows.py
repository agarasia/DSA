# Approach: Check for all possible answers and then 
#           return when able to place
def maximumMinimumDistanceBruteForce(stalls, cows):
    # Helper function: Helps in checking whether we
    #                  can place k cows in stables
    def canWePlace(distance):
        n = len(stalls)
        cntCows = 1
        last = stalls[0]

        for i in range(1, n):
            if stalls[i] - last >= distance:
                cntCows += 1
                last = stalls[i]
            if cntCows >= cows: return True
        
        return False
    
    # Driver Code
    n = len(stalls)
    stalls.sort()
    limit = stalls[n-1] - stalls[0]

    for i in range(1, limit+1):
        if not canWePlace(i):
            return i-1

    return limit

def maximumMinimumDistanceOptimal(stalls, cows):
    def canWePlace(distance):
        n = len(stalls)
        countCows = 1
        last = stalls[0]

        for i in range(n):
            if stalls[i]-last > distance:
                countCows += 1
                last = stalls[i]
            if countCows >= cows:   return True
        return False
    
    # Driver Code
    stalls.sort()
    low, high = 1, stalls[-1] - stalls[0]
    
    while low <= high:
        mid = low + (high-low)//2
        if canWePlace(mid):
            low = mid + 1
        else:
            high = mid - 1

    return low 

stalls = [0, 2, 4, 7, 10, 9]
cows = 4
print(maximumMinimumDistanceBruteForce(stalls, cows))
print(maximumMinimumDistanceOptimal(stalls, cows))