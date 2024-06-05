# Approach: For various lengths, try expanding and check
#           whether the substring is palindrome or not. 
def longestPalindrome(s):
    # Helper function: expand from center and return the
    #                  length of longest palindrome substring.
    def expand(i, j):
        left, right = i, j
        while left >= 0 and right < n and s[left] == s[right]:
            left -= 1
            right += 1
        
        return right - left + 1

    n =  len(s)
    ans = [0, 0]

    for i in range(n):
        odd_length = expand(i, i)
        if odd_length > ans[1] - ans[0] + 1:
            dist = odd_length // 2
            ans = [i-dist, i+dist]
        
        even_length = expand(i, i+1)
        if even_length > ans[1] - ans[0] + 1:
            dist = (even_length // 2) - 1
            ans = [i-dist, i+dist+1]
    
    i, j = ans
    return s[i : j+1]
# T(n) = O(n ** 2)

s = "babad"
print(longestPalindrome(s))