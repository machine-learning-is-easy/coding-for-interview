

class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:

        res = defaultdict(list)
        for r, l in enumerate(nums):
            for c, ele in enumerate(l):
                res[r + c].append(ele)

        res_list = []
        key = 0
        while key in res:
            res_list += res[key][::-1]
            key += 1
        return res_list