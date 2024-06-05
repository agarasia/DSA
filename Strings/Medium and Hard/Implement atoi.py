# Approach: Strip the string of spaces and then calculate
#           the value according to the flag.
def myAToI(s:str):
    s = s.strip()
    if not s or len(s) == 0:
        return 0
    
    neg = False
    if s[0] == '-':
        neg = True
        s = s[1:]
    elif s[0] == '+':
        s = s[1:]

    numValue = 0
    for i in s:
        val = ord(i) - ord('0')
        if val < 0 or val > 9:
            break
        else:
            numValue = numValue*10 + val
    
    if numValue > 2**31 - 1:
        if neg: return -2**31
        else:   return 2**31 - 1
    
    return numValue if not neg else -numValue
# T(n) = O(n)   where n = length of the string

s = "  -0420"

print(myAToI(s))