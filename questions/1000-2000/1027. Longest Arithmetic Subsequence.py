
class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        lasnum = [] # list of {delta: frequency}
        maxEnc = 0
        for i in range(0, len(nums)):
            lasset = {}
            for j in range(i):
                if ((nums[i] - nums[j]) in lasnum[j]):
                    newval = lasnum[j][nums[i] - nums[j]] + 1
                else:
                    newval = 2
                maxEnc = max(maxEnc, newval)
                lasset.update({nums[i] -  nums[j] : newval})
            lasnum.append(lasset)
        return maxEnc