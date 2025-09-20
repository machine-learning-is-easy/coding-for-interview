


class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:

        acc = defaultdict(int)
        acc[0] = -1
        total = 0
        max_size = 0
        for idx, v in enumerate(nums):
            total += v
            if total - k in acc:
                max_size = max(max_size, idx - acc[total - k])

            if total not in acc:
                acc[total] = idx
        return max_size