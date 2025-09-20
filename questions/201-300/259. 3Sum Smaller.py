

class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        #choose three elements from the array, and the order doesn't matter, and beause our gaol is to find something related to the sum, so in the first step, sort in
        nums.sort()
        res = 0
        for i in range(len(nums)-2):
            #find the number of result when the first element of the triplet is nums[i]
            l,r = i+1, len(nums)-1
            #use two pointer as the second and end point of the triplet
            while l < r:
                if nums[i]+nums[l]+nums[r] < target:
                    #if nums[i]+nums[l]+nums[r] < target, then r-1,r-2...r-(r-l-1) all satisfy the rrequirement
                    res += r-l
                    #all the possible cases when the middle element has the index of l are considered
                    l += 1
                else:
                    #if nums[i]+nums[l]+nums[r] < target, then l+1, l+2..l+(r-l-1) are all not available, so all cases with r are considered
                    r -= 1
        return res