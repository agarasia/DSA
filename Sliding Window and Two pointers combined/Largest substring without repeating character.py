# Approach: Employ a set and check for each possible
#           substring if it has all distinct characters.
def longestSubstringBruteForce(s):
    ans = 0

    for i in range(len(s)):
        chars = set()
        for j in range(i, len(s)):
            chars.add(s[j])
            if len(chars) == j-i+1:
                ans = max(ans, j-i+1)
    
    return ans
# T(n)= O(n**2)
# S(n)= O(n)

# Approach: Emply a set and two pointers to keep track
#           of repeating characters.
def longestSubstringOptimal(s):
    if len(s) == 0: return 0

    ans = float('-inf')
    Set = set()
    l = 0

    for r in range(len(s)):
        if s[r] in Set:
            while l < r and s[r] in Set:
                Set.remove(s[l])
                l += 1
        Set.add(s[r])
        ans = max(ans, r-l+1)
    
    return ans
# T(n) = O(2*n) for a string with all but one character duplicate, say "abcdeff"
#               l would have to jump to the last character
# S(n) = O(n)   because of the set


s = "abcabcbb"
print(longestSubstringBruteForce(s))
print(longestSubstringOptimal(s))