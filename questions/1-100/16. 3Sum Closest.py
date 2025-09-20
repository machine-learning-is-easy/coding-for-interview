

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:

        nums = sorted(nums)
        l = len(nums)
        result = float("inf")
        for i in range(l):

            pointerA = i + 1
            pointerB = l - 1

            while pointerA < pointerB:
                r = nums[i] + nums[pointerA] + nums[pointerB]
                if r < target:
                    pointerA += 1
                else:
                    pointerB -= 1

                if abs(r - target) < abs(result - target):
                    result = r

        return result
