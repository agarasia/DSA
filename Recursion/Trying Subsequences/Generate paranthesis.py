def generateParanthesis(n):
    def generator(ans, s, open, closed, n):
        if open > n or closed > open or len(s) > 2*n:
            return
        if open == n and closed == n and len(s) == 2*n:
            ans.append(s)
        
        generator(ans, s+"(", open+1, closed, n)
        generator(ans, s+")", open, closed+1, n)

    ans = []
    generator(ans, "", 0, 0, n)
    return ans

print(generateParanthesis(1))