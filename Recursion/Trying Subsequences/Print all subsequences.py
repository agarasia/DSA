def powerSet(s):
    def generateSet(ans, temp, s, ind):
        if ind == len(s):
            ans.append(temp[:])
            return
        
        temp.append(s[ind])
        generateSet(ans, temp, s, ind+1)
        temp.pop()
        generateSet(ans, temp, s, ind+1)
    
    if not s:
        return []
    ans = []

    generateSet(ans, [], s, 0)
    return ans


Set = [1, 2]
print(powerSet(Set))