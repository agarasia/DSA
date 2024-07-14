def nonOverlappingIntervals(intervals):
    count = 0

    # Sort according to end times
    intervals.sort(key = lambda x: x[1])

    end = intervals[0][1]
    for i in range(1, len(intervals)):
        # Check for overlapping
        if intervals[i][0] < end:
            count += 1
        else:
            end = intervals[i][1]
    
    return count
# T(n) = O(n)
# S(n) = O(1)

intervals = [[1,100], [11,22], [1,11], [2,12]]

print(nonOverlappingIntervals(intervals))