

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        n = len(nums)
        seen = set()
        # Go backward and find the longest suffix with all unique elements
        i = n - 1
        while i >= 0:
            if nums[i] in seen:
                break
            seen.add(nums[i])
            i -= 1

        # Elements to remove from the front = i + 1
        # One operation removes 3 elements
        return ceil((i + 1) / 3)