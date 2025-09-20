

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        cur, count, d = 0, 0, defaultdict(int, {0:1})
        for i in nums:
            cur += i
            rem = cur % k
            count += d[rem]
            d[rem]+=1
        return count