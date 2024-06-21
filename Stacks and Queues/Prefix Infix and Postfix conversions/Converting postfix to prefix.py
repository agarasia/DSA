def convertToPostfix(expr):
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

expr = "AB-CD+*"
print(convertToPostfix(expr))