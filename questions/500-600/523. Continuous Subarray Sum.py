

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:

        l = len(nums)
        if l < 2:
            return False
        acc = 0
        hashtable = {0: -1}
        for idx in range(l):
            acc = acc + nums[idx]
            if acc % k in hashtable and idx - hashtable[acc % k] >= 2:
                return True
            elif acc % k not in hashtable:
                hashtable[acc % k] = idx
        return False