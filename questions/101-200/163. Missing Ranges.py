

class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        ans = []
        # iterate all the numbers in the array
        for num in nums:
            # when the current number larger than the current lower
            # that means there is a gap, add the gap into ans
            # the range is [lower, num - 1]
            if num > lower:
                ans.append([lower, num - 1])

            # otherwise, update the lower to the next integer after current number
            lower = num + 1

        # After go through all the number in the array
        # the lower will be the next integer of the last number
        # if there is a gap between the lower and the upper, append the range to the ans as result.
        if lower <= upper:
            ans.append([lower, upper])

        return ans