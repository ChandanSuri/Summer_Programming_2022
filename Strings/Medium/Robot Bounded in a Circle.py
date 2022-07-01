class Solution(object):
    def isRobotBounded(self, instructions):
        """
        :type instructions: str
        :rtype: bool
        """

        '''
        This signifies directions:
        0: North
        1: East
        2: South
        3: West
        '''
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        curr_direction = 0
        # Current Coordinates
        curr_x = curr_y = 0

        for instruction in instructions:
            if instruction == "G":
                curr_x += directions[curr_direction][0]
                curr_y += directions[curr_direction][1]
            elif instruction == "L":
                curr_direction = (curr_direction - 1) % 4
            elif instruction == "R":
                curr_direction = (curr_direction + 1) % 4

        return (curr_x == 0 and curr_y == 0) or curr_direction != 0
