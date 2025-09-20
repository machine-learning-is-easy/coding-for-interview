

class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        ans = ""

        index = 0
        for bin_num in nums:
            # if change one digit, the result will different from current number,
            # iteration from all numbers, it mean the ans will different from all number
            ans = ans + str(1 - int(bin_num[index]))
            index += 1
        return ans