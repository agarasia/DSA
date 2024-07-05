# Approach: generate all substrings and check if the substring can
#           be transformed within K operations.
def characterReplacementBruteForce(st, k):
    def canTransform(substring):
        count = [0]*26
        for char in substring:
            count[ord(char) - ord('A')] += 1
        maxFreq = max(count)
        return len(substring) - maxFreq <= k
    
    maxLength = 0
    n = len(st)

    for i in range(n):
        for j in range(i, n):
            if canTransform(st[i:j+1]):
                maxLength = max(maxLength, j - i + 1)
    
    return maxLength
# T(n) = O(n**3)    n**2 for generating all substrings, n for checking
# S(n) = O(n)       for count


# Approach: Use sliding window to keep track of the longest 
#           possible substring
def characterReplacementOptimal(st, k):
    left = 0
    count = {}
    max_count = 0
    max_length = 0

    for right in range(len(st)):
        count[st[right]] = count.get(st[right], 0) + 1
        max_count = max(max_count, count[st[right]])

        while right - left + 1 - max_count > k:
            count[st[left]] -= 1
            left += 1

        max_length = max(max_length, right - left + 1)

    return max_length
# T(n) = O(n)   as we only traverse the string once
# S(n) = O(1)

st = "AABABBA"
k = 1

print(characterReplacementBruteForce(st, k))
print(characterReplacementOptimal(st, k))