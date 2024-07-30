from collections import deque


def floodFill(image, sr, sc, color):
    if image[sr][sc] == color:
        return image

    queue = deque([(sr, sc)])
    sColor = image[sr][sc]
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    image[sr][sc] = color

    while queue:
        r, c = queue.popleft()

        for dr, dc in directions:
            row, col = r + dr, c + dc

            if 0 <= row < len(image) and 0 <= col < len(image[0]) and image[row][col] == sColor:
                image[row][col] = color
                queue.append((row, col))

    return image
# T(n) = O(n * m)
# S(n) = O(n * m)

image = [[1, 1, 1],
         [1, 1, 0],
         [1, 0, 1]]
sr, sc = 1, 1
color = 2
print(floodFill(image, sr, sc, color))