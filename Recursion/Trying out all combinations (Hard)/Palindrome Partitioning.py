# Approach: Generate all palindrome partitions 
def possibleSubstrings(s):
    def isPalindrome(s, ind1, ind2):
        while ind1 < ind2:
            if s[ind1] != s[ind2]:
                return False
            ind1 += 1
            ind2 -= 2
        return True

    def generate(ans, temp, ind, st):
        if ind == len(st):
            ans.append(temp[:])
            return
        
        for i in range(ind, len(st)):
            if isPalindrome(st, ind, i):
                temp.append(st[ind: i+1])
                generate(ans, temp, i + 1, st)
                temp.pop()

    if not s:
        return []
    ans = []
    temp = []
    generate(ans, temp, 0, s)
    return ans

inputString = "aab"

print(possibleSubstrings(inputString))