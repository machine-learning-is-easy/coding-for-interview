
from collections import defaultdict

class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        changed_dict = defaultdict(int)
        for num in changed:
            changed_dict[num] += 1
        res = []
        changed.sort()

        for num in changed:
            if num in changed_dict and changed_dict[num] > 0:
                changed_dict[num] -= 1
                if 2 * num in changed_dict and changed_dict[2 * num] > 0:
                    res.append(num)
                    changed_dict[2 * num] -= 1

        if len(res) == len(changed) / 2:
            return res
        else:
            return []



changed = [1,3,4,2,6,8]
assert Solution().findOriginalArray(changed) == [1, 3, 4]