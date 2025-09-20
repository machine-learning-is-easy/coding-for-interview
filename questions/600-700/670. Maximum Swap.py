

class Solution:
    def maximumSwap(self, num: int) -> int:

        s = list(str(num))
        maxIdx = [len(s) - 1] * len(s)
        curMax = 0
        for i in range(len(s) - 2, -1, -1):
            if s[i] > s[maxIdx[i + 1]]:
                maxIdx[i] = i
            else:
                maxIdx[i] = maxIdx[i + 1]
        for i in range(len(s)):
            if s[i] < s[maxIdx[i]]:  # swap
                s[i], s[maxIdx[i]] = s[maxIdx[i]], s[i]
                break
        return int(''.join(s))


class Solution:
    def maximumSwap(self, num: int) -> int:
        num_str = list(str(num))
        last_index = {int(digit): i for i, digit in enumerate(num_str)}  # Store the last occurrence of each digit

        for i, digit in enumerate(num_str):
            for d in range(9, int(digit), -1):  # Check for a larger digit
                if d in last_index and last_index[d] > i:
                    num_str[i], num_str[last_index[d]] = num_str[last_index[d]], num_str[i]  # Swap
                    return int("".join(num_str))  # Return the new number

num = 98368
assert Solution().maximumSwap(num) == 98863