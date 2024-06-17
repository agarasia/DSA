def swap(a, b):
    a = a^b
    b = b^a
    a = b^a

    return a, b

a, b = 9, 13

print(swap(a,b))