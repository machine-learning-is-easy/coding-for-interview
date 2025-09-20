

class Solution:
    def checkSubarraySum(self, nums, k: int) -> bool:

        # calculate the accumulative sum
        acc = [0] * len(nums)
        acc[0] = 0
        for i in range(len(nums)):
            acc.append(acc[-1] + nums[i])

        # put acc into mod hashmap

        hash_map = {0: 0}
        for i in range(1, len(acc)):
            mod_n = acc[i] % k
            if mod_n in hash_map:
                if i + 1 > hash_map[mod_n]:
                    return True
            else:
                hash_map[mod_n] = i

        return False

assert Solution().checkSubarraySum([23,2,4,6,6], 7) == True
