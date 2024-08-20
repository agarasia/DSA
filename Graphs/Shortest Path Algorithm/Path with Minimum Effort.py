from heapq import heappop, heappush

def minimumEffortPath(heights):
    rows, cols = len(heights), len(heights[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    # Min-heap to store the minimum effort at the current position
    min_heap = [(0, 0, 0)]  # (effort, row, col)
    efforts = [[float('inf')] * cols for _ in range(rows)]
    efforts[0][0] = 0
    
    while min_heap:
        current_effort, r, c = heappop(min_heap)
        
        # If we reach the bottom-right cell
        if r == rows - 1 and c == cols - 1:
            return current_effort
        
        # Explore all neighbors
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            
            if 0 <= nr < rows and 0 <= nc < cols:
                # Calculate the effort to the neighboring cell
                next_effort = max(current_effort, abs(heights[nr][nc] - heights[r][c]))
                
                # If this path offers a smaller effort, update and push to heap
                if next_effort < efforts[nr][nc]:
                    efforts[nr][nc] = next_effort
                    heappush(min_heap, (next_effort, nr, nc))
    
    return 0



heights = [[1,2,2],[3,8,2],[5,3,5]]
print(minimumEffortPath(heights))