def power(num, pow):
    if pow == 0:
        return 1
    if pow == -1:
        return 1/num
    if pow == 1:
        return num

    return power(num * num, pow//2) * power(num, pow % 2)

print(power(2.1, 3))
    