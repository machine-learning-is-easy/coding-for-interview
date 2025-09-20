
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def compare(x, y):
            # x > y return 1. x < y return -1
            return -(int(str(x) + str(y)) - int(str(y) + str(x)))

        sorted_numbers = sorted(nums, key=cmp_to_key(compare))
        print(sorted_numbers)
        ans = ''.join(str(i) for i in sorted_numbers)
        return ans if ans[0] != '0' else '0'


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums_str = [str(x) for x in nums]

        def compare(a, b):
            if a + b > b + a:
                return -1
            elif a + b < b + a:
                return 1
            else:
                return 0

        nums_str.sort(key=cmp_to_key(compare))

        if nums_str[0] == '0':
            return '0'

        return ''.join(nums_str)
