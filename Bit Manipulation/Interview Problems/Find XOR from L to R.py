def xorBruteForce(l, r):
    for i in range(l, r+1):
        l ^= i
    
    return i

l, r = 4, 8

print(xorBruteForce(l, r))