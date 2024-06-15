def generateBinaryStrings(n):
    def generateStrings(temp, ans, k, n):
        if k == n:
            ans.append(temp)
            return
        
        generateStrings(temp + "0", ans, k+1, n)
        generateStrings(temp + "1", ans, k+1, n)
    
    if n == 0:
        return []
    ans = []
    generateStrings("", ans, 0, n)
    return ans


print(generateBinaryStrings(3))