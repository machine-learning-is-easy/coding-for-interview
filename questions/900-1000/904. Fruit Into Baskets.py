

from collections import defaultdict


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        fruitdict = defaultdict(int)

        end = 0
        start = 0
        m_len = 0
        while end < len(fruits):
            fruitdict[fruits[end]] += 1

            while len(fruitdict) > 2:
                fruitdict[fruits[start]] -= 1
                if fruitdict[fruits[start]] == 0:
                    del fruitdict[fruits[start]]
                start += 1

            m_len = max(m_len, end - start + 1)
            end += 1
        return m_len

fruits = [3,3,3,1,2,1,1,2,3,3,4]

assert Solution().totalFruit(fruits) == 5