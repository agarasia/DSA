import math

# Approach: Remember high school prime factorization
def primeFactors(num):
    ans = []

    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            ans.append(i)
            while num % i == 0:
                num = num//i
    
    if num != 1:    ans.append(num)

    return ans
# T(n) = O(sqrt(n))     where n = num

num = 12
print(primeFactors(num))