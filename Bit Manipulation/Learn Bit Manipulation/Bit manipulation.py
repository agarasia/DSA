# Return following:
# 1. the ith bit
# 2. set the ith bit
# 3. unset the ith bit
def bitManipulation(num, i):
    ans = []

    # Finding the ith bit
    ith = num
    ith = (ith >> (i-1)) & 1
    ans.append(ith)

    # Number after Setting the ith bit
    if ith:
        ans.append(num)
    else:
        ans.append(num + pow(2, i-1))
    
    # Unsetting the ith bit
    if ans[-1] == num:
        ans.append(num - pow(2, i - 1))
    else:
        ans.append(num)

    return ans
    

num = 70
i = 3
print(bitManipulation(num, i))