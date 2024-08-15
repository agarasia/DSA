from collections import defaultdict, deque

def canFinish(numCourses, prerequisites):

    graph = defaultdict(list)
    for prereq, course in prerequisites:
        graph[course].append(prereq)

    indegree = [0] * numCourses
    for i in graph:
        for e in graph[i]:
            indegree[e] += 1

    q = deque()
    processedNodes = 0
    for i in range(numCourses):
        if indegree[i] == 0: 
            q.append(i)
    
    while q:
        node = q.popleft()
        processedNodes += 1

        for i in graph[node]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)
    
    if processedNodes != numCourses:
        return False
    else:
        return True
# T(n) = O(V + E)
# S(n) = O(V + E)

numCourses = 2
prerequisites = [[1,0], [0, 1]]
print(canFinish(numCourses, prerequisites))