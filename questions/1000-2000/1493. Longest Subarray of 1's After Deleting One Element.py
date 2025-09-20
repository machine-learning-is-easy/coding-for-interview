

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        front = 0
        back = 0
        count = 0 # count 0s
        max_len = 0
        while front < len(nums):
            if nums[front] == 0:
                count += 1

            while count > 1:
                if nums[back] == 0:
                    count -= 1
                back += 1
            max_len = max(max_len, front - back + 1)
            front += 1
        return max_len - 1