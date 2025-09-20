

class Solution:
    def countSubstrings(self, s: str) -> int:

        def isPalindromic(s: str, ind: int) -> int:
            # return the maximum index of the Palindromic string
            l, r = 0, 0
            total = 0
            for l, r in [(0, 0), (0, 1)]:
                while ind + r < len(s) and ind + l >= 0:
                    if s[ind + r] == s[ind + l]:
                        l -= 1
                        r += 1
                        total += 1
                    else:
                        break

            return total

        pali_n = 0
        ind = 0
        while ind < len(s):
            total = isPalindromic(s, ind)
            pali_n += total
            ind += 1

        return pali_n

