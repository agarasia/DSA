from collections import defaultdict, deque

def ladderLength(beginWord, endWord, wordList):
    if endWord not in wordList:
        return 0
    
    neighbors = defaultdict(list)
    wordList.append(beginWord)
    for word in wordList:
        for j in range(len(word)):
            pattern = word[:j] + "*" + word[j+1:]
            neighbors[pattern].append(word)
    
    visited = set([beginWord])
    queue = deque([beginWord])
    res = 1

    while queue:
        for _ in range(len(queue)):
            word = queue.popleft()
            if word == endWord:
                return res
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j+1:]
                for w in neighbors[pattern]:
                    if w not in visited:
                        visited.add(w)
                        queue.append(w)
        res += 1
    
    return 0
# T(n) = O(n * l)
# S(n) = O(n * l)

beginWord, endWord = "hit", "cog"
wordList = ["hot", "dot", "dog", "lot", "log", "cog"]

print(ladderLength(beginWord, endWord, wordList))