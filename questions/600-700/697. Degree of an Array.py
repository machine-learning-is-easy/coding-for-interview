

class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:

        leftfirstseen = {}
        rightfirstseen = {}
        frequency = {}

        degree = 0

        for ind, i in enumerate(nums):
            if i not in leftfirstseen:
                leftfirstseen[i] = ind

            if i not in frequency:
                frequency[i] = 1
            else:
                frequency[i] += 1

            degree = max(degree, frequency[i])

        for ind in range(len(nums) - 1, -1, -1):
            if nums[ind] not in rightfirstseen:
                rightfirstseen[nums[ind]] = ind

        keys = [key for key in frequency if frequency[key] == degree]

        min_len = min([rightfirstseen[key] - leftfirstseen[key] + 1 for key in keys])

        return min_len