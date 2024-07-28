def numberOfProvinces(isConnected):
    visited = set()
    provinces = 0

    def dfs(vertex):
        visited.add(vertex)
        for i in range(len(isConnected)):
            if i not in visited and isConnected[vertex][i]:
                dfs(i)
    
    for i in range(len(isConnected)):
        if i not in visited:
            dfs(i)
            provinces += 1

    return provinces
# T(n) = O(n ** 2)

isConnected = [[1, 1, 0],
               [1, 1, 0],
               [0, 0, 1]]
print(numberOfProvinces(isConnected))