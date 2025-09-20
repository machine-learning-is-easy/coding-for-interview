

class Solution(object):
    def merge(self, intervals):

        if not intervals:
            return intervals
        result = []
        intervals.sort()
        merged_interval = intervals[0]

        for ind in range(1, len(intervals)):
            if merged_interval[1] >= intervals[ind][0]:
                merged_interval[1] = max(merged_interval[1], intervals[ind][1])
            else:
                result.append(merged_interval)
                merged_interval = intervals[ind]
        result.append(merged_interval)

        return result