def canWeColor(graph, m, vertices):

    def isSafe(node, colors, col):
        for k in range(len(colors)):
            if k != node and graph[k][node] == 1 and colors[k] == col:
                return False
        return True

    def solve(colors, vertex):
        if vertex == len(colors):
            return True
        
        for i in range(1, m+1):
            if isSafe(vertex, colors, i):
                colors[vertex] = i
                if solve(colors, vertex + 1):
                    return True
                colors[vertex] = 0
        
        return False

    colors = [0]*vertices
    return solve(colors, 0)

graph = [[0]*101 for _ in range(101)]

graph[0][1] = 1
graph[1][2] = 1
graph[2][3] = 1
graph[3][0] = 1
graph[0][2] = 1

nodes = 4
print(canWeColor(graph, 3, 4))