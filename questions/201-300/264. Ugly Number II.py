

from sortedcontainers import SortedSet

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        s=SortedSet()
        s.add(1)

        for i in range(n+1):
            val=s[i]
            s.add(val*2)
            s.add(val*3)
            s.add(val*5)
        return s[n-1]