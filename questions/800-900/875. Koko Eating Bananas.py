

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if len(piles) == h:
            return max(piles)

        left, right = 1, max(piles)

        ans = -1
        while left <= right:
            mid = (left + right) // 2
            if sum([ceil(i / mid) for i in piles]) > h:
                left = mid + 1
            else:
                ans = mid
                right = mid - 1
        return ans