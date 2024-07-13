def jobsDone(jobs):
    jobs.sort(key = lambda x: x[2], reverse = True)
    
    maxDeadline = max(job[1] for job in jobs)
    timeSlots = [-1]*maxDeadline
    jobsDone = 0
    profitGained = 0
    
    for job in jobs:
        for time in range(job[1]-1, -1, -1):
            if timeSlots[time] == -1:
                timeSlots[time] = job[0]
                jobsDone += 1
                profitGained += job[2]
                break
    
    return [jobsDone,profitGained]
# T(n) = O(n * log n)
# S(n) = O(n)

jobs = [[1, 4, 20], [2, 1, 10], [3, 1, 40], [4, 1, 30]]
print(jobsDone(jobs))