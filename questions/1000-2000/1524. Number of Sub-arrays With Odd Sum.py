

class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        count = 0
        sum_dict = {0: 1, 1: 0} #
        total = 0
        for num in arr:
            total += num
            odd = total % 2
            if odd == 1:
                count += sum_dict.get(0, 0)
            else:
                count += sum_dict.get(1, 0)

            sum_dict[odd] += 1
            print(sum_dict)
        return count


from typing import List


def numOfSubarrays(arr: List[int]) -> int:
    MOD = 10 ** 9 + 7
    odd_count = 0
    even_count = 1  # at the start of the arry, the total is 0, 0 is even, so event start with 1
    prefix_sum = 0
    result = 0

    for num in arr:
        prefix_sum += num
        if prefix_sum % 2 == 0:
            result = (result + odd_count) % MOD
            even_count += 1
        else:
            result = (result + even_count) % MOD
            odd_count += 1

    return result


class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        count = 0
        sum_dict = {0: 1, 1: 0} # at starting point, the total is 0, 0 is even, so even start with 1
        total = 0
        for num in arr:
            total += num
            odd = total % 2
            if odd == 1:
                count += sum_dict.get(0, 0)
            else:
                count += sum_dict.get(1, 0)

            sum_dict[odd] += 1
            print(sum_dict)
        return count