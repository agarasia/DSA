# Approach: create a hashmap, sort it in decreasing order
#           and create the answer string.
def frequencySort(s):
    hashMap = {}
    ans = ""

    for i in s:
        if i not in hashMap:
            hashMap[i] = 1
        else:
            hashMap[i] += 1
    
    sortedFrequencyMap = sorted(hashMap.items(), key = lambda x: x[1], reverse = True)

    for char, freq in sortedFrequencyMap:
        ans += (char * freq)
    
    return ans
# T(n) = O(n logn)
# S(n) = O(n)   for storing the hash map

s = "cccAaa"

print(frequencySort(s))