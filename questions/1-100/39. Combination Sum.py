
# need all the elements in the array to be positive, so that we can use the same element multiple times.
# need to sort the array to avoid duplicate combinations.
# if minimum elements, need to use backtracking to explore all the possible combinations. selet the element and explore the next element.
# from largest to smallest, if the element is larger than the target, skip the element.
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # **********
        results = []

        def backtrack(remain, comb, start):
            if remain == 0:
                # make a deep copy of the current combination
                results.append(list(comb))
                return
            elif remain < 0:
                # exceed the scope, stop exploration.
                return

            for i in range(start, len(candidates)):
                # add the number into the combination
                comb.append(candidates[i])
                # give the current number another chance, rather than moving on, allowing picking up the same element.
                # if does not picking up the same element, need to search i + 1 in the next loop
                backtrack(remain - candidates[i], comb, i) # if need different element, need i + 1 to call backtracking.
                # backtrack, remove the number from the combination
                comb.pop()

        backtrack(target, [], 0)

        return results

