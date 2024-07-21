def isValid(inorder):
    for i in range(len(1, inorder)):
        if inorder[i] <= inorder[i-1]:
            return False
    
    return True
# T(n) = O(n)
# S(n) = O(1)

inorder = [8, 14, 45, 64, 100]
print(isValid(inorder))