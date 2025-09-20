
class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        x_axis = defaultdict(dict)
        y_axis = defaultdict(dict)
        d = {}
        points.sort()

        ans = float('inf')

        for point in points:
            x_axis[point[0]][point[1]] = True
            y_axis[point[1]][point[0]] = True
            d[(point[0], point[1])] = True

        for point in points:
            x1 = point[0]
            y1 = point[1]
            for y2 in x_axis[x1]:
                if y2 == y1: continue
                for x2 in y_axis[y2]:
                    if x2 == x1: continue
                    if (x2, y1) in d:
                        tmp = abs(x2 - x1) * abs(y2 - y1)
                        if tmp < ans: ans = tmp
        return ans if ans != float('inf') else 0