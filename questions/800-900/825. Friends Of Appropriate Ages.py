
class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        count = {}
        for age in ages:
            if age not in count:
                count[age] = 0
            count[age] += 1

        res = 0
        for ageA, f_a in count.items():
            for ageB, f_b in count.items():
                if 0.5 * ageA + 7 >= ageB:
                    continue
                if ageA < ageB:
                    continue
                if ageA < 100 < ageB:
                    continue

                res += f_a * f_b
                if ageA == ageB:
                    res -= f_a
        return res
