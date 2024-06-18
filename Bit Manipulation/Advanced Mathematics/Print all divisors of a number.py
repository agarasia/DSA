def allDivisors(num):
    ans = []

    for i in range(1, num//2 + 1):
        if num % i == 0:
            ans.append(i)
    
    ans.append(num)

    return ans

num = 60

print(allDivisors(num))
print(allDivisors(21191))