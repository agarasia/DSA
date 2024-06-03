# Approach: Map each character from str1 to str2 and vice versa
#           and check for conflicting mappings in the strings.
def isIsomorphic(str1, str2):
    if len(str1) != len(str2):
        return False
    
    str1_str2 = {}
    str2_str1 = {}

    for i in range(len(str1)):
        if str1[i] in str1_str2:
            if str1_str2[str1[i]] != str2[i]:
                return False
        if str2[i] in str2_str1:
            if str2_str1[str2[i]] != str1[i]:
                return False
        
        str1_str2[str1[i]] = str2[i]
        str1_str2[str2[i]] = str1[i]
    
    return True
# T(n) = O(n)   where n = length of string
# S(n) = O(n)   for storing the mapping

str1, str2 = "egg", "add"

print(isIsomorphic(str1, str2))