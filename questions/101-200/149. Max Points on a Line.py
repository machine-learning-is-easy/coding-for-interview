

def maxPoints(points) -> int:
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    def max_points_on_a_line_containing_point_i(i):
        def slope_coprime(x1, y1, x2, y2):
            delta_x, delta_y = x1 - x2, y1 - y2
            if delta_x == 0:
                return (0, 0)
            elif delta_y == 0:
                return (sys.maxsize, sys.maxsize)
            elif delta_x < 0:
                delta_x, delta_y = - delta_x, - delta_y
            gcd_value = gcd(delta_x, delta_y)
            return (delta_x // gcd_value, delta_y // gcd_value)

        def add_line(i, j, count, duplicates):
            x1 = points[i][0]
            y1 = points[i][1]
            x2 = points[j][0]
            y2 = points[j][1]
            if x1 == x2 and y1 == y2:
                duplicates += 1
            elif y1 == y2:
                nonlocal horizontal_lines
                horizontal_lines += 1
                count = max(horizontal_lines, count)
            else:
                slope = slope_coprime(x1, y1, x2, y2)
                lines[slope] = lines.get(slope, 1) + 1
                count = max(lines[slope], count)
            return count, duplicates

        lines, horizontal_lines = {}, 1
        count = 1
        duplicates = 0
        for j in range(i + 1, n):
            count, duplicates = add_line(i, j, count, duplicates)
        return count + duplicates

    n = len(points)
    if n < 3:
        return n

    max_points = 1
    for i in range(n - 1):
        max_points = max(max_points, max_points_on_a_line_containing_point_i(i))
    return max_points

# simple solution using the slope and the intercept to find the maximum points on the same line.
class Solution:
    def maxPoints(self, points) -> int:
        #
        def max_points_on_a_line_containing_point_i(i):
            # Compute the slope and y-intercept of the line with other points
            def add_line(i, j, count, duplicates):
                # add a line passing through points[i] and points[j]
                x1 = points[i][0]
                y1 = points[i][1]
                x2 = points[j][0]
                y2 = points[j][1]
                # overlap points
                if x1 == x2 and y1 == y2:
                    # overlap points
                    duplicates += 1
                elif x1 == x2:
                    # vertical line
                    nonlocal horizontal_lines
                    horizontal_lines += 1
                    count = max(horizontal_lines, count)
                else:
                    slope = (y1 - y2) / (x1 - x2)
                    intercept = y1 - slope * x1
                    lines[(slope, intercept)] = lines.get((slope, intercept), 1) + 1
                    count = max(lines[(slope, intercept)], count)
                return count, duplicates

            lines, horizontal_lines = {}, 1
            count = 1
            duplicates = 0
            for j in range(i + 1, n):
                # add line passing through points[i] and points[j]
                count, duplicates = add_line(i, j, count, duplicates)
            return count + duplicates

        n = len(points)
        if n < 3:
            return n

        max_points = 1
        for i in range(n - 1):
            max_points = max(max_points, max_points_on_a_line_containing_point_i(i))
        return max_points

# add explainatio to above codes
# add time and space complexity
# add more test cases


class Solution:
    def maxPoints(self, points) -> int:
        def max_points_on_a_line_containing_point_i(i):
            nonlocal maximum_points
            def add_line(i, j):
                nonlocal lines
                x1 = points[i][0]
                y1 = points[i][1]
                x2 = points[j][0]
                y2 = points[j][1]
                max_count = 0
                duplicates = 0
                if x1 == x2 and y1 == y2:
                    duplicates += 1
                elif x1 == x2:
                    # vertical line
                    lines[x1] = lines.get(x1, 0) + 1
                    max_count = max(lines[x1], max_count)
                else:
                    slope = (y1 - y2) / (x1 - x2)
                    intercept = y1 - slope * x1
                    lines[(slope, intercept)] = lines.get((slope, intercept), 0) + 1
                    max_count = max(lines[(slope, intercept)], max_count)
                return max_count + duplicates

            lines = {}  # keep all the lines passing through point[i]
            for j in range(i + 1, n):
                current_point_lines = add_line(i, j)
                maximum_points = max(maximum_points, current_point_lines + 1)

        n = len(points)
        if n < 3:
            return n

        maximum_points = 1
        for i in range(n - 1):
            max_points_on_a_line_containing_point_i(i)
        return maximum_points
