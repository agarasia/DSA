def isPowerOf2(num):
    if num <= 0:
        return False
    if num == 1:
        return True
    if num % 2: 
        return False
    return isPowerOf2(num//2)

num = 16
print(isPowerOf2(num))