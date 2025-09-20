

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)

        # Base case.
        if 1 not in nums:
            return 1

        # nums = [1]
        if n == 1:
            return 2

        for integar in range(1, n + 1):
            if integar not in nums:
                return integar

        return integar + 1