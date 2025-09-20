# array is sorted array or not matters. if sorted array, binary search the first element of the val,
# then remove all the elements of the val
# if not sorted array, loop all the element, if equal to val, remove it, otherwise, go next index
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        left, right = 0, len(nums) - 1

        while left <= right:
            if nums[right] == val:
                right -= 1
                continue
            else:
                if nums[left] != val:
                    left += 1
                    continue
                else:
                    nums[left], nums[right] = nums[right], nums[left]
                    left += 1
                    right -= 1

        return left
