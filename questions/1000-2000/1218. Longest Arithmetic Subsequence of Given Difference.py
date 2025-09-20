

class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        map = {}
        for val in arr:
            map[val] = map.get(val - difference, 0) + 1
        return max(map.values())