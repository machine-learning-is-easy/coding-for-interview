
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m, n = len(haystack), len(needle)

        if n == 0:
            return 0

        for i in range(m - n + 1):
            if haystack[i:i+n] == needle:
                return i

        return -1


# needle to a set for fast checking if haystack[i:i+n] in set

# rolling hash and KMP

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0

        base = 256
        mod = 10 ** 9 + 7
        n, m = len(haystack), len(needle)

        if m > n:
            return -1

        # Compute the hash of the needle
        hash_needle = 0
        for ch in needle:
            hash_needle = (hash_needle * base + ord(ch)) % mod

        # Precompute base^(m-1) for rolling
        high_base = pow(base, m - 1, mod)

        # Rolling hash for haystack
        hash_hay = 0
        for i in range(m):
            hash_hay = (hash_hay * base + ord(haystack[i])) % mod

        if hash_hay == hash_needle and haystack[:m] == needle:
            return 0

        for i in range(m, n):
            hash_hay = (
                               (hash_hay - ord(haystack[i - m]) * high_base) * base + ord(haystack[i])
                       ) % mod
            if hash_hay == hash_needle and haystack[i - m + 1:i + 1] == needle:
                return i - m + 1

        return -1