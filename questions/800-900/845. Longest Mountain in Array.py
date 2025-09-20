

# solution 1, left and right directions
class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        l = len(arr)
        right_arr = [0] * l
        right_arr[-1] = 0
        left_arr = [0] * l
        left_arr[-1] = 0

        anchor = arr[-1]  # recored the start of contious increase order

        for ind in range(l - 2, -1, -1):
            if arr[ind] > arr[ind + 1]:
                right_arr[ind] = right_arr[ind + 1] + 1
            else:
                right_arr[ind] = 0

        for ind in range(1, l):
            if arr[ind] > arr[ind - 1]:
                left_arr[ind] = left_arr[ind - 1] + 1
            else:
                left_arr[ind] = 0
        max_len = 0
        for l, r in zip(left_arr, right_arr):
            if l == 0 and r == 0:
                continue
            else:
                max_len = max(max_len, l + r + 1)

        return max_len

# solution2, use dfs searching left and right
class Solution1:
    def longestMountain(self, arr: List[int]) -> int:

        def dfs(i, direction):
            if direction == 'l':
                if i == 0:
                    return 0

                if arr[i - 1] < arr[i]:
                    l = 1 + dfs(i - 1, direction)
                else:
                    l = 0
            else:
                if i == len(arr) - 1:
                    return 0

                if arr[i] > arr[i + 1]:
                    l = 1 + dfs(i + 1, direction)
                else:
                    l = 0
            return l

        maximum_len = 0
        for i in range(0, len(arr)):
            left_len = dfs(i, "l")
            right_len = dfs(i, "r")
            if left_len == 0 and right_len == 0:
                continue
            else:
                maximum_len = max(maximum_len, left_len + right_len + 1)
        return maximum_len
