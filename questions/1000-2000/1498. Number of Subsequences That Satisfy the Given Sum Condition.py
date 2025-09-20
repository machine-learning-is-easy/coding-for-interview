

class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        MOD = 10 ** 9 + 7
        nums.sort()
        n = len(nums)

        # Precompute powers of 2 up to n
        power = [1] * n
        for i in range(1, n):
            power[i] = (power[i - 1] * 2) % MOD

        res = 0
        left, right = 0, n - 1

        while left <= right:
            if nums[left] + nums[right] <= target:
                res = (res + power[right - left]) % MOD
                left += 1
            else:
                right -= 1

        return res