

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums

        st = []
        res = []

        for i in range(k):
            heapq.heappush(st, (-nums[i], i))

        res.append(-st[0][0])

        for i in range(k, len(nums)):
            heapq.heappush(st, (-nums[i], i))
            while st[0][1] <= i - k:
                heapq.heappop(st)
            res.append(-st[0][0])

        return res