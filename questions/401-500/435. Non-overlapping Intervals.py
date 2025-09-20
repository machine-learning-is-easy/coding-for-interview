
# sorting by the end of the interval can help to find the non-overlapping intervals with the minimum number of intervals to remove.

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        sorted_intervals = sorted(intervals, key=lambda x: x[1])

        res = []
        max_end = float(-inf)
        for interval in sorted_intervals:
            if interval[0] >= max_end:
                res.append(interval)
                max_end = interval[1]

        return len(intervals) - len(res)