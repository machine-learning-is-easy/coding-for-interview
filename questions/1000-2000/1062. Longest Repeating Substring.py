

class Solution:
    def search(self, L: int, n: int, S: str) -> str:
        """
        Search a substring of given length
        that occurs at least 2 times.
        @return start position if the substring exits and -1 otherwise.
        """
        seen = set()
        for start in range(0, n - L + 1):
            tmp = S[start:start + L]
            if tmp in seen:
                return start
            seen.add(tmp)
        return -1

    def longestRepeatingSubstring(self, S: str) -> str:
        n = len(S)

        # binary search, L = repeating string length
        left, right = 1, n
        while left <= right:
            mid = left + (right - left) // 2
            if self.search(mid, n, S) != -1:
                left = mid + 1
            else:
                right = mid - 1

        return left - 1

# another short solution. window searching window length from n-1
class Solution:
    def longestRepeatingSubstring(self, s: str) -> int:
        n = len(s)
        window = n//2

        while window > 1:
            hashmap = {}
            for i in range(n - window + 1):
                temp = s[i: i + window]
                if temp in hashmap and i > hashmap[temp]:
                    # need to check the start index is greater than the end of first find string.
                    return window
                else:
                    hashmap[temp] = i + window - 1  # save the first time see the string maximum index

            window -= 1

        return 0

assert Solution().longestRepeatingSubstring("aaaaa") == 4