

class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:

        if len(intervals) <= 1:
            return True

        intervals.sort(key=lambda x: x[0])

        interval = intervals[0]

        for ind in range(1, len(intervals)):
            if intervals[ind][0] >= interval[1]:
                interval = intervals[ind]
            else:
                return False

        return True
