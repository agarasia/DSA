def validParanthesis(s):
    open_count, close_count = 0, 0

    for i in range(len(s)):
        if s[i] == "(" or s[i] == "*":
            open_count += 1
        else:
            open_count -= 1
        
        if s[len(s) - i - 1] == ")" or s[len(s) - i -1] == "*":
            close_count += 1
        else:
            close_count -= 1
        
        if open_count < 0 or close_count < 0:
            return False
    
    return True
# T(n) = O(n)
# S(n) = O(1)

s = "(*))"

print(validParanthesis(s))