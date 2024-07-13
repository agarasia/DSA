def avgWaitingTime(burstTime):
    burstTime.sort()
    ct = []
    for i in burstTime:
        ct.append(i)
    
    for i in range(1, len(burstTime)):
        ct[i] = ct[i] + ct[i-1]
    
    wt = [ct[i] - burstTime[i] for i in range(len(burstTime))]
    return (sum(wt)//len(burstTime))
# T(n) = O(n * log n)
# S(n) = O(n)

burstTime = [6, 2, 8, 3]
print(avgWaitingTime(burstTime))