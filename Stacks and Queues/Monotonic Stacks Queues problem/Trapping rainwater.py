# Approach: Find the maximum amount of water that can be collected
#           at each index.
def waterTrappedBruteForce(heights):
    n = len(heights)
    waterTrapped = 0
    lMax, rMax = 0, 0

    for i in range(n):
        j = i
        while j >= 0:
            lMax = max(lMax, heights[j])
            j -= 1
        
        j = i
        while j < n:
            rMax = max(rMax, heights[j])
            j += 1
        
        waterTrapped += min(lMax, rMax) - heights[i]
    
    return waterTrapped
# T(n) = O(n**2), S(n) = O(1)

def waterTrapped(heights):
    n = len(heights)
    prefix, suffix = [0]*n, [0]*n
    prefix[0] = heights[0]
    suffix[n-1] = heights[n-1]
    waterTrapped = 0

    for i in range(1, n):
        prefix[i] = max(prefix[i-1], heights[i])
    
    for j in range(n-2, -1, -1):
        suffix[j] = max(suffix[j+1], heights[j])
    
    for k in range(0, n):
        waterTrapped += (min(prefix[k], suffix[k]) - heights[k])

    return waterTrapped
# T(n) = O(3*n), S(n) = O(2*n) 

heights = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]

print(waterTrapped(heights))