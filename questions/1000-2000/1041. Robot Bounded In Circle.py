


class Solution:
    def isRobotBounded(self, instructions: str) -> bool:

        direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        xy = [0, 0]
        dir_ind = 0

        for _ in range(4):
            for ins in instructions:
                if ins == "G":
                    xy[0] = xy[0] + direction[dir_ind][0]
                    xy[1] = xy[1] + direction[dir_ind][1]
                elif ins == "L":
                    dir_ind = (dir_ind + 4 - 1) % 4
                elif ins == "R":
                    dir_ind = (dir_ind + 1) % 4
                else:
                    raise Exception("Not accept instruction")
            if xy == [0, 0]:
                return True

        return False