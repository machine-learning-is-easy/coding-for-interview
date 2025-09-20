

class Solution:
    def findStrobogrammatic(self, n: int):
        mapping = {
            '0': '0',
            '1': '1',
            '6': '9',
            '8': '8',
            '9': '6',
        }

        def dfs(nums, count, n):
            if count == n:
                return nums
            new_nums = []
            for dig1, dig2 in mapping.items():
                if count == n - 2 and dig1 == '0':
                    continue
                for num in nums:
                    new_nums.append(dig1 + num + dig2)

            return dfs(new_nums, count + 2, n)

        if n % 2 == 1:
            return dfs(["0", "1", "8"], 1, n)
        else:
            return dfs([""], 0, n)

n = 2

print(Solution().findStrobogrammatic(4))