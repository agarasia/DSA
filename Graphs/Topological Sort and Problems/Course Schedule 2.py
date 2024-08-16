from collections import defaultdict, deque

def findOrder(numCourses, prerequisite):
    graph = defaultdict(list)
    for prereq, course in prerequisite:
        graph[course].append(prereq)
    
    indegree = [0] * numCourses
    for i in range(numCourses):
        for e in graph[i]:
            indegree[e] += 1
    
    q = deque()
    for i in range(numCourses):
        if indegree[i] == 0:
            q.append(i)
    
    ans = []
    processedNodes = 0
    while q:
        node = q.popleft()
        processedNodes += 1
        ans.append(node)

        for i in graph[node]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)
    
    return ans if processedNodes == numCourses else []
# T(n) = O(V + E)
# S(n) = O(V)

numCourses = 4
prerequisites = [[1,0],[2,0],[3,1],[3,2]]
print(findOrder(numCourses, prerequisites))