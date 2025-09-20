

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # ********** very good
        s_len = len(s)
        p_len = len(p)

        # base cases
        if p == s:
            return True
        elif (p == '*' or all([c == '*' for c in p])) and s == "":
            return True

        if p == '' or s == '' or s == "":
            return False

        # init all matrix except [0][0] element as False
        d = [[False] * (s_len + 1) for _ in range(p_len + 1)]
        d[0][0] = True

        # DP compute
        for p_idx in range(1, p_len + 1):
            # the current character in the pattern is '*'
            # remember last row matching index
            value = d[p_idx - 1]
            if all([r == False for r in value]):
                return False
            else:
                min_ind = value.index(True)

            if p[p_idx - 1] == '*':
                # * can be no matched words and multiple words,
                # starting from the index (last row is True)
                for s_idx in range(min_ind, s_len + 1):
                    if d[p_idx-1][s_idx] == True:
                        for i in range(s_idx, s_len + 1):
                            d[p_idx][i] = True
                        break

            # the current character in the pattern is '?'
            elif p[p_idx - 1] == '?':
                # if ?, need to loop with next token. because ? need to match one word
                for s_idx in range(min_ind + 1, s_len + 1):
                    d[p_idx][s_idx] = d[p_idx - 1][s_idx - 1]
                    # the current character in the pattern is not '*' or '?'
            else:
                # if character, need to loop with next token,
                # because token need to match at lease one word
                for s_idx in range(min_ind + 1, s_len + 1):
                    # Match is possible if there is a previous match
                    # and current characters are the same
                    if p[p_idx - 1] == s[s_idx - 1]:
                        d[p_idx][s_idx] = d[p_idx - 1][s_idx - 1]

        return d[p_len][s_len]

# another version DFS split and conquer, time complexity is 2^n
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if not p:
            return not s

        first_match = bool(s) and p[0] in {s[0], '*', '?'}

        if p[0] == "*":
            return self.isMatch(s[1:], p[1:]) or self.isMatch(s[1:], p)
        else:
            return first_match and self.isMatch(s[1:], p[1:])

# more concise solution
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True
        for j in range(1, n + 1):
            if p[j - 1] == "*":
                dp[0][j] = dp[0][j - 1]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == "?":
                    dp[i][j] = dp[i - 1][j - 1]

                if p[j - 1] == "*":
                    dp[i][j] = dp[i - 1][j] or dp[i][j - 1]

        return dp[m][n]

