

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        sig_num = set()
        for item in nums:
            if item not in sig_num:
                sig_num.add(item)
            else:
                sig_num.remove(item)

        return sig_num.pop()