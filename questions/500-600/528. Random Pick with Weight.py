

# need to ask if all the elements are in positive. otherwise it will not work
class Solution:
    def __init__(self, w: List[int]):
        self.array = []
        self.SUM = sum(w)
        self.LENGTH = len(w)
        self.PERCENT = 100

        for idx, weight in enumerate(w):
            frequency = math.ceil(weight * self.PERCENT / self.SUM)
            self.array += [idx] * frequency

        print("length of array", len(self.array))

    def pickIndex(self) -> int:
        return self.array[random.randrange(len(self.array))]


class Solution:

    def __init__(self, w: List[int]):
        self.running_sums = []
        running_sum = 0

        for weight in w:
            running_sum += weight
            self.running_sums.append(running_sum)

        self.total_sum = running_sum

    def pickIndex(self) -> int:
        target = random.randint(1, self.total_sum)
        low, high = 0, len(self.running_sums)

        while low < high:
            mid = low + (high - low) // 2
            if target > self.running_sums[mid]:
                low = mid + 1
            else:
                high = mid

        return low

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()