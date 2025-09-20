

class Solution:
    def longestDupSubstring(self, s: str) -> str:

        l = 0
        r = 0
        duplicate_string = ''
        while r < len(s):
            # find a string
            sub_string = s[l:r]
            # check if the string is a substring
            if sub_string in s[l + 1:]:
                if len(sub_string) > len(duplicate_string):
                    duplicate_string = sub_string
                r += 1

            else:
                l += 1
                r = l + 1

        return duplicate_string


class Solution:
    def longestDupSubstring(self, s: str) -> str:
        def search(length: int) -> str:
            seen = set()
            hash_val = 0
            base, mod = 26, 2 ** 63 - 1

            for i in range(length):
                hash_val = (hash_val * base + ord(s[i])) % mod
            seen.add(hash_val)

            baseL = pow(base, length, mod)
            for i in range(1, len(s) - length + 1):
                hash_val = (hash_val * base - ord(s[i - 1]) * baseL + ord(s[i + length - 1])) % mod
                if hash_val in seen:
                    return s[i:i + length]
                seen.add(hash_val)
            return ""

        left, right = 1, len(s)
        result = ""
        while left <= right:
            mid = (left + right) // 2
            substr = search(mid)
            if substr:
                result = substr
                left = mid + 1
            else:
                right = mid - 1
        return result

assert Solution().longestDupSubstring("zxcvdqkfawuytt") == 't'

# my solution
class Solution:
    def longestDupSubstring(self, s: str) -> str:
        def search(length: int) -> str:
            start = 0
            seen = {}
            while start + length <= len(s):
                if s[start: start + length] in seen:
                    return s[start: start + length]
                else:
                    seen[s[start:start + length]] = start + length
                start += 1
            return ""

        left, right = 1, len(s)
        result = ""
        while left <= right:
            mid = (left + right) // 2
            substr = search(mid)
            if substr:
                result = substr
                left = mid + 1
            else:
                right = mid - 1
        return result

assert Solution().longestDupSubstring("banana") == 'ana'