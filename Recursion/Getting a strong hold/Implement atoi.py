def myAtoI(s):
    def calc(st, sign, num, ind):
        if sign * num >= 2**31 - 1:
            return 2**31 - 1
        if sign * num <= -2**31:
            return -2**31
        
        if ind == len(st) or (ord(st[ind]) - ord('0')) < 0 or (ord(st[ind]) - ord('0')) > 9:
            return sign * num
        
        num = calc(st, sign, num*10 + (ord(st[ind]) - ord('0')), ind + 1)

        return num
    
    s = s.strip()

    if s[0] == '-':
        s = s[1:]
        return calc(s, -1, 0, 0)
    elif s[0] == '+':
        s = s[1:]
        return calc(s, 1, 0, 0)



s = "   -042"
print(myAtoI(s))