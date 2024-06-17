def setThatBit(N):
    temp = N
    c = 0
    
    while temp and temp&1 == 1:
        temp = temp >> 1
        c += 1
    
    N += 2**c
    
    return N

n = 7

print(setThatBit(n))