


class Solution:

    def __init__(self, nums: List[int]):
        self.original = nums[:]  # Save the original copy
        self.array = nums[:]

    def reset(self) -> List[int]:
        self.array = self.original[:]  # Restore original
        return self.array

    def shuffle(self) -> List[int]:
        array = self.array[:]
        n = len(array)
        for i in range(n - 1, 0, -1):
            j = random.randint(0, i)
            array[i], array[j] = array[j], array[i]
        return array

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()