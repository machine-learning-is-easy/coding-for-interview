

# another solution is brutal force, two loops, out loop iteration over the entire array, inner loop interation all the elments
# after the index of first loop, and find all the element not in repeat.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # ******
        ans = 0  # maximum length of substring
        # mp stores the maximum index of a character
        # key: character, value: maximum index
        mp = {}

        anchor = -1  # record the unrepeated string start index

        for j in range(len(s)):
            if s[j] in mp:
                anchor = max(mp[s[j]], anchor)

            ans = max(ans, j - anchor)
            mp[s[j]] = j

        return ans

assert Solution().lengthOfLongestSubstring("pwwkew") == 3