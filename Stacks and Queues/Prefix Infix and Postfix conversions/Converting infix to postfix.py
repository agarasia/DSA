def convertToPostfix(expr):
    # Helper function to find out the order od precedence
    def precedence(operator):
        if operator == '^':
            return 3
        elif operator == '*' or operator == '/':
            return 2
        elif operator == '+' or operator == '-':
            return 1
        else:
            return 0
    
    res = ""
    stack = []

    for i in expr:
        if i == "(":
            stack.append(i)
        
        # If valid operand, print the charactor
        elif i.isalnum():
            res += i
        
        elif (i == ")"):
        # Empty the stack until we encounter (
            while stack[-1] != "(":
                res += stack.pop()
            stack.pop()

        else:
            while (stack and precedence(i) <= precedence(stack[-1])):
                res += stack.pop()
            stack.append(i)

    while stack:
        res += stack.pop()

    return res        


# Infix expression
expr = "(A+B)*(C-D)"

print(convertToPostfix(expr))