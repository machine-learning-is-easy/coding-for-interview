
"""
question: 
normally, the number of elements are fixed? or not. 
Does the number are consecutive or not? 
the element is selected once or mutiple times
0 elements is in the list or not?
"""

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        numbers.sort()

        l, r = 0, len(numbers) - 1

        while l < r:
            if numbers[l] + numbers[r] > target:
                r -= 1
            elif numbers[l] + numbers[r] < target:
                l += 1
            else:
                return [l + 1, r + 1]