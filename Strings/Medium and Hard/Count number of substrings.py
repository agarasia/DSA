def numOfSubstrings(s, k):
    def kDistinctCharacters(k1):
        left = 0
        count = 0
        hashMap = {}

        for right in range(len(s)):
            hashMap[s[right]] = hashMap.get(s[right], 0) + 1

            while len(hashMap) > k1:
                hashMap[s[left]] -= 1
                if hashMap[s[left]] == 0:
                    del hashMap[s[left]]
                left += 1
            
            count += (right - left + 1)
        
        return count

    return kDistinctCharacters(k) - kDistinctCharacters(k-1)

s = "aba"
distinctCharacters = 2

print(numOfSubstrings(s, distinctCharacters))