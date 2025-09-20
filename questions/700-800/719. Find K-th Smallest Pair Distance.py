

class Solution:
    def smallestDistancePair(self, nums, k: int) -> int:

        def check(dist: int) -> bool:

            i = j = cnt = 0

            for i in range(n):  # Use two ptrs to count pairs with
                while j < n and nums[j] - nums[i] <= dist:  # distance no greater than k
                    # count is treat j as center. look left, if nums[j] - num[i] <= dist, then nums[j] - nums[i+1] < dist.
                    # then the total count of pairs of distance less than dist is j - i
                    cnt += j - i
                    j += 1
            return cnt >= k  # return whether at least k such pairs exist

        nums.sort()
        n, left, right = len(nums), 0, nums[-1] - nums[0]

        while left < right:  # bin search

            mid = (left + right) // 2
            if check(mid):
                right = mid
            else:
                left = mid + 1

        return left

nums = [1,3,10,25,16]
assert Solution().smallestDistancePair(nums, 1) == 0