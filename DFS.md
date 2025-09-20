28.	DFS
Key Points:
a)	Pay attention adding element to the visited hash table, (DFS needs to process when entering iterative loop whereas BFS needs to add visited when adding the nodes to the queue)
b)	In selection questions like permutation. Don’t need to keep the visited table while need to keep the remaining table like 47, 47 keep the remaining dictionary not visited table. and loop checks the remaining table value. 
c)	Not every DFS needs a visited hash table. Like 463. Island Perimeter
a.	This question is calculating the edges with 0. Every direction entering from 1 to 0 is one edge. Also, this can be solved with and without DFS. 
d)	What situation needs to visited.remove()? 
a.	Visited.add(), visited.remove() do not necessarily appear together, in the backtracking, it appears in the loop. But in DFS, it only has visited.add() and check if the new point is in the visited or not. While the backtracking needs adding and removing the element.
b.	If duplicated elements, need a list of elements to check visited.
e)	Efficiency (add lru_cache() to the function) if the function has returns and the parameter does not have set and dictionary. It only applies to the DFS.
f)	Function parameters (depends on the question, common parameters are, index, value, memo, dict), for example, 417 needs to add the previous cell height into the parameter. 1335 needs to add the index to the DFS function.
g)	Processing the end condition (in a finding possibility question, if find one solution, return directly, or break the loop. In a finding the lowest or highest, need to finish the loop and then return the value)
h)	Loop of recursive call DFS
a.	In reachable questions, if find one return immediately. But in finding minimum or maximum questions, need to finish all loops. 
i)	Return value (if possible, assign a default value, then check if the return is the default value or not). Find the minimum, the initial value is Inf. If find the maximum, the initial value is -Inf.
j)	Time complexity (for questions like the number of islands or number of provinces, the time complexity is m*n (the loop of every value) + m *n (DFS or BFS, the entire number of calls this function is all the value of the matrix))
k)	Cache can fast the dfs searching time.
l)	Two types of question, all the possible realization and how many realizations. In the first scenario, need to add the result in the DFS function, in the second scenario, need to return the value of each DFS function.

Typically, DFS needs a visited set. Put all visited cells into the set. Ignore the element which is already visited.

def _dfs(node, visited):
    # find if node island is surrounded by "X"
    r, c = node
    if r < 0 or r > r_n or c < 0 or c > c_n:
        return

    if node not in visited:
        if board[r][c] == 'O':
            visited.add(node)
            _dfs((r - 1, c), visited)
            _dfs((r + 1, c), visited)
            _dfs((r, c - 1), visited)
            _dfs((r, c + 1), visited)
	    visited.remove(node)

17. Letter Combinations of a Phone Number
TIPS: it can be implemented with an array, but the BFS is better. 

339. Nested List Weight Sum
TIPS: instead of knowing it is a list or element, need to call the object function.

695. Max Area of Island (Easy)
Questions: Is it allowed to change the value of the matrix?
TIPS: BSF or DFS. iteration over every element of the grid. If find 1, Put the current cell to the seen hash table, depth-first search over all the neighbours.
827. Making A Large Island
Start with 0s cell, DFS all the 1s in the grid. Keep the largest area.

1020. Number of Enclaves
TIPS: find elements surrounding by 0s. DFS return is surround by 0, and number of cells
class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m, n, ans = len(grid), len(grid[0]), 0

        def move(i, j, grid):
            if (i < 0 or j < 0 or i >= m or j >= n):
                return False, 0
            elif (grid[i][j] == 0):
                return True, 0
            grid[i][j] = 0
            a = move(i - 1, j, grid)
            b = move(i + 1, j, grid)
            c = move(i, j - 1, grid)
            d = move(i, j + 1, grid)
            return a[0] and b[0] and c[0] and d[0], 1 + a[1] + b[1] + c[1] + d[1]

        for i in range(m):
            for j in range(n):
                if (grid[i][j] == 1):
                    valid, count = move(i, j, grid)
                    if (valid):
                        ans += count

        return ans 


694. Number of Distinct Islands
TIPS: normal DFS search 1 element. The difference is keeping the relative position to the original cell. Adding all the relative positions all 1s to a tuple, the result will distinguish different shape of island.

547. Friend Circles (Medium)
TIPS: iteration over all the grids. If find 1, number + 1 and depth-first search all neighbours and set all the elements to *
547. Number of Provinces
TIPS: convert the connection to a hash table. DFS the hash table, and add the visited element to visited_dict. Iteration of the keys, if the current key is not in the visited_dict, number += 1, DFS current element, add visited element into the visited_dict. After finishing the DFS, continue to the next element.

417. Pacific Atlantic Water Flow (Medium)
Tips: adding a parameter of height to the DFS function. Need to add the visited set to the parameter as we need the visited set. Depth-first search from the left and top border and add all seen points in the Pacific set. Depth-first search from the right and bottom border and add all seen points in the Atlantic set.
The return is the intersection of the Pacific set and the Atlantic set. The trick is the need to add the cell height to the DFS function parameter. Also, need to pass the set() to the next DFS function. Because there are two set(), the Atlantic and Pacific set. In DFS not know which set the current position needs to be added to. So, add the set to the parameter is better.

323. Number of Connected Components in an Undirected Graph

399. Evaluate Division
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # ********
        graph = defaultdict(defaultdict)
 	# no need to remove the element from the visited. Each element need to be visited once
        def backtrack_evaluate(curr_node, target_node, acc_product, visited):
            visited.add(curr_node)
            ret = -1.0
            neighbors = graph[curr_node]
            if target_node in neighbors:
                ret = acc_product * neighbors[target_node]
            else:
                for neighbor, value in neighbors.items():
                    if neighbor in visited:
                        continue
                    ret = backtrack_evaluate(
                        neighbor, target_node, acc_product * value, visited)
                    if ret != -1.0:
                        break
            # visited.remove(curr_node) # does not need to remove current_node.
            return ret

        # Step 1). build the graph from the equations
        for (dividend, divisor), value in zip(equations, values):
            # add nodes and two edges into the graph
            graph[dividend][divisor] = value
            graph[divisor][dividend] = 1 / value

        # Step 2). Evaluate each query via backtracking (DFS)
        #  by verifying if there exists a path from dividend to divisor
        results = []
        for dividend, divisor in queries:
            if dividend not in graph or divisor not in graph:
                # case 1): either node does not exist
                ret = -1.0
            elif dividend == divisor:
                # case 2): origin and destination are the same node
                ret = 1.0
            else:
                visited = set()
                ret = backtrack_evaluate(dividend, divisor, 1, visited)
            results.append(ret)

        return results
Start, end, product, visited
Visited hash table: why it does not need to remove the current node? Because it is a feasible reachable question, if trying the current node, cannot reach the end, then the next iteration is not necessary to iterate the current node because it will not reach the object.
Return value: Need to return if find any solution.

282. Expression Add Operators
TIPS: DFS call the next number, the trick is the accumulative sum is adding all numbers, but if next number is / or *, the accumulative sum need to – the temporary sum. Need to think of 0 number and first number iteration.

class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        res = []
        ln = len(num)
        def dfs(i, path, cur_num, prevNum):
            if i == ln:
                if cur_num == target:
                    res.append(path)
                return

            for j in range(i, ln):
                # starting with zero?
                if j > i and num[i] == '0':
                    # need to process current number and break.
                    break
                sub_num = int(num[i:j + 1])

                # if cur index is 0 then simple add that number
                if i == 0:
                    dfs(j + 1, path + str(sub_num), cur_num + sub_num, sub_num)
                else:
                    dfs(j + 1, path + "+" + str(sub_num), cur_num + sub_num, sub_num)
                    dfs(j + 1, path + "-" + str(sub_num), cur_num - sub_num, - sub_num)
                    # need to keep the last multiply result.
                    dfs(j + 1, path + "*" + str(sub_num), cur_num - prevNum + prevNum * sub_num, prevNum * sub_num)

        dfs(0, "", 0, 0)
        return res


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
                ans = 0  
		# this need to be 0, not float("inf"), 
		# because if the condition is not meet, will return -inf.
                for ind in range(idx, l):
                    if nums[ind] > value:
                        ans = max(ans, 1 + dfs(ind + 1, nums[ind]))
 
                visited[(idx, value)] = ans 
		# add the current idx, value to hash table for later dfs use
                return ans

        return dfs(0, float('-inf'))
TIPS: DFS searching all the array, for every DFS recursive call, needs to pass the current index value, in order next selected element to be greater than the current value. Need to add the current index to the parameter, next value selection needs to be the next index. For each selection, select all possible elements, and recursive call the function, until to get the maximum length.
Another option is using monotonic stack. 
329. Longest Increasing Path in a Matrix
TIPS: for each element in the matrix, search all directions which are higher than the current element. Cache the dfs process could decrease the time complexity to 0(n). no need to keep visited cell, because it is searching the higher value cell.

1335. Minimum Difficulty of a Job Schedule  *****
This is typical to find the lowest or smallest combination.
Split the whole process into a subprocess. But which to split the array is unknown. DFS try to split every index and calculate the value. 
class Solution:
    def minDifficulty(self, jobs, d: int) -> int:
        @lru_cache()
        def dfs(i, d):
            if len(jobs) - i < d: return float('inf')
            if d == 0:
                if i < len(jobs):
                    return float('inf')
                else:
                    return 0
            curmax = float('-inf')
            res = float('inf')
            for j in range(i, len(jobs)):
                curmax = max(curmax, jobs[j])
                res = min(res, curmax + dfs(j + 1, d - 1))
            return res

        res = dfs(0, d)
        return res if res != math.inf else -1

compare the minimum days to complete the job (Binary search) and find the minimum difficulty to complete within D days (DFS).

1763. Longest Nice Substring 


class Solution:
    @lru_cache()
    def longestNiceSubstring(self, s: str) -> str:
        # Edge case
        if len(s) < 2:
            return ""

        nice = ""  # Store the longest nice substring
        for i in range(len(s)):
            # checking every character, upper case and lower case, if find one letter upper case or lower case is not
            # in the string, will split the string and recursive call left half and right half, find the maximum length
            # and return the maximum length
            if s[i].lower() in s and s[i].upper() in s:
                nice += s[i]
            else:
                leftPart = self.longestNiceSubstring(s[:i])
                rightPart = self.longestNiceSubstring(s[i + 1:])
                return leftPart if len(leftPart) >= len(rightPart) else rightPart
        return nice
Aside from the return value, it has two returns in the loop, if it has both lower case and upper case of every character, it will return the whole string, if not, recursively call the left part and right part of the string to get the maximum left part and maximum right part and return a maximum of left and right part.

841. Keys and Rooms
Dfs searching room 0, find the key, dfs searching all room which has keys in the current room, 

1395. Count Number of Teams
TIPS. Two-direction DFS. One is an increasing pattern; the other is a decreasing pattern.
Another version: select one element as middle index, count how many elements lower than middle value and how many elements higher than middle value. Left * right is increasing order. Wise versa. Count how many elements higher than middle value on the left and how many elements lower on the right. Left * right is decreasing order. Return sum of the increasing pattern and decreasing pattern

211. Design Add and Search Words Data Structure
TIPS: trie + DFS search. build the trie with hashtable.  DFS search the next index and cur pointer.
class WordDictionary:

    def __init__(self):
        self.word = {}

    def addWord(self, word: str) -> None:
        w = self.word
        for c in word:
            if c not in w:
                w[c] = {}
            w = w[c]
        w["$"] = {}

    def search(self, word: str) -> bool:
        cur = self.word
        def dfs(ind, cur):
            if ind == len(word):
                if "$" in cur:
                    return True
                else:
                    return False
            else:
                if word[ind] == ".":
                    for key in cur:
                        if dfs(ind + 1, cur[key]):
                            return True
                    return False
                else:
                    if word[ind] in cur:
                        return dfs(ind + 1, cur[word[ind]])
                    else:
                        return False

        return dfs(0, cur)

93. Restore IP Addresses
TIPS:
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:

        res = []
        if len(s) > 12:
            return res

        def dfs(i, dots, curip):
            if i == len(s) and dots == 4:
                res.append(curip[:-1])  # to remove the fourth dot - [:-1]
                return

            for j in range(i, min(i + 3, len(s))):
                if int(s[i:j + 1]) <= 255 and (i == j or s[i] != "0"):  # allow .0. but not allow .01.
                    dfs(j + 1, dots + 1, curip + s[i:j + 1] + ".")

        dfs(0, 0, "")
        return res

583. Delete Operation for Two Strings
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)
        @cache
        def calc(i, j):
            if i == n or j == m:
                return max(n - i, m - j)
            if word1[i] == word2[j]:
                return calc(i + 1, j + 1)
            else:
                return min(calc(i + 1, j), calc(i, j + 1)) + 1
        return calc(0, 0)

416. Partition Equal Subset Sum
TIPS: we can convert this problem into select elements whose sum is sum(nums)//2
class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        if sum(nums) % 2 == 1:
            return False

        @cache  # lru_cache is worse than cache
        def dfs(i, target):
            if target == 0:
                return True
            else:
                if i == len(nums):
                    return False
                else:
                    if dfs(i + 1, target - nums[i]) or dfs(i + 1, target):
                        return True
                return False

        return dfs(0, sum(nums) // 2)
	
698. Partition to K Equal Sum Subsets
TIPS: split a list into k equal sum subset. DFS for each subset. Keep used signal, used need to be a list. Because there may be duplicated elements. backtracking

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        # Calculate the sum of all numbers in the array
        nums_sum = sum(nums)
        # If the sum cannot be evenly divided by k, it is not possible
        if nums_sum % k != 0:
            return False

        # Calculate the target sum for each subset
        target_sum = nums_sum // k
        # Sort the array in descending order to optimize pruning
        nums.sort(reverse=True)
        # Keep track of which numbers have been used in subsets
        used = [False] * len(nums)

        # Depth-first search function to explore all possible subsets
        def dfs(sub_sets_count, cur_sum, start_index):
            # If we have found k subsets, it is a valid partition
            if sub_sets_count == k:
                return True
            # If the current subset sum matches the target sum, move to the next subset
            if cur_sum == target_sum:
                return dfs(sub_sets_count + 1, 0, 0)

            # Iterate through the remaining numbers in the array
            for i in range(start_index, len(nums)):
                # If the number has been used or adding it exceeds the target sum, skip it
                if used[i] or cur_sum + nums[i] > target_sum:
                    continue

                # Pruning step: if the current number is the same as the previous number
                # optional the previous number hasn't been used, skip the current number
                if i > start_index and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue

                # Mark the current number as used
                used[i] = True
                # Recursive call to explore the next number and update the subset sum
                if dfs(sub_sets_count, cur_sum + nums[i], i + 1):
                    return True
                # Undo the choice of using the current number and try the next number in the array
                used[i] = False

            # If no solution is found, return False
            return False

        # Start the depth-first search from the beginning of the array with an empty subset
        return dfs(0, 0, 0)

279. Perfect Squares
TIPS: DFS from 2 to n // 2. Pick one and recursively call this function with target – I * I, and tmp 
