def isBitSet(num, i):
    while i:
        num = num >> 1
        i -= 1
    
    return True if num&1 else False

num, i = 4, 0
print(isBitSet(num, i))