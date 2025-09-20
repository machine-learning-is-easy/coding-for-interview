

class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        # Convert the list of obstacles to a set for O(1) lookup time
        obstacle_set = set(map(tuple, obstacles))

        # Directions: North, East, South, West (in terms of x, y changes)
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        # Initial position and direction (facing North)
        x, y = 0, 0
        direction_index = 0

        max_distance_squared = 0

        for command in commands:
            if command == -2:
                # Turn left (counterclockwise)
                direction_index = (direction_index - 1) % 4
            elif command == -1:
                # Turn right (clockwise)
                direction_index = (direction_index + 1) % 4
            else:
                # Move forward 'command' units
                for _ in range(command):
                    # Calculate next position
                    next_x = x + directions[direction_index][0]
                    next_y = y + directions[direction_index][1]

                    # Check if the next position is an obstacle
                    if (next_x, next_y) in obstacle_set:
                        # If there's an obstacle, stop moving in this direction
                        break

                    # Update position
                    x, y = next_x, next_y

                    # Calculate the square of the distance from the origin
                    max_distance_squared = max(max_distance_squared, x * x + y * y)

        return max_distance_squared