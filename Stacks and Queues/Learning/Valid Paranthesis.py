# Approach: As and when the paranthesis open, keep their
#           track using a stack. If there are violations of
#           valid parantheses, return False, else return True.
def isValidOptimal(s):
    mapping = { ')':'(', '}':'{', ']':'['}
    stack = []

    for i in s:
        if i == '(' or i == '{' or i == '[':
            stack.append(i)
        if i == ')' or i == ']' or i == '}':
            if stack and mapping[i] == stack[-1]:
                stack.pop()
            else:
                return False
    
    if not stack:   return True
    return False
# T(n) = O(n)   where n = length of string
# S(n) = O(n)   for the stack

s = "({{{{}}}))"
print(s)
print(isValidOptimal(s))