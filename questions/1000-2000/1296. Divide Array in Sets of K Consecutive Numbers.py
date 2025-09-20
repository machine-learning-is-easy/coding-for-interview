

class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        """
        m is the minimum value in the counter.
        """
        dict_a = Counter(nums)
        while dict_a:
            m = min(dict_a)
            for i in range(k):
                if m in dict_a:
                    """
                    if we can decrease the number of m in the counter, we decrease it. 
                    """
                    dict_a[m] -= 1
                    if dict_a[m] == 0:
                        del dict_a[m]
                else:
                    return False
                m = m + 1
        return True