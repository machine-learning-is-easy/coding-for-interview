
class Solution:
    def rob(self, nums: List[int]) -> int:
        if(len(nums)<3): return max(nums)

        for i in range(2,len(nums)):
            big = max(nums[i-2],nums[i-1])

            if(big==nums[i-2]):
                nums[i]+=nums[i-2]
                nums[i-1]=big
                big=nums[i]
            else:
                nums[i]=max(big, nums[i]+nums[i-2])
        return max(nums[-1], nums[-2])


# another senario
class Solution:
    def rob(self, nums: List[int]) -> int:
        length = len(nums)
        dp = [0] * length
        if length <= 2:
            return max(nums)

        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        ind = 2
        while ind < length:
            dp[ind] = max(dp[ind - 2] + nums[ind], dp[ind - 1]) # maxium is max of rob current one, and not rob current one.
            ind += 1
        return dp[-1]