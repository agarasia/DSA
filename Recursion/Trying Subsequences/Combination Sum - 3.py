# Approach: Choose distinct numbers from 1 to 9 and if we reach
#           the target within the given length, append the subset.
def possibleCombination(target, length):
    def generate(ans, temp, target, length):
        if len(temp) == length:
            if target == 0:
                ans.append(temp[:])
        
        for i in range(1, 10):
            if i > target:
                break
            if temp and i <= temp[-1]:
                continue
            temp.append(i)
            generate(ans, temp, target - i, length)
            temp.pop()

    ans = []
    generate(ans, [], target, length)
    return ans
# T(n) = O(9^k), where k = given length

target, length = 9, 3

print(possibleCombination(target, length))