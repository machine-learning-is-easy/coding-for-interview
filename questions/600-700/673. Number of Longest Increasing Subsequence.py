

class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:

        n = len(nums)
        if n == 0:
            return 0

        lengths = [1] * n  # length of LIS ending at i
        counts = [1] * n  # number of LIS ending at i

        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    if lengths[j] + 1 > lengths[i]:
                        lengths[i] = lengths[j] + 1
                        counts[i] = counts[j]
                    elif lengths[j] + 1 == lengths[i]:
                        counts[i] += counts[j]

        max_len = max(lengths)
        return sum(c for l, c in zip(lengths, counts) if l == max_len)