

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        point1 = m - 1
        point2 = n - 1
        pivot_index = m + n - 1
        while point2 >= 0 and point1 >= 0:
            if nums1[point1] > nums2[point2]:
                nums1[pivot_index] = nums1[point1]
                point1 -= 1
            else:
                nums1[pivot_index] = nums2[point2]
                point2 -= 1
            pivot_index -= 1

        while point2 >= 0:
            nums1[pivot_index] = nums2[point2]
            pivot_index -= 1
            point2 -= 1