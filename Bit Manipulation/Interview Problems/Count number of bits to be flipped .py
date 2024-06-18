def bitsToFlip(start, target):
    count = 0
    while start > 0 or target > 0:
        if start&1 != target&1:
            count += 1
        start >>= 1
        target >>= 1
    
    return count


start, target = 10, 7

print(bitsToFlip(start, target))
print(bitsToFlip(3, 4))