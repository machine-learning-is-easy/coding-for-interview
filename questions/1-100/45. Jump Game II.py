

class Solution:
    def jump(self, nums) -> int:

        jumps = [float("inf")] * len(nums)
        jumps[0] = 0
        for ind in range(len(nums)):
            max_jump = nums[ind]
            for steps in range(1, max_jump + 1):
                if ind + steps < len(nums):
                    jumps[ind + steps] = min(jumps[ind] + 1, jumps[ind + steps])

        return jumps[-1]

assert Solution().jump([2,3,1,1,4]) == 2