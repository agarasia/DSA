def minimizeMaximumDistance(stations, k):
    def numberOfStationsNeeded(distance):
        l = len(stations)
        cnt = 0

        for i in range(1, l):
            numberInBetween = ((stations[i] - stations[i - 1]) / distance)
            if (stations[i] - stations[i - 1]) == (distance * numberInBetween):
                numberInBetween -= 1
            cnt += numberInBetween
        
        return cnt
    
    n = len(stations)
    low, high = 0, 0

    for i in range(n-1):
        high = max(high, stations[i+1] - stations[i])
    
    diff = 1e-6
    while high - low >= diff:
        mid = low + (high - low)/2.0
        count = numberOfStationsNeeded(mid)
        if count > k:
            low = mid
        else:
            high = mid

    return high


stations = [1, 2, 3, 4, 5]
k = 4

print(minimizeMaximumDistance(stations, k))