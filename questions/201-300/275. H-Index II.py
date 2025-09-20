

class Solution:
    def hIndex(self, citations: List[int]) -> int:

        l = 0
        n = len(citations)
        h = n - 1
        ans = -1

        while l <= h:
            mid = l + (h - l) // 2;
            if citations[mid] == n - mid:
                return citations[mid]
            elif citations[mid] < n - mid:
                l = mid + 1;
            else:
                h = mid - 1

        return n - l