def convertToInfix(expr):
    def convertToPrefix(expr):
        def isOperator(x):
            return x in '+-*/'
        
        stack = []

        for i in expr:
            if i.isalnum():
                stack.append(i)
            if isOperator(i):
                op1 = stack.pop()
                op2 = stack.pop()
                temp = i + op2 + op1
                stack.append(temp)
        
        return stack.pop()
    
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
    
    return convertToInfix(convertToPrefix(expr))

postfix_expr = "AB+CD-*"

print(convertToInfix(postfix_expr))