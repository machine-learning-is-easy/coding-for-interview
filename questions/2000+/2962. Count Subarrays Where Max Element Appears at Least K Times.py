
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_num = max(nums)
        n = len(nums)
        res = 0
        j = 0
        count = 0

        for i in range(n):
            # Move j to right until count of max_num >= k
            while j < n and count < k:
                if nums[j] == max_num:
                    count += 1
                j += 1
            if count >= k:
                res += n - j + 1
            # Move left boundary of window
            if nums[i] == max_num:
                count -= 1

        return res