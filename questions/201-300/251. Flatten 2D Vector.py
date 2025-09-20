

class Vector2D:

    def __init__(self, vec: List[List[int]]):
        self.r = 0  # the next element row
        self.c = 0  # next element col
        self.vec = vec

    def next(self) -> int:
        if self.hasNext():
            ans = self.vec[self.r][self.c]
            self.c += 1
            if self.c == len(self.vec[self.r]):
                self.r += 1
                self.c = 0
            return ans

    def hasNext(self) -> bool:
        while self.r < len(self.vec):
            if self.c < len(self.vec[self.r]):
                return True
            else:
                self.c = 0

            self.r += 1

        return False

# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(vec)
# param_1 = obj.next()
# param_2 = obj.hasNext()