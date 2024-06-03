# Approach: keep track of how many times the
#           paranthesis opens and closes. If
#           more than one openings, concatenate to
#           the answer string.
def removeOutermostParenthesis(s):
    ans = ""
    open = 0

    for i in s:
        if i == '(':
            open += 1
        if i == ')':
            open -= 1
        if i == '(' and open > 1:
            ans += '('
        if i == ')' and open > 0:
            ans += ')'

    return ans
# T(n) = O(len(string))

s = "(()())(())(()(()))"

print(removeOutermostParenthesis(s))