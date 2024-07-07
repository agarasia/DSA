# Approach: Expand and contract the sliding window keeping
#           track of the characters we have in the map and
#           the characters we need from string t.
def minimumWindowSubstring(s, t):
    if t == "": return ""

    left = 0
    resLen = float('inf')
    res = [-1, -1]
    window, countT = {}, {}

    for c in t:
        countT[c] = countT.get(c, 0) + 1
    
    have, need = 0, len(countT)

    for right in range(len(s)):
        char = s[right]
        window[char] = window.get(char, 0) + 1

        if char in countT and window[char] == countT[char]:
            have += 1
        
        while have == need:
            # Update our result
            if (right - left + 1) < resLen:
                res = [left, right]
                resLen = right - left + 1
            
            # Pop from the left of our window
            charB = s[left]
            window[charB] -= 1
            if charB in countT and window[charB] < countT[charB]:
                have -= 1
            
            left += 1
    
    left, right = res
    if resLen != float('inf'):
        return s[left : right + 1]
    else:
        return ""
# T(n) = O(n)
# S(n) = O(n)

s = "adobecodebanc"
t = "abc"

print(minimumWindowSubstring(s, t))