

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        friends = [ind + 1 for ind in range(n)]
        ind = 0
        while len(friends) > 1:
            # count k
            for _ in range(1, k):
                ind += 1
            ind = ind % len(friends)
            friends.pop(ind)
        return friends[0]