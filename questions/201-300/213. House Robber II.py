

class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        # Helper function for linear House Robber problem
        def rob_linear(houses):
            prev = curr = 0
            for amount in houses:
                prev, curr = curr, max(curr, prev + amount)
            return curr

        # Option 1: Rob from house 0 to n-2
        # Option 2: Rob from house 1 to n-1
        return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))