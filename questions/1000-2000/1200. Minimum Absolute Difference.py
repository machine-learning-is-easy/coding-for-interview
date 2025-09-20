

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()

        res = []

        min_dif = float("inf")

        for ind in range(1, len(arr)):
            current_diff = arr[ind] - arr[ind - 1]
            if current_diff < min_dif:
                res = [[arr[ind - 1], arr[ind]]]
                min_dif = current_diff
            elif current_diff == min_dif:
                res.append([arr[ind - 1], arr[ind]])
        return res