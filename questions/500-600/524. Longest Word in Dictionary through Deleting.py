


class Solution:
    def findLongestWord(self, s: str, dictionary) -> str:

        def word_in_string(s, word):
            if not s:
                return False

            s_p, w_p = 0, 0
            while s_p < len(s):
                if s[s_p] == word[w_p]:
                    if w_p == len(word) - 1:
                        return True
                    w_p += 1
                s_p += 1
            else:
                return False

        dictionary.sort(key=lambda x: (-len(x), x))

        for word in dictionary:
            if word_in_string(s, word):
                return word

        return ""

assert Solution().findLongestWord("abpcplea", ["ale","apple","monkey","plea"]) == 'apple'