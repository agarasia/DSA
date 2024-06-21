def convertToPostFix(expr):
    # Convert prefix expr to infix expr
    def convertToInfix(expr):
        expr = expr[::-1]   # Converting prefix to postfix expr

        stack = []
        for i in expr:
            if i.isalnum():
                stack.append(i)

            elif i == "+" or i=="-" or i=="*" or i=="/":
                operand1 = stack.pop()
                operand2 = stack.pop()
                newExpr = "("+operand1+i+operand2+")"
                stack.append(newExpr)
        
        return stack[0]
    
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
    
    return convertToPostfix(convertToInfix(expr))

expr = "*-A/BC-/AKL"

print(convertToPostFix(expr))