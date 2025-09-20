


class Solution:
    def numberOfWeakCharacters(self, properties) -> int:
        properties.sort(key=lambda x: (-x[0], x[1]))
        ans = 0
        curr_max = 0

        for _, d in properties:
            if d < curr_max:
                ans += 1
            else:
                curr_max = d
        return ans

properties = [[1,5],[10,4],[4,3]]

assert Solution().numberOfWeakCharacters(properties) == 1
