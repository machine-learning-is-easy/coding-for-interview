
class Solution:
    def getHint(self, secret: str, guess: str) -> str:

        hits = '{}A{}B'
        bulls = 0
        cows = 0

        hash_table = {}

        for s in secret:
            if s in hash_table:
                hash_table[s] += 1
            else:
                hash_table[s] = 1

        for x, y in zip(secret, guess):
            if x == y:
                bulls += 1
                hash_table[y] -= 1

        for x, y in zip(secret, guess):
            if x != y and y in hash_table and hash_table[y] > 0:
                cows += 1
                hash_table[y] -= 1

        return hits.format(bulls, cows)

assert Solution().getHint("11", "10") == "1A0B"