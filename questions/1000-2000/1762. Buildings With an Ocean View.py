

class Solution:
    def findBuildings(self, heights):

        right_highest = list(heights)
        max_height = 0
        for ind in range(len(heights) - 1, -1, -1):
            right_highest[ind] = max_height
            max_height = max(max_height, heights[ind])
        view_num = []
        ind = 0
        for height, righ_height in zip(heights, right_highest):
            if height > righ_height:
                view_num.append(ind)
            ind += 1
        return view_num

assert Solution().findBuildings([4,2,3,1]) == [0,2,3]


# more concise solution
class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:

        ind = len(heights) - 1
        max_so_far = 0
        res = []
        while ind >= 0:
            if heights[ind] > max_so_far:
                res.insert(0, ind)
            max_so_far = max(max_so_far, heights[ind])
            ind -= 1
        return res