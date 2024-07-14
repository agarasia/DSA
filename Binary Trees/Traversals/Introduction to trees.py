# Given a level of a binary tree, return the maximum number of nodes
def countNodes(i):
    return 2**(i-1)
# T(n) = O(1)

print(countNodes(2))