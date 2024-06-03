# Approach: Vertical scanning each character for each
#           string.
def longestCommonPrefix(strs):
    if not strs or len(strs) == 0:
        return ""
    
    for i in range(len(strs[0])):
        char = strs[0][i]

        for j in range(1, len(strs)):
            if i == len(strs[j]) or strs[j][i] != char:
                return strs[0][:i]
    
    return strs[0]
# T(n) = O(S) where S = sum of all characters in strs

strs = ["flower", "flow", "flight"]

print("\""+longestCommonPrefix(strs)+"\"")