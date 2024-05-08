# def func(a,target):         # Brute Force
#     ans = []
#     for i in range(len(a)):
#         for j in range(i+1, len(a)):
#             if a[i] + a[j] == target:
#                 ans.append(i)
#                 ans.append(j)
#     return ans

def func(a, target):        # Better 
    ans = []
    hash_map = {}
    
    for i in range(len(a)):
        hash_map[a[i]] = i
    
    for i in a:
        rem = target - i
        if rem in hash_map:
            ans.append(hash_map[i])
            ans.append(hash_map[rem])
    
    ans = set(ans)

    return list(ans)


a = [2,7,11,15]
target = 9
ans = func(a, target)
print(ans)