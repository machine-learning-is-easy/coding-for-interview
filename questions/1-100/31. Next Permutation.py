


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def swap(nums, i, j):
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp

        def reverse(nums, start):
            i = start
            j = len(nums) - 1
            while (i < j):
                swap(nums, i, j)
                i += 1
                j -= 1

        # find decreasing element
        i = len(nums) - 2
        # find the first decreasing section from end to beginning
        while (i >= 0 and nums[i] >= nums[i + 1]):
            i -= 1

        # i is the index before the decreasing section
        # from right to left, find the first index which value is greater than index i
        # and swap the value of index i and found index
        if (i >= 0):
            j = len(nums) - 1
            while (nums[j] <= nums[i]):
                j -= 1
            swap(nums, i, j)

        # reverse the decreasing session
        reverse(nums, i + 1)

"""
Intuition :
Understanding Permutations:

Permutations are arranged in lexicographical order based on their elements.
For a given permutation, the next permutation is the smallest permutation larger than the current one.
Key Insight:

Starting from the right, find the first position where the elements are not in descending order. This is the "breakpoint."
Swap the breakpoint with the smallest element larger than it, found to the right.
Reverse the subarray to the right of the breakpoint to get the smallest possible order.
Example Walkthrough:

( nums = [1,2,3] ): Breakpoint is 2. Swap 2 and 3, then reverse to get ( [1,3,2] ).
( nums = [3,2,1] ): Fully descending. Reverse the entire array to ( [1,2,3] ).
Algorithm :
Find the Breakpoint:

Traverse the array from right to left and find the first index ( i ) such that ( nums[i] < nums[i+1] ). This is the breakpoint.
If no such index exists, the array is in descending order; reverse it and return.
Find the Smallest Larger Element:

Starting from the rightmost element, find the smallest element larger than ( nums[i] ). Let this index be ( j ).
Swap:

Swap ( nums[i] ) and ( nums[j] ).
Reverse the Subarray:

Reverse the subarray to the right of ( i ) to get the smallest possible order.
"""
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n = len(nums)
        i = n - 2

        # Step 1: Find the breakpoint
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        if i >= 0:
            # Step 2: Find the smallest element larger than nums[i]
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1
            # Swap nums[i] and nums[j]
            nums[i], nums[j] = nums[j], nums[i]

        # Step 3: Reverse the subarray to the right of i
        nums[i + 1:] = reversed(nums[i + 1:])