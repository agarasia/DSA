# Approach: Sliding window 
def maxPoints(cardPoints, k):
    points = 0
    ans = 0

    for i in range(k):
        points += cardPoints[i]
    
    k -= 1
    i = len(cardPoints) - 1

    while k >= 0:
        points = points - cardPoints[k] + cardPoints[i]
        k -= 1
        i -= 1
        ans = max(ans, points)
    
    return ans
# T(n) = O(n)
# S(n) = O(1)

cardPoints = [1, 2, 3, 4, 5, 6, 1]
k = 3

print(maxPoints(cardPoints, k))