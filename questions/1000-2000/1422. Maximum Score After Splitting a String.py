
class Solution:
    def maxScore(self, s: str) -> int:
        max_score = 0
        zero_count = 0
        one_count = s.count('1')
        for i in range(len(s) - 1):
            if s[i] == '0':
                zero_count += 1
            else:
                one_count -= 1
            max_score = max(max_score, zero_count + one_count)
        return max_score