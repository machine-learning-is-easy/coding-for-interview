

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        seen = set()

        for n in nums:
            if n in seen:
                seen.remove(n)
            else:
                seen.add(n)

        return [key for key in seen][0]