# Approach: For the largest 'odd' number,
#           we only need to check the last number!
def largestOddNumber(s):
    n = len(s)

    for i in range(n-1, -1, -1):
        if (ord(s[i]) - 48) % 2:
            return s[:i+1] 

    return ""
# T(n) = O(n)   where n = length of string


s = "34826"

print(largestOddNumber(s))