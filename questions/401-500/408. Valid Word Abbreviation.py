
class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:

        i = j = 0
        m, n = len(word), len(abbr)
        while i < m and j < n:
            if word[i] == abbr[j]:
                i += 1
                j += 1
            elif abbr[j] == "0":  # need to ask if 0 is valid
                return False
            elif abbr[j].isnumeric():
                k = j
                while k < n and abbr[k].isnumeric():
                    k += 1
                i += int(abbr[j:k])
                j = k
            else:
                return False
        return i == m and j == n

word = "internationalization"
abbr = "i12iz4n"
assert Solution().validWordAbbreviation(word, abbr) == True