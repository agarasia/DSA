def largestMinDistance(boards, painters):
    def paintersNeeded(time):
        n = len(boards)
        numPainters = 1
        timeTaken = 0

        for i in range(n):
            if timeTaken + boards[i] <= time:
                timeTaken += boards[i]
            else:
                numPainters += 1
                timeTaken = boards[i]
        
        return numPainters
    
    maxTime = max(boards)
    maxTotalTime = sum(boards)

    for time in range(maxTime, maxTotalTime+1):
        if paintersNeeded(time) == painters:
            return time
    
    return maxTime

def largestMinDistanceOptimal(boards, painters):
    def paintersNeeded(time):
        n = len(boards)
        numPainters = 1
        timeTaken = 0

        for i in range(n):
            if timeTaken + boards[i] <= time:
                timeTaken += boards[i]
            else:
                numPainters += 1
                timeTaken = boards[i]
        
        return numPainters
    
    low = max(boards)
    high = sum(boards)

    while low <= high:
        mid = low + (high - low)//2
        numPainters = paintersNeeded(mid)
        if numPainters > painters:
            low = mid + 1
        else:
            high = mid - 1
        
    return low

boards = [10, 20, 30, 40]
painters = 2

print(largestMinDistance(boards, painters))
print(largestMinDistanceOptimal(boards, painters))