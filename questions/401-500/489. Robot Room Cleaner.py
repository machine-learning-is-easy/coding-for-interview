

class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        # up, right, down, left
        # the robot starts facing up
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        def go_back():
            # go back to the starting position and the original direction
            robot.turnRight()
            robot.turnRight()
            robot.move()
            robot.turnRight()
            robot.turnRight()

        def dfs(cell, d):
            # clean the current cell and mark it as visited
            # then try to explore the next 4 directions
            robot.clean()
            visited.add(cell)
            for i in range(4):
                new_d = (d + i) % 4
                new_cell = (cell[0] + directions[new_d][0], cell[1] + directions[new_d][1])
                if new_cell not in visited and robot.move():
                    dfs(new_cell, new_d)
                    go_back()   # go back to the original cell
                robot.turnRight() # turn right to explore the next direction

        visited = set()
        dfs((0, 0), 0)

# the time complexity is O(4^(n-m)), where n is the number of cells in the room and m is the number of obstacles. The robot will visit each cell exactly once. The total number of possible paths the robot can take is 4^(n-m). The robot will backtrack when it reaches a dead end, so the total number of paths is 4^(n-m). The time complexity is O(4^(n-m)).
# add explaination to above code
# The robot starts at an unknown location in the room that is guaranteed to be empty, and you do not have access to the grid,
# but you can move the robot using the given API Robot.

# key point is to use DFS to explore the room and backtrack to the original cell when the robot reaches a dead end.
# The robot will visit each cell exactly once. The total number of possible paths the robot can take is 4^(n-m).


class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        """
        :type robot: Robot
        :rtype: None
        """
        # up, right, down, left
        directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]

        def move_back(robot):
            robot.turnRight()
            robot.turnRight()
            robot.move()
            robot.turnRight()
            robot.turnRight()

        visited = set()

        def dfs(x, y, d=0):
            nonlocal visited
            nonlocal robot
            robot.clean()
            visited.add((x, y))
            for _ in range(1, 5):
                nxt_direction_idx = (_ + d) % 4
                new_x, new_y = x + directions[nxt_direction_idx][0], y + directions[nxt_direction_idx][1]
                if (new_x, new_y) not in visited and robot.move():
                    dfs(new_x, new_y, nxt_direction_idx + 1)
                    move_back(robot)
                robot.turnRight()

        dfs(0, 0, 0)
        return "Robot cleaned all rooms."


class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        """
        :type robot: Robot
        :rtype: None
        """
        # up, right, down, left
        # row, col
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)] # need to be right sequence
        visited = set()

        def move_back():
            robot.turnRight()
            robot.turnRight()
            robot.move()
            robot.turnRight()
            robot.turnRight()

        def backtracking(r: int, c: int, cur_dir: int):
            robot.clean()
            visited.add((r, c))
            for inc in range(4):
                next_dir = (cur_dir + inc) % 4
                dr, dc = directions[next_dir]
                if (r + dr, c + dc) not in visited and robot.move():
                    backtracking(r + dr, c + dc, next_dir)
                    move_back()
                robot.turnRight()  # need to turn right for the next direction

        backtracking(0, 0, 0)
        return "Robot cleaned all rooms."