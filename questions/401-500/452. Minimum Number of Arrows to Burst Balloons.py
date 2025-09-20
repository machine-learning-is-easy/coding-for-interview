
class Solution:
    def findMinArrowShots(self, points) -> int:
        points.sort(key=lambda x: (x[1], x[0])) # need to be sorted by end
        total_arrow = 0
        ind = 0

        while ind < len(points):
            if ind < len(points) - 1:
                anchor = ind + 1
                while anchor < len(points):
                    if points[anchor][0] <= points[ind][1]:
                        anchor += 1
                    else:
                        break
                total_arrow += 1
                ind = anchor

            else:
                total_arrow += 1
                ind += 1

        return total_arrow

points = [[3,9],[7,12],[3,8],[6,8],[9,10],[2,9],[0,9],[3,9],[0,6],[2,8]]
assert Solution().findMinArrowShots(points) == 2