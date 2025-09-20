
import itertools
class Solution:
    def expressiveWords(self, S, words) -> int:

        group = lambda x: [(k, len(list(v))) for k, v in itertools.groupby(x)]
        S, count = group(S), 0
        for W in map(group, words):
            if len(W) != len(S): continue
            for s, w in zip(S, W):
                if s[0] != w[0] or s[1] < w[1] or w[1] < s[1] < 3:
                    break
            else:
                count += 1

        return count

# two pointers
class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:

        def similary(long_s, short_s):
            n = len(long_s)
            m = len(short_s)

            idx_n, idx_m = 0, 0

            while idx_n < n and idx_m < m:
                if long_s[idx_n] != short_s[idx_m]:
                    return False

                c_n = long_s[idx_n]
                num_c_n = 1
                while idx_n + 1 < n and long_s[idx_n + 1] == c_n:
                    idx_n += 1
                    num_c_n += 1

                num_c_m = 1
                while idx_m + 1 < m and short_s[idx_m + 1] == c_n:
                    idx_m += 1
                    num_c_m += 1

                if num_c_n == num_c_m or (num_c_n >= num_c_m and num_c_n >= 3):
                    idx_m += 1
                    idx_n += 1
                else:
                    return False

            if idx_n == n and idx_m == m:
                return True
            return False

        total_n = 0
        for word in words:
            if similary(s, word):
                total_n += 1

        return total_n


# DFS version
class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        n = len(s)

        @cache
        def dfs(i, j, word):
            if i >= n and j >= len(word):
                return True
            if i >= n or j >= len(word):
                return False

            if s[i] == word[j]:
                tak = dfs(i + 1, j + 1, word)

                count_s = count_word = 1
                while i + 1 < n and s[i] == s[i + 1]:
                    i += 1
                    count_s += 1

                while j + 1 < len(word) and word[j] == word[j + 1]:
                    j += 1
                    count_word += 1

                if count_s < count_word or (count_s > count_word and count_s < 3):
                    return False

                rep = dfs(i + 1, j + 1, word)

                return tak or rep

            return False

        res = 0
        for w in words:
            if dfs(0, 0, w):
                res += 1

        return res
s = "zzzzzyyyyy"
words = ["zzyy", "zy", "zyy"]

assert Solution().expressiveWords(s, words) == 3
