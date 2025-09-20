

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(first=0, curr=[]):
            # if the combination is done
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
# time complexity: O(N * 2^N)



class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def create_subset(i):
            if i == len(nums):
                res.append(subset[:])
                return

            subset.append(nums[i])
            create_subset(i + 1)

            subset.pop()
            create_subset(i + 1)

        create_subset(0)
        return res


# time complexity is O(2^n) as we are generating all possible subsets
# each element has 2 possibilities have it or not.

