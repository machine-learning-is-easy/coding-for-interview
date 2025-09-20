

class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        subsequence = []
        for n in nums:
            if len(subsequence) % 2 == 0:  # even turn, now current value must be bigger than the last value in stack
                if subsequence and subsequence[-1] > n:
                    subsequence.pop()
            else:  # is odds turn, new value must be smaller than the last value of stack
                if subsequence and subsequence[-1] < n:
                    subsequence.pop()
            subsequence.append(n)

        if len(subsequence) % 2 == 0: # make the length of subsequence to even
            subsequence.pop()

        res = 0
        sign = 1
        for v in subsequence:
            res += sign*v
            sign = -sign

        return res