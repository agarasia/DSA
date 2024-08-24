from collections import deque

def minimumMultiplications(start, end, arr):
    if start == end:
            return 0
    q = deque([(start, 0)])
    visited = set([start])
    mod = 100000

    while q:
        current, steps = q.popleft()
        
        for num in arr:
            new_value = (current * num) % mod
            
            if new_value == end:
                return steps + 1
            
            if new_value not in visited:
                visited.add(new_value)
                q.append((new_value, steps + 1))
    
    return -1




arr = [3, 4, 65]
start, end = 7, 66175
print(minimumMultiplications(start, end, arr))