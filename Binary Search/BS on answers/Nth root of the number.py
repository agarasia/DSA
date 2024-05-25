# Approach: Use Linear search to find the Nth root
def nthRootBruteForce(num, power):
    for i in range(1, num+1):
        val = i**power
        if val == num:
            return i
        if val > num:   break

    return -1
# T(n) = O(n)

# Approach: Use Binary Search to find the Nth root
def nthRootOptimal(num, power):
    low, high = 1, num
    while low <= high:
        mid = low + (high-low)//2
        val = mid ** power
        if val == num:  return mid
        if val < num:
            low = mid + 1
        else:
            high = mid - 1
    
    return -1
# T(n) = O(log n)

num = 512
power = 3

print(nthRootBruteForce(num, power), nthRootOptimal(num, power))