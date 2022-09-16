class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        pos = [0, 0]
        for move in moves:
            if move == "U":
                pos[0] = pos[0] + 1
            elif move == "D":
                pos[0] = pos[0] - 1
            elif move == "L":
                pos[1] = pos[1] + 1
            elif move == "R":
                pos[1] = pos[1] - 1
        return pos == [0, 0]