
class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0] * (n + 1)  # Extra space for easier handling of out-of-bounds

        for i in range(n - 1, -1, -1):
            points, brainpower = questions[i]
            next_q = i + brainpower + 1
            solve = points + (dp[next_q] if next_q < n else 0)
            skip = dp[i + 1]
            dp[i] = max(solve, skip)

        return dp[0]