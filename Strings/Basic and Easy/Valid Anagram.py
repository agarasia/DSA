def validAnagram(s, t):
    if len(s) != len(t):
        return False
    
    freq = [0]*26

    for i in s:
        freq[ord(i)-ord('a')] += 1
    
    for j in t:
        freq[ord(j)-ord('a')] -= 1
    
    for i in range(26):
        if freq[i] == 0:    continue
        else: return False
    
    return True

s, t = "racecar", "carrace"

print(validAnagram(s, t))