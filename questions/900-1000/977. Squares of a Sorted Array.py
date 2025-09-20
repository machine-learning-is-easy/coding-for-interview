

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        output = [0] * len(nums)

        start = 0
        end = len(nums) - 1
        output_pointer = len(nums) - 1

        while start <= end:
            if nums[start] ** 2 > nums[end] ** 2:
                output[output_pointer] = nums[start] ** 2
                start += 1
                output_pointer -= 1
            else:
                output[output_pointer] = nums[end] ** 2
                output_pointer -= 1
                end -= 1
        return output