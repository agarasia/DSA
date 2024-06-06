def beautySum(s):
    beautySum = 0

    for i in range(len(s)):
        hashMap = {}

        for j in range(i, len(s)):
            hashMap[s[j]] = hashMap.get(s[j], 0) + 1
            sortedHashMap = sorted(hashMap.items(), key = lambda x: x[1])

            if len(sortedHashMap) > 1:
                beautySum = beautySum + sortedHashMap[-1][1] - sortedHashMap[0][1]
    
    return beautySum


s = "aabcb"

print(beautySum(s))
print(beautySum("aabcbaa"))