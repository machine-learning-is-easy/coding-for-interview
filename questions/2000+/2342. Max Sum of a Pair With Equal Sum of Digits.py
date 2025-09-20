
class Solution:
    def maximumSum(self, nums: List[int]) -> int:

        digit_sum_dict = collections.defaultdict(list)

        maximum = -1
        for num in nums:
            key = sum([int(d) for d in str(num)])

            if digit_sum_dict.get(key, []):
                maximum = max(maximum, max(digit_sum_dict[key]) + num)
                digit_sum_dict[key].append(num)
            else:
                digit_sum_dict[key].append(num)

        return maximum