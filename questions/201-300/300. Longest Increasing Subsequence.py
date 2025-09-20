

# DFS solution
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        l = len(nums)

        visited = {}

        def dfs(idx, value):
            nonlocal nums
            if idx == l:
                return 0
            else:
                if (idx, value) in visited:
                    return visited[(idx, value)]
                ans = 0  # this need to be 0, not float("inf"), because if the condition is not meet, will return -inf.
                for ind in range(idx, l):
                    if nums[ind] > value:
                        ans = max(ans, 1 + dfs(ind + 1, nums[ind]))

                visited[(idx, value)] = ans # add the current idx, value to hash table for later dfs use
                return ans

        return dfs(0, float('-inf'))
'''
Realizing a Dynamic Programming Problem

This problem has two important attributes that let us know it should be solved by dynamic programming. First, the question is asking for the maximum or minimum of something. Second, we have to make decisions that may depend on previously made decisions, which is very typical of a problem involving subsequences.

As we go through the input, each "decision" we must make is simple: is it worth it to consider this number? If we use a number, it may contribute towards an increasing subsequence, but it may also eliminate larger elements that came before it. For example, let's say we have nums = [5, 6, 7, 8, 1, 2, 3]. It isn't worth using the 1, 2, or 3, since using any of them would eliminate 5, 6, 7, and 8, which form the longest increasing subsequence. We can use dynamic programming to determine whether an element is worth using or not.

A Framework to Solve Dynamic Programming Problems

Typically, dynamic programming problems can be solved with three main components. If you're new to dynamic programming, this might be hard to understand but is extremely valuable to learn since most dynamic programming problems can be solved this way.

First, we need some function or array that represents the answer to the problem from a given state. For many solutions on LeetCode, you will see this function/array named "dp". For this problem, let's say that we have an array dp. As just stated, this array needs to represent the answer to the problem for a given state, so let's say that dp[i] represents the length of the longest increasing subsequence that ends with the i^{th}i 
th
  element. The "state" is one-dimensional since it can be represented with only one variable - the index i.

Second, we need a way to transition between states, such as dp[5] and dp[7]. This is called a recurrence relation and can sometimes be tricky to figure out. Let's say we know dp[0], dp[1], and dp[2]. How can we find dp[3] given this information? Well, since dp[2] represents the length of the longest increasing subsequence that ends with nums[2], if nums[3] > nums[2], then we can simply take the subsequence ending at i = 2 and append nums[3] to it, increasing the length by 1. The same can be said for nums[0] and nums[1] if nums[3] is larger. Of course, we should try to maximize dp[3], so we need to check all 3. Formally, the recurrence relation is: dp[i] = max(dp[j] + 1) for all j where nums[j] < nums[i] and j < i.

The third component is the simplest: we need a base case. For this problem, we can initialize every element of dp to 1, since every element on its own is technically an increasing subsequence.
'''
#
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)

assert Solution().lengthOfLIS([0,1,0,3,2,3]) == 4


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        sub = []
        for x in nums:
            i = bisect.bisect_left(sub, x)
            if i == len(sub):
                sub.append(x)
            else:
                sub[i] = x
        return len(sub)
# time complexity is O(nlogn)