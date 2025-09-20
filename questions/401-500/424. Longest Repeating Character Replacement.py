

from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        back = 0
        max_len = 0
        for front, char in enumerate(s):
            count[char] += 1
            if front - back + 1 - max(count.values()) > k:
                count[s[back]] -= 1
                back += 1
            else:
                max_len = max(max_len, front - back + 1)

        return max_len