

class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if not s or not k:
            return 0
        hashtable = collections.defaultdict(int)

        ans = 0
        prev = 0
        for ind, l in enumerate(s):
            hashtable[l] += 1
            while prev < len(s) and len(hashtable) > k:
                hashtable[s[prev]] -= 1
                if hashtable[s[prev]] <= 0:
                    del hashtable[s[prev]]
                prev += 1

            ans = max(ans, ind - prev + 1)
        return ans