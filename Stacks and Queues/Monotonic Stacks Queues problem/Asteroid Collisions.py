# Approach: A collision can only happen if while traversing the array
#           we see an asteroid moving in left and other moving on the right.
#           Because of this, we can use a stack data structure.
def afterCollisions(asteroids):
    stack = []
    for a in asteroids:
        while stack and a < 0 and stack[-1] > 0:
            diff = a + stack[-1]
            if diff > 0:
                a = 0
            if diff < 0:
                stack.pop()
            if diff == 0:
                stack.pop()
                a = 0
        if a:
            stack.append(a)
    
    return stack
# T(n) = O(n)   where n = length of the array

asteroids = [-1, 3, 2, -3]

print(afterCollisions(asteroids))