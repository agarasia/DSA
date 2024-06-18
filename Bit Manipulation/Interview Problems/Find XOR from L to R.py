# Approach: observations for xor upto n
#           reveal an easier way to compute
def xorOptimal(l, r):
    def xor_upto(n):
        if n % 4 == 0:
            return n
        elif n % 4 == 1:
            return 1
        elif n % 4 == 2:
            return n + 1
        else:
            return 0
    
    return xor_upto(r) ^ xor_upto(l - 1)
# T(n) = O(1)

# Approach: Use a for loop and do XOR
#           operation. Return the resultant
#           value.
def xorBruteForce(l, r):
    for i in range(l, r+1):
        l ^= i
    
    return i
# T(n) = O(n)   where n = difference between l and r.

l, r = 4, 8

print(xorBruteForce(l, r))
print(xorOptimal(l, r))