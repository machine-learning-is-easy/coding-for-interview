

class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        # Step 1: Precompute the sum of windows of size k
        window_sum = [0] * (n - k + 1)
        curr_sum = sum(nums[:k])
        window_sum[0] = curr_sum
        for i in range(1, n - k + 1):
            curr_sum += nums[i + k - 1] - nums[i - 1]
            window_sum[i] = curr_sum

        # Step 2: Build left array
        left = [0] * len(window_sum)
        best = 0
        for i in range(len(window_sum)):
            if window_sum[i] > window_sum[best]:
                best = i
            left[i] = best

        # Step 3: Build right array
        right = [0] * len(window_sum)
        best = len(window_sum) - 1
        for i in range(len(window_sum) - 1, -1, -1):
            if window_sum[i] >= window_sum[best]:  # >= for lexicographically smaller
                best = i
            right[i] = best

        # Step 4: Try all middle subarray positions
        max_total = 0
        res = []
        for m in range(k, len(window_sum) - k):
            l = left[m - k]
            r = right[m + k]
            total = window_sum[l] + window_sum[m] + window_sum[r]
            if total > max_total:
                max_total = total
                res = [l, m, r]
        return res