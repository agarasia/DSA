# Approach: All rotations of a string A are
#           enclosed in string A+A. The goal string
#           also should lie in A+A.
def rotateString(str1, str2):
    return len(str1) == len(str2) and str2 in str1+str1

str1 = "abcde"
str2 = "cdeab"
print(rotateString(str1, str2))