

"""
need to ask if all the candidate positive, or can be negative
"""
class Solution:
    def combinationSum2(self, candidates, target: int):

        result = []
        candidates.sort()
        def backtrack(start, candidates, temp, target):

            if target == 0:
                result.append(list(temp))
                return

            for i in range(start, len(candidates)):
                # already traversed i - 1, if i and i-1 are the same, not necessary to traverse i
                # it require the array to be sorted.
                if i > start and (candidates[i] == candidates[i - 1]):
                    continue
                temp.append(candidates[i])

                if target - candidates[i] >= 0:
                    backtrack(i + 1, candidates, temp, target - candidates[i]) # need start from i + 1
                temp.pop()

        backtrack(0, candidates, [], target)
        return result

Solution().combinationSum2([10,1,2,7,6,1,5], 8)