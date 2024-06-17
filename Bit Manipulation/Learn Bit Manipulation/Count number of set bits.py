def setBits(n):
    n += 1
    count = 0
    
    x = 2
    
    while x//2 < n:
        q = n // x
        count += (q * x // 2)
        remainder = n % x
        if remainder > x//2:
            count += remainder - x//2
        x *= 2
    
    return count

num = 4

print(setBits(num))