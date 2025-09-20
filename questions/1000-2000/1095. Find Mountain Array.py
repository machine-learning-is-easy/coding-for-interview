

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:

        # find the peak

        left = 0
        right = mountain_arr.length() - 1
        peak_ind = 0
        while left < right:
            mid = (left + right) // 2

            mid_val = mountain_arr.get(mid)
            mid_next_val = mountain_arr.get(mid + 1) # the while condition need to be left < right.

            if mid_val < mid_next_val:
                left = mid + 1
            elif mid_val > mid_next_val:
                right = mid

        print("peak index", left)
        # peak index is left index

        l_left = 0
        l_right = left

        r_left = left
        r_right = mountain_arr.length() - 1

        min_index = mountain_arr.length()

        while l_left <= l_right:
            mid = (l_left + l_right) // 2
            mid_val = mountain_arr.get(mid)
            if mid_val == target:
                min_index = min(min_index, mid)
                break
            else:
                if mid_val < target:
                    l_left = mid + 1
                elif mid_val > target:
                    l_right = mid - 1

        while r_left <= r_right:
            mid = (r_left + r_right) // 2
            mid_val = mountain_arr.get(mid)
            if mid_val == target:
                min_index = min(min_index, mid)
                break
            else:
                if mid_val < target:
                    r_right = mid - 1
                elif mid_val > target:
                    r_left = mid + 1

        if min_index == mountain_arr.length():
            return -1
        else:
            return min_index