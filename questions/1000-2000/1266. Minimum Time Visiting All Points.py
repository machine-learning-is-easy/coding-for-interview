

class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """

        def distance(point1, point2):
            x_distance = abs(point1[0] - point2[0])
            y_distance = abs(point1[1] - point2[1])

            return min(abs(y_distance - x_distance) + x_distance, abs(y_distance - x_distance) + y_distance)

        seconds = 0
        for index in range(len(points) - 1):
            seconds += distance(points[index], points[index + 1])
        return seconds