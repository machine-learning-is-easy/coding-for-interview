

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:

        g.sort()
        s.sort()
        count = 0
        while g:
            greed = g.pop(0)
            meet = 0
            for idx in range(len(s)):
                if s[idx] >= greed:
                    count += 1
                    s.pop(idx)
                    meet = 1
                    break
            if meet == 0:
                return count
        return count
# time complexity is O(n^2) where n is the length of the list g or s

# one loop and the other one is binary search
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:

        g.sort()
        s.sort()
        count = 0
        while g:
            greed = g.pop(0)
            l = 0
            r = len(s) - 1
            while l <= r:
                mid = (l + r) // 2
                if s[mid] < greed:
                    l = mid + 1
                else:
                    r = mid - 1
            if l < len(s) and s[l] >= greed:
                s.pop(mid)
                count += 1
            else:
                return count
        return count
# time complexity is O(nlogn) + O(nlogn) = O(nlogn) where n is the length of the list g or s

# two pointers
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        content_children = 0
        cookie_index = 0
        while cookie_index < len(s) and content_children < len(g):
            if s[cookie_index] >= g[content_children]:
                content_children += 1
            cookie_index += 1
        return content_children

# time complexity is O(nlogn) + O(n) = O(nlogn) where n is the length of the list g or s