
class Solution:
    def minDays(self, bloomDay, m: int, k: int) -> int:
        def ispossible(bloomDay, m, k, day):
            possible_arr = [r <= day for r in bloomDay]
            count_k = 0
            count_m = 0
            ind = 0
            while ind < len(possible_arr):
                if possible_arr[ind] == True:
                    count_k += 1
                    if count_k == k:
                        count_m += 1
                        count_k = 0
                else:
                    count_k = 0

                ind += 1
            return count_m >= m

        if len(bloomDay) < m * k:
            return -1
        else:
            left = 1
            right = max(bloomDay)

            while left <= right:
                mid = (left + right) // 2

                if ispossible(bloomDay, m, k, mid):
                    right = mid - 1
                else:
                    left = mid + 1

            return left


bloomDay = [1,10,3,10,2]
m = 3
k = 1

assert Solution().minDays(bloomDay, m, k) == 3