


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        res = []
        n = len(nums)

        def subset(nums, ind, tmp):

            if tmp not in res:
                res.append(list(tmp))

            for i in range(ind, n):
                tmp.append(nums[i])
                subset(nums, i + 1, tmp)
                tmp.pop(-1)

        subset(nums, 0, [])

        return res

assert Solution().subsetsWithDup([1, 2, 2]) == [[],[1],[1,2],[1,2,2],[2],[2,2]]