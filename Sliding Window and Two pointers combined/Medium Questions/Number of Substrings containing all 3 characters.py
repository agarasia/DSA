# Approach: Generate all substrings and check if 
#           the substring is valid or not.
def numberOfSubstringsBruteForce(s):
    ans = 0
    
    for i in range(len(s)):
        st = set()
        for j in range(i, len(s)):
            st.add(s[j])

            if len(st) == 3:
                ans += 1
    
    return ans
# T(n) = O(n**2)
# S(n) = O(1)

# Approach: Use sliding window to find each possible 
#           and valid substring
def numberOfSubstringsOptimal(s):
    ans = 0
    left = 0
    char = [0] * 3

    for right in range(len(s)):
        char[ord(s[right]) - ord("a")] += 1

        while all(char):
            ans += len(s) - right
            char[ord(s[left]) - ord("a")] -= 1
            left += 1
    
    return ans
# T(n) = O(n)
# S(n) = O(1)

s = "aaacb"
print(numberOfSubstringsBruteForce(s))
print(numberOfSubstringsOptimal(s))