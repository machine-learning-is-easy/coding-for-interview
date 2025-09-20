
class Solution:
    def subarraySum(self, nums, k: int) -> int:

        acc = [0] # first element of accumulation need to be 0
        total = 0

        for num in nums:
            total += num
            acc.append(total)

        hash_table = {}  # key is the value of accumulation, value is the times of value appear in accumulation

        res = 0
        for ind, v in enumerate(acc):

            residual = v - k
            if residual in hash_table:
                res += hash_table[residual]

            if v in hash_table:
                hash_table[v] += 1
            else:
                hash_table[v] = 1

        return res


nums = [1,1,1]
assert Solution().subarraySum(nums, 2) == 2