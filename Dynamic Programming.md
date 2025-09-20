30.	Dynamic Programming
Keynote:
1.	A list of dictionaries to keep records of current status. 
Attention: BFS to DP. normally BFS solve the best steps, DFS get the solutions like path or permutation. DP solve min or max number of solutions. Sometime DP can also solve the best solution if the search direction is one way, for example from left to right. From top left to right bottom. BFS can be any direction. DP is greedy search, as each step, the optimum can be calculated.
Template of one dimension of dynamic programming
1)	Define an array of DP
2)	Initialization of the first element
3)	Iteration rest of the element with transition function
Template of two dimensions of dynamic programming
1)	define two-dimension array DP
2)	initialization of row 0 and column 0 value
3)	iteration rest of DP element with transition function
 
a.	Coins amount
518. https://leetcode.com/problems/coin-change-2/
Tips: The outer loop is the coin number; the inner loop is the amount. The transition function is dp[n] += dp[n-coin]. Cannot use backtracking, backtracking will treat [2, 1, 2] and [1, 2, 2] the same.  This solution is using coin by coin. First, use one coin to get all the coin combinations. Then add the second coin. If the coins are not sorted, need to sort the coins in ascending order.
class Solution:
    def change(self, amount: int, coins) -> int:

        dp = [0] * (amount + 1)
        dp[0] = 1  # one coin, 0 amount

        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] += dp[x - coin]

        return dp[- 1]

class Solution:
    def change(self, amount:int, coins) -> int:
        res = 0

        def recursive(amount, memo):
            nonlocal res
            if amount == 0:
                res += 1
            elif amount < 0:
                return

            for coin in coins:
                memo.append(coin)
                recursive(amount - coin, memo)
                memo.pop()

        recursive(amount, [])
        return res

70. Climbing Stairs: https://leetcode.com/problems/climbing-stairs/
This is like the coins amount. The transition function id dp[n] = dp[n-1] + dp[n-2]

2979. Most Expensive Item That Can Not Be Bought

class Solution:
    def mostExpensiveItem(self, primeOne: int, primeTwo: int) -> int:
        j = primeOne * primeTwo

        dp = [False] * j
        dp[primeOne] = True
        dp[primeTwo] = True

        for i in range(j):
            dp[i] = dp[i] or dp[i - primeOne] or dp[i - primeTwo]

        for k in range(j - 1, -1, 1):
            if not dp[k]:
                return k

        return j - primeOne - primeTwo


b.	Number of dice rolls or coins flip
1155. Number of Dice Rolls with Target Sum
Tips: it is different from coin amount which is unlimited coins. But dices rolls has limited dices
The transition function is d[dice_n][target] += d[dice_n – 1][target – face_amount]
Current (dice_number, target) += (dice_number -1, target -face amount). When add one more dice, the extra dice face can be all possible face_number (1, 2, 3….). 

Recursive (this is a typical DFS)
class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        res = 0
        memo = []
        def recursive(amount, n, k):
            nonlocal res
            nonlocal memo
            if amount == 0 and n == 0:
                res += 1
            elif amount < 0 or n < 0:
                return

            for amt in range(1, k + 1):
                memo.append(amt)
                recursive(amount - amt, n - 1, k)
                memo.pop()

        recursive(target, n, k)
        return res


c.	Unique path
63. Unique Paths II
https://leetcode.com/problems/unique-paths-ii/
Tips can be solved with dynamic programming, BFS(BFS does not work) or DFS.

From top left to bottom right, only consider non-blocked cells. If one can search in four directions, one must use BFS or DFS. This requires moving right, bottom. Need

If only moving in two directions and finding the total number of unique paths, can use dynamic programming and DFS
If can move in four directions and find the total number of unique paths, need to use DFS. 
If need to find the minimum steps with four possible moving directions, need to use BFS.

64. Minimum Path Sum: https://leetcode.com/problems/minimum-path-sum/
72. Edit Distance: https://leetcode.com/problems/edit-distance/
TIPS: left, right and left right cell. If current characters are equal, Current cell distance = min(left, right, left right) else current cell distance = min(left, right, left right +1)
62. Unique Paths: https://leetcode.com/problems/unique-paths/
Start from the top left corner, iterate to right bottom. Transit function current cell value equal up cell + left cell


332. Reconstruct Itinerary ***
BFS or DFS
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)

        for src, dst in sorted(tickets, reverse=True):
            graph[src].append(dst)

        itinerary = []

        def dfs(airport):
            while graph[airport]:
                dfs(graph[airport].pop())
            itinerary.append(airport)

        dfs("JFK")

70. Climbing Stairs
322. Coin Change
TIPS: this question is finding the fewer coins, need to sort the face amount reverse=True.  Start to select denominations from the left (the higher denominations the fewer coins required). Try to add higher face amount coins, if find the residual = 0, return immediately, if residual < 0, need to pop the end of the memo and try a smaller face amount.

300. Longest Increasing Subsequence
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

198. House Robber
The transition function is max_value(current_index) = max(max_value[current_index – 1], current_value + max_value[current_index – 2]
213. House Robber II
91. Decode Ways
62. Unique Paths
55. Jump Game
TIPS: keep maximum reachable index, iteration from left to right, if index > maximum reachable index, return false. And update the maximum reachable index. 
139. Word Break
1027. Longest Arithmetic Subsequence
TIPS: keep a list of dictionaries of delta: frequency. For new element, check previous index and calculate the delta. Update the new index dictionaries.
A dictionary of delta: frequency dose not work
Compared with 1048 longest string chain. 1048 is using one dictionary while 1027 need to keep a dictionary for each index (a list of dictionaries)

221. Maximal Square
1799. Maximize Score After N Operations
3202. Find the Maximum Length of Valid Subsequence II
Iteration from 0 to K in outer loop. In inner loop, crate a dp array to save the maximum length of length. The index is residual of the addition. The value of dp[i] is the maximum length. For given element

class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:

        max_length = 0

        # Iterate over each possible remainder value from 0 to k-1
        for target_remainder in range(k):

            # Initialize the dynamic programming array to store the maximum length for each remainder
            dp = [0] * k

            # Iterate over each number in the input array
            for num in nums:
                # Calculate the remainder of the current number when divided by k
                current_remainder = num % k

                # Calculate the remainder that would achieve the target remainder when added to the current number
                previous_remainder = (target_remainder - num) % k

                # Update the dp array
                dp[current_remainder] = max(dp[current_remainder], dp[previous_remainder] + 1)

            # Update the result with the maximum value found in the dp array for the current target remainder
            max_length = max(max_length, max(dp))

        return max_length
