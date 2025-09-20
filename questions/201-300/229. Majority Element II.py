


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        frequency = len(nums) // 3

        dp = dict()

        res = {}
        for item in nums:
            if item in dp:
                dp[item] += 1
            else:
                dp[item] = 1

            if dp[item] > frequency:
                res[item] = ""

        return list(res.keys())

# concise version
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # Counters for the potential majority elements
        count = {}
        res = set()
        freq = floor(len(nums)/3)
        for num in nums:
            count[num] = count.get(num, 0) + 1
            if num not in res and count[num] > freq:
                res.add(num)

        return list(res)


a = [1,1,1,1,2,3,4,5,6,7,8,9,10]

assert Solution().majorityElement(a) == [1]
