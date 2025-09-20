
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = [x for x in nums if x > 0]
        neg = [x for x in nums if x < 0]

        result = []
        for p, n in zip(pos, neg):
            result.append(p)
            result.append(n)

        return result