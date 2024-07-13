def numOfPlatforms(arr, dep):
    n = len(arr)
    order = []
        
    for i in range(n):
        order.append([arr[i], 'a'])
        order.append([dep[i], 'd'])
    
    order.sort(key = lambda x: x[1])
    order.sort()
    result = 1
    platforms = 0
    
    for i in order:
        if i[1] == 'a':
            platforms += 1
        else:
            platforms -= 1
        
        result = max(result, platforms)
    
    return result
# T(n) = O(n * log n)
# S(n) = O(n)

arr = [900, 940, 950, 1100, 1500, 1800]
dep = [910, 1200, 1120, 1130, 1900, 2000]

print(numOfPlatforms(arr, dep))