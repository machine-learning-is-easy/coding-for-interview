

class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:

        count, i = {}, 0
        max_len = 0
        for j, k in enumerate(s):
            count[k] = count.get(k, 0) + 1
            if len(count) > 2:
                count[s[i]] -= 1
                if count[s[i]] == 0:
                    del count[s[i]]
                i += 1

            if len(count) <= 2:
                max_len = max(max_len, j - i + 1)
        return max_len