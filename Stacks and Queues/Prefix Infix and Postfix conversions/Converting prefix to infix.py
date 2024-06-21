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

expr = "*-A/BC-/AKL"

print(convertToInfix(expr))