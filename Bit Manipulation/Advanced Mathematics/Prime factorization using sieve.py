from math import sqrt

def primeFactorization(num):
    isPrime = [True]*num
    isPrime[0] = isPrime[1] = False

    for i in range(2, int(sqrt(num))+1):
        if num%i == 0:
            for j in range(i*i, num, i):
                isPrime[j] = False
    
    ans = []
    for i in range(num):
        if isPrime[i] and num%i == 0:
            ans.append(i)

    return ans

num = 35
print(primeFactorization(num))