

class Solution:
    def partitionDisjoint(self, nums: list) -> int:
        # binary search of the array

        n = len(nums)
        # max(left) <= min(right)
        maxleft, minright = {}, {}
        maxv, minv = float('-inf'), float('inf')

        for i in range(n):
            maxv = max(maxv, nums[i])
            maxleft[i] = maxv

        for i in range(n - 1, -1, -1):
            minv = min(minv, nums[i])
            minright[i] = minv

        for i in range(n - 1):
            if maxleft[i] <= minright[i + 1]:
                return i + 1

assert  Solution().partitionDisjoint([1,1,1,0,6,12]) == 4