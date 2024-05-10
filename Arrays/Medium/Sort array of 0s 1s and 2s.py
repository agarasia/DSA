# Naive approach
def Sort(arr):
    arr = sorted(arr)
    return arr

# Better Approach
def SortBetter(arr):
    c_0, c_1, c_2 = 0, 0, 0
    for i in arr:
        if i == 0:  c_0 += 1
        elif i == 1:    c_1 += 1
        else:       c_2 += 1
    
    ans = []
    for i in range(c_0):
        ans.append(0)

    for i in range(c_1):
        ans.append(1)

    for i in range(c_2):
        ans.append(2)
    
    return ans

# Optimal Approach
def SortOptimal(arr):
    start, mid = 0, 0
    end = len(arr) - 1

    while mid <= end:
        if arr[mid] == 0:
            arr[start], a[mid] = arr[mid], arr[start]
            start += 1
            mid += 1
        
        elif arr[mid] == 1:
            mid += 1
        
        else:
            arr[end], arr[mid] = arr[mid], arr[end]
            end -= 1
    
    return arr

a = [1,2,1,1,1,0,2,0]
print(Sort(a), "\n", SortBetter(a), "\n", SortOptimal(a))