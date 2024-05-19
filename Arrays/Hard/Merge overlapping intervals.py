def mergedIntervalsBruteForce(intervals):
    # intialize all necessary variables
    n = len(intervals)
    ans = []

    # sort the intervals so as to bring intervals closer
    intervals.sort()

    # Traversing the array
    for i in range(n):
        start = intervals[i][0]
        end = intervals[i][1]

        # if the current interval already lies 
        # inside the merged interval, continue
        if ans and ans[-1][1] >= end:
            continue

        # Now check for each element in array,
        # if overlapping, merge it
        for ii in range(i+1, n):
            if intervals[ii][0] <= end:
                end = max(end, intervals[ii][1])
            else:
                break
        
        # appending the merged interval in answer
        ans.append([start, end])

    return ans
# T(n) = O(nlogn) + O(2*n)

def mergedIntervalsOptimal(intervals):
    # intialize all necessary variables
    n = len(intervals)
    ans = []

    # sort the intervals so as to bring intervals closer
    intervals.sort()

    # Traversing the array
    for i in range(n):
        # Now if answer is empty or our interval is not overlapping
        # just add it to the answer array
        if not ans or ans[-1][1] < intervals[i][0]:
            ans.append(intervals[i])
        # If overlapping, then extend the existing interval to 
        # accomodate the current interval
        else:
            ans[-1][1] = max(ans[-1][1], intervals[i][1])
    
    return ans
# T(n) = O(nlogn) + O(n)

intervals = [[1,3], [2,6], [8,10], [5,7], [2,4], [9,11]]
print(mergedIntervalsBruteForce(intervals))
print(mergedIntervalsOptimal(intervals))