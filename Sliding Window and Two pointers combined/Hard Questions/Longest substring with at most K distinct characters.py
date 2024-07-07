# Approach: Employ a sliding window to expand and contract
#           based on the number of distinct characters.
def longestSubstring(s, k):
    if k == 0 or not s:
        return ""
    
    charCount = {}
    left = 0
    maxLength = 0

    for right in range(len(s)):
        charCount[s[right]] = charCount.get(s[right], 0) + 1

        if len(charCount) > k:
            charCount[s[left]] -= 1
            if charCount[s[left]] == 0:
                del charCount[s[left]]
            left += 1
        
        maxLength = max(maxLength, right - left + 1)
    
    return maxLength
# T(n) = O(n)
# S(n) = O(n)

s = "aaabc"
k = 3

print(longestSubstring(s, k))