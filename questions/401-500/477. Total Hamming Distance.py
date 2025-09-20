


class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        total = 0
        n = len(nums)

        for i in range(32):  # for each bit position
            countOnes = 0
            for num in nums:
                if (num >> i) & 1:
                    countOnes += 1
            countZeros = n - countOnes
            total += countOnes * countZeros

        return total