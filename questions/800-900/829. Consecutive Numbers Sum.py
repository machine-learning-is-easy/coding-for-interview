
class Solution:
    def consecutiveNumbersSum(self, N: int) -> int:
        ans = 0
        upper_limit = int(math.sqrt(2 * N + 0.25) - 0.5) + 1
        for k in range(1, upper_limit):
            if (N - k * (k + 1) / 2) % k == 0:
                ans += 1
        return ans


# dfs searching strategy
class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:

        def dfs(number, total):
            if total < 0:
                return False
            elif total == 0:
                return True
            else:
                return dfs(number + 1, total - number)

        numbers = 0
        for num in range(1, n):
            if dfs(num, n):
                numbers += 1

        return numbers + 1