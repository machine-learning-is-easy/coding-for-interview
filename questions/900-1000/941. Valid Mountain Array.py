

class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        start, end, L = 0, len(arr) - 1, len(arr)

        while start < L-1 and arr[start] < arr[start+1]:
            start += 1
        while end > 0 and arr[end] < arr[end-1]:
            end -= 1
        # need at lease one element for start and at least one element for end
        return start == end and 0 < start and end < len(arr) - 1