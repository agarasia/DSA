def numOfUndirectedGraphs(n):
    return 2**((n*(n-1))//2)

print(numOfUndirectedGraphs(5))