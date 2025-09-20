

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        results = []
        comb = []
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

        results = []  # container to hold the final combinations
        counter = Counter(candidates)
        # convert the counter table to a list of (num, count) tuples
        counter = [(c, counter[c]) for c in counter]

        backtrack(remain=target, curr=0)

        return results


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        results = []
        candidates.sort()

        def backtracking(start, path, remaining):
            if remaining == 0:
                results.append(path[:])
                return
            for i in range(start, len(candidates)):
                # Skip duplicates at the same recursive level
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                if candidates[i] > remaining:
                    break  # No need to continue if the number is too large
                path.append(candidates[i])
                backtracking(i + 1, path, remaining - candidates[i])
                path.pop()

        backtracking(0, [], target)
        return results