def minTimeToSchedule(tasks, n):
    def heapify(heap, index):
        max_index = index
        left, right = 2*index+1, 2*index+2

        if left < len(heap) and heap[max_index] < heap[left]:
            max_index = left
        
        if right < len(heap) and heap[max_index] < heap[right]:
            max_index = right
        
        if max_index != index:
            heap[index], heap[max_index] = heap[max_index], heap[index]
            heapify(heap, max_index)
    
    def insert(heap, key):
        heap.append(key)
        index = len(heap) - 1
        while index and heap[index] > heap[(index-1)//2]:
            heap[index], heap[(index-1)//2] = heap[(index-1)//2], heap[index]
            index = (index-1)//2
    
    def extractMax(heap):
        if len(heap) == 1:
            return heap.pop()
        result = heap[0]
        heap[0] = heap.pop()
        heapify(heap, 0)
        return result
    
    # Main program
    freqMap = [0]*26
    for i in tasks:
        freqMap[ord(i) - ord("A")] += 1
    
    maxHeap = []
    for freq in freqMap:
        if freq > 0:
            insert(maxHeap, freq)
    
    time, cooldown = 0, []

    while maxHeap or cooldown:
            time += 1

            if maxHeap:
                freq = extractMax(maxHeap)
                freq -= 1
                if freq > 0:
                    cooldown.append((freq, time + n))

            if cooldown and cooldown[0][1] == time:
                task = cooldown.pop(0)
                insert(maxHeap, task[0])

    return time
# T(n) = O(n)
# S(n) = O(26) == O(1)
        


tasks = ["A", "A", "A", "B", "B", "B"]
n = 3

print(minTimeToSchedule(tasks, n))