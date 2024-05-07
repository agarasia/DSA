def max1s(arr):
    count = 0
    max_count = 0
    for i in arr:
        if i == 1:
            count += 1
            max_count = max(max_count, count)
        else:
            max_count = max(max_count, count)
            count = 0
        # print("Count: ", count, ", Max Count: ", max_count)

    return max_count

arr = [1, 1, 0, 1, 1, 1]
arr2 = [1,0,1,1,0,1]
print(max1s(arr2))

