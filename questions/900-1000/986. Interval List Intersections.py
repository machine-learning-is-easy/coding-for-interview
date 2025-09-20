


class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        res = []

        ind1 = 0
        ind2 = 0

        while ind1 < len(firstList) and ind2 < len(secondList):
            if secondList[ind2][0] <= firstList[ind1][0] <= secondList[ind2][1] or \
                    firstList[ind1][0] <= secondList[ind2][0] <= firstList[ind1][1]:
                res.append((max(firstList[ind1][0], secondList[ind2][0]), min(firstList[ind1][1], secondList[ind2][1])))

            if firstList[ind1][1] < secondList[ind2][1]:
                ind1 += 1
            elif firstList[ind1][1] > secondList[ind2][1]:
                ind2 += 1
            else:
                ind1 += 1
                ind2 += 1
        return res