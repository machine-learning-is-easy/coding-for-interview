"""

"""
import math
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # put nums1 and nums2 into

        def getLeft(nums, partition):
            if partition <= 0:
                return -math.inf
            elif partition >= len(nums):
                return math.inf
            return nums[partition - 1]

        def getRight(nums, partition):
            if partition >= len(nums):
                return math.inf
            elif partition <= 0:
                return -math.inf
            return nums[partition]

        n1 = len(nums1)
        n2 = len(nums2)

        if n1 < n2:
            return self.findMedianSortedArrays(nums2, nums1)

        # Binary Search Parameters(searching the shorter array)
        lo = 0
        hi = n1  # need to search from 0 to n1
        totalLength = n1 + n2

        while lo <= hi:
            partX = (lo + hi) // 2   # middle of array 1
            partY = (totalLength + 1) // 2 - partX  # Middle of array 2

            l1 = getLeft(nums1, partX)  # number on the left of the partition - array 1
            r1 = getRight(nums1, partX)  # number on the right of the partition - array 1

            l2 = getLeft(nums2, partY)  # number on the left of the partition - array 2
            r2 = getRight(nums2, partY)  # number on the right of the partition - array 2

            # if the number on the left in array 1 is lesser than the number of on the right
            # of array 2 and the number on the left in array 2 is less than the number on
            # the right in array 1 then the correct partitions are found.

            if l1 <= r2 and l2 <= r1:
                # if the resulting array has even no of elements.
                if totalLength % 2 == 0:
                    return (max(l1, l2) + min(r1, r2)) / 2.0

                # odd number of elements
                return max(l1, l2)

            # if left number in array 1 is higher than the right number in array 2.
            elif (l1 > r2):
                # move the higher end to the left
                hi = partX - 1

            # if left number in array 2 is higher than the right number in array 1.
            else:
                # move the lower end to the right
                lo = partX + 1

        # incorrect result
        return -1


assert Solution().findMedianSortedArrays([1, 2], [3, 4]) == 2.5