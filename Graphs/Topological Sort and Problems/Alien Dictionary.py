from collections import defaultdict, deque

def findOrder(word, N, K):
    graph = defaultdict(list)
    indegree = {chr(i + ord('a')): 0 for i in range(K)}

    for i in range(N - 1):
        w1, w2 = word[i], word[i+1]
        l = min(len(w1), len(w2))
        for j in range(l):
            if w1[j] != w2[j]:
                graph[w1[j]].append(w2[j])
                indegree[w2[j]] += 1
                break
    
    q = deque([c for c in indegree if indegree[c] == 0])
    
    ans = []
    while q:
        n = q.popleft()
        ans.append(n)

        for e in graph[n]:
            indegree[e] -= 1
            if indegree[e] == 0:
                q.append(e)
    
    if len(ans) == K:
        return "".join(ans)
    else:
        return ""
# T(n) = O(N * |S| + K)
# S(n) = O(K) 

alienDict = ["baa","abcd","abca","cab","cad"]
N, K = 5, 4
print(findOrder(alienDict, N, K))