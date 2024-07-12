# Approach: Sort the meetings in order of their ending
#           so that a room is free at the very next meeting.
def numberOfMeetings(start, end):
    meetings = []
    for i in range(len(start)):
        meetings.append([start[i], end[i]])
    
    sorted_meetings = sorted(meetings, key=lambda x: x[1])

    # Initialize the list of selected meetings with the first meeting
    selected_meetings = [sorted_meetings[0]]
    last_end_time = sorted_meetings[0][1]
    
    # Iterate through the remaining meetings
    for i in range(1, len(sorted_meetings)):
        if sorted_meetings[i][0] > last_end_time:
            selected_meetings.append(sorted_meetings[i])
            last_end_time = sorted_meetings[i][1]
    
    return len(selected_meetings)
# T(n) = O(n * logn)
# S(n) = O(n)

start = [1,3,0,5,8,5]
end = [2,4,6,7,9,9]

print(numberOfMeetings(start, end))