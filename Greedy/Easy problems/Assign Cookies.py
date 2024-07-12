def findContentChildrenBruteForce(g, s):
    ans = 0

    for i in range(len(g)):
        for j in range(len(s)):
            if i < len(g) and j < len(s) and s[j] >= g[i]:
                ans += 1
                s.pop(j)
                break
    
    return ans
# T(n) = O(n**2)
# S(n) = O(1)

def findContentChildren(g, s):
    g.sort()
    s.sort()
    
    # Initialize pointers for greed factors (g) and cookies (s)
    i = 0
    j = 0
    ans = 0
    
    # Loop through both lists
    while i < len(g) and j < len(s):
        # If the current cookie can satisfy the current child
        if s[j] >= g[i]:
            ans += 1
            i += 1
        # Move to the next cookie
        j += 1
    
    return ans
# T(n) = O(n * log n)
# S(n) = O(1)

g = [1, 2, 3]
s = [1, 1]

print(findContentChildrenBruteForce(g, s))
print(findContentChildren(g, s))