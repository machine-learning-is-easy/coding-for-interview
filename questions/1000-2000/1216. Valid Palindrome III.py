

class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        if k < 0:
            return False
        if s == '' or len(s) == 1:
            return True
        start = 0
        end = len(s) - 1
        while start <= end:
            if s[start] == s[end]:
                return self.isValidPalindrome(s[start+1:end], k)
            else:
                return self.isValidPalindrome(s[start: end], k - 1) or self.isValidPalindrome(s[start + 1: end + 1], k - 1)

# the time complexity is O(2^n) and the space complexity is O(n)

# O(n)
class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        # queue holds a tuple of `l` and `r`, and the depth `curr_k`.
        queue = deque([(0, len(s) - 1, 0)])
        visited = set()

        while queue:
            l, r, curr_k = queue.popleft()  # also can use a heap to get the smallest max left element.

            # If the budget is exceeded return False
            if curr_k > k:
                return False

            # Shave off the two ends of s[l:r+1] until end characters
            # don't match. Each graph node is defined by (l,r)
            # where s[l] != s[r].
            while s[l] == s[r]:
                l += 1
                r -= 1
                # if you reach the end node, you've found a k-palindrome
                if l >= r:
                    return True

            # append the two new nodes to the queue.
            if (l + 1, r) not in visited:
                queue.append((l + 1, r, curr_k + 1))
                visited.add((l + 1, r))

            if (l, r - 1) not in visited:
                queue.append((l, r - 1, curr_k + 1))
                visited.add((l, r - 1))

# time complexity is O(n^2) and the space complexity is O(n^2)

class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        n = len(s)
        dp = [[0] * n for _ in range(n)]

        # Fill the DP table
        for length in range(2, n + 1):  # length of substring
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1]  # no need to delete
                else:
                    # one delete needed: delete s[i] or s[j]
                    dp[i][j] = min(dp[i + 1][j], dp[i][j - 1]) + 1

        return dp[0][n - 1] <= k

# time complexity is O(n^2) and the space complexity is O(n^2)