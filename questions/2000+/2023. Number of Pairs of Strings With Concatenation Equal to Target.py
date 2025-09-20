
class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        c=0
        l=nums.copy()
        temp=''
        for i in range (0,len(nums)):
            temp=l[i]
            l.pop(i)
            for j in l:
                if nums[i]+j==target:
                    c+=1
            l.insert(i,temp)
        return(c)