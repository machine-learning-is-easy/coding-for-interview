27.	Backtracking
Questions:
Distinct value?
Allow select the same value multiple times?
Negative value?

Keynotes
1)	Backtracking by adding the visited position or letter to the seen hash table needs to be in the loop. While the DFS, adds the visited position can be at the beginning of the recursive function.
2)	Backtracking to get the path in a tree, like the Lowest common ancestor
3)	Backtracking work with a graph

39. combination sum
Questions: 
1.	allow selection of the same element multiple times or just select one time. If allowing selecting multiple times, the backtracking function needs iteration on the next index, 
2.	Are all the elements positive or can be negative? If can be negative, select the element multiple times, otherwise, it will loop the current value forever.

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # **********
        results = []

        def backtrack(remain, comb, start):
            if remain == 0:
                # make a deep copy of the current combination
                results.append(list(comb))
                return   # if negative numbers in the array, don’t return, continue searching

            elif remain < 0:
                # exceed the scope, stop exploration.
                return

            for i in range(start, len(candidates)):
                # add the number into the combination
                comb.append(candidates[i])
                # if allowing picking up the same element, searching from i in the next loop
                # if does not pick up the same element, need to search i + 1 in the next loop
                backtrack(remain - candidates[i], comb, i)
                # backtrack, remove the number from the combination
                comb.pop()

        backtrack(target, [], 0)

        return results

40. Combination of the sum
The difference to the 39 is the array has duplicate elements, so need to count the element numbers.

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        results = []. # container to hold the final combinations
        comb = []
        counter = Counter(candidates)
        # convert the counter table to a list of (num, count) tuples
        counter = [(c, counter[c]) for c in counter]

        def backtrack(remain, curr):
            if remain == 0:
                # make a deep copy of the current combination
                #   rather than keeping the reference.
                results.append(list(comb))
                return
            elif remain < 0:
                return

            for next_curr in range(curr, len(counter)):
                candidate, freq = counter[next_curr]

                if freq <= 0:
                    continue

                # add a new element to the current combination
                comb.append(candidate)
                counter[next_curr] = (candidate, freq-1)

                # continue the exploration with the updated combination
                backtrack(remain - candidate, next_curr)

                # backtrack the changes, so that we can try another candidate
                counter[next_curr] = (candidate, freq)
                comb.pop()

        
        backtrack(remain=target, curr=0)

        return results


77. Combinations
78. Subsets
77 and 78 are similar questions. We can use backtracking to solve it. 
TIPS: add index as a recursive function, for loop starts from the index.
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(first=0, curr=[]):
            # If the combination is done
            output.append(curr[:])
            for i in range(first, n):
                # add nums[i] into the current combination
                curr.append(nums[i])
                # use next integers to complete the combination
                backtrack(i + 1, curr)
                # backtrack
                curr.pop()

        output = []
        n = len(nums)
        backtrack()
        return output

140. Word Break II: 
Tips: backtracking over the word set list until the string is empty
46. Permutations (4Medium)
Tip: position is the parameter of backtracking. The current position can be any of the values after an equal current index. In a for loop, iteration over the position after the current position switches the value and continues the switch until the end of the list. After each switch, need to switch back the value. ALLOW SAME PERMUTATION(OR THE VALUE OF THE LIST IS DISTINCT)

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        def backtrack(first=0):
            # if all integers are used up
            if first == n:
                output.append(nums[:])
            for i in range(first, n):
                # place i-th integer first
                # in the current permutation
                nums[first], nums[i] = nums[i], nums[first]
                # use next integers to complete the permutations
                backtrack(first + 1)
                # backtrack
                nums[first], nums[i] = nums[i], nums[first]

        n = len(nums)
        output = []
        backtrack()
        return output
60. Permutation Sequence
The same with 46, just need to save the permutation and return if length of the return equal k.  
47. Permutations II
Tips: the difference is not allowed to duplicate value in a permutation (which means the value of the list can be duplicated, in the permutation does not include the same value change position). Of course, this algorithm also applies the 46. 47 add a condition to the backtracking loop
Tips: convert the list into a hash table. A combination list selects all possible values from the starting index of the list. the first index of the combination list is all the values in the list. then the second index of the combination list can be all the values after the current index (including the current index), iteration until the very end of the list.
 In the backtracking, when putting a number into the combination list, the value of the key decreases one until the value equals 0. Iteration over all the keys in the hash table until the combination list is filled up.
# The biggest difference with 46 is the iteration in 47 is the hash table key. But the iteration in 46 is on the value of the next component of the list. iteration over the key in the hash table eliminates the duplicate permutation. 
47 solutions also work to 46.
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        results = []
        def backtrack(comb, counter):
            if len(comb) == len(nums):
                # make a deep copy of the resulting permutation,
                # since the permutation would be backtracked later.
                results.append(list(comb))
                return

            for num in counter:
                if counter[num] > 0:
                    # add this number into the current combination
                    comb.append(num)
                    counter[num] -= 1
                    # continue the exploration
                    backtrack(comb, counter)
                    # revert the choice for the next exploration
                    comb.pop()
                    counter[num] += 1

        backtrack([], Counter(nums))

78. Subsets (similar with 46)
90. Subsets II (similar with 47)

77. Combinations (Medium)
Tips: similar to permutation, the only difference is adding a k which is less than the length of the list. stop criteria is the length of the combination list is equal to k
79. Word Search (Medium)
51. N-Queens (Hard)
Tips: add row and col into a hash table, converting check can be placed to check if the row or column in the list is 1. When removing the queen, assign the row, column and hill diagonals and dale diagonals value to 0. 
Backtracking parameter row number, for each row, add an iteration of column
class Solution:
    def solveNQueens(self, n: int) -> list:
        # **********
        def could_place(row, col):
            return not (cols[col] + hill_diag[row - col] + dale_diag[row + col])

        def place_queen(row, col):
            queen_pos.append([row, col])
            cols[col] = 1
            hill_diag[row - col] = 1
            dale_diag[row + col] = 1

        def remove_queen(row, col):
            queen_pos.remove([row, col])
            cols[col] = 0
            hill_diag[row - col] = 0
            dale_diag[row + col] = 0

        def add_solution():
            solution.append(["." * col + 'Q' + '.' * (n - 1 - col) for _, col in queen_pos])

        def backtrack(row=0):
            for c in range(n):
                if could_place(row, c):
                    place_queen(row, c)
                    if row == n - 1:
                        add_solution()
                    else:
                        backtrack(row + 1)

                    remove_queen(row, c)

        solution = []
        hill_diag = [0] * (2 * n - 1)  #
        dale_diag = [0] * (2 * n - 1)  #
        queen_pos = []
        cols = [0] * n
        backtrack()

        return solution

70. Climbing Stairs
719. Find K-th Smallest Pair Distance
TIPS: binary search:
Another version is using heap.

class Solution:
    def smallestDistancePair(self, nums, k: int) -> int:

        def check(dist: int) -> bool:

            i = j = cnt = 0

            for i in range(n):  # Use two ptrs to count pairs with
                while j < n and nums[j] - nums[i] <= dist:  # distance no greater than k
                    # count is treat j as center. look left, if nums[j] - num[i] <= dist, then nums[j] - nums[i+1] < dist.
                    # then the total count of pairs of distance less than dist is j - i
                    cnt += j - i
                    j += 1
            return cnt >= k  # return whether at least k such pairs exist

        nums.sort()
        n, left, right = len(nums), 0, nums[-1] - nums[0]

        while left < right:  # bin search

            mid = (left + right) // 2
            if check(mid):
                right = mid
            else:
                left = mid + 1

