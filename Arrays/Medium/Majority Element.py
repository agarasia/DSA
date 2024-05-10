# Naive approach
def majorityNaive(arr):
    arr = sorted(arr)
    return arr[len(arr)//2]

# Better Approach
def majorityBetter(arr):
    hash_map = {}
    for i in arr:
        if i not in hash_map:   hash_map[i] = 1
        if i in hash_map:       hash_map[i] += 1
    
    for i in hash_map:
        if hash_map[i] >= len(arr)//2:   return i

# Optimal Approach : Moore's voting algorithm
def majorityOptimal(arr):
    element = None
    count = 0

    for current_element in arr:
        if count == 0 :
            count = 1
            element = current_element
        elif current_element != element:
            count -= 1
        else:
            count += 1
    
    count_element = 0
    for i in arr:
        if i == element:    count_element += 1
    
    return element if count_element > len(arr) // 2 else -1

a = [3, 2, 3]
print(majorityNaive(a), majorityBetter(a), majorityOptimal(a))