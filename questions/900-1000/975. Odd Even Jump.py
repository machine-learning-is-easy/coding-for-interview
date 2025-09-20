
class Solution:
    def oddEvenJumps(self, A) -> int:
        # could not understand **********
        n = len(A)
        move = [[None for _ in range(n)] for _ in range(2)]
        nums = [[A[i], i] for i in range(n)]
        nums.sort() # lowerest value first
        stack = []
        for _, i in nums:
            while stack and stack[-1] < i:
                move[0][stack.pop()] = i
            stack.append(i)
        nums.sort(key=lambda x: [-x[0], x[1]])  # highest value first
        stack = []
        for _, i in nums:
            while stack and stack[-1] < i:
                move[1][stack.pop()] = i
            stack.append(i)

        # @functools.lru_cache(None)
        def dp(pos, odd):
            if pos == n - 1: return True
            nextPos = move[odd][pos]
            if nextPos == None: return False
            return dp(nextPos, 1 - odd)

        res = 0
        for i in range(n - 1, -1, -1):
            if dp(i, 0):
                res += 1

        return res

arr = [5,1,3,4,2]
assert Solution().oddEvenJumps(arr) == 3