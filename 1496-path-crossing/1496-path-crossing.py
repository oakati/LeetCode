class Solution(object):
    def isPathCrossing(self, path):
        """
        :type path: str
        :rtype: bool
        """
        p_path = [[0,0]]
        pos = [0,0]
        for move in path:
            if move == "N":
                pos[0] = pos[0] + 1
            elif move == "S":
                pos[0] = pos[0] - 1
            elif move == "E":
                pos[1] = pos[1] + 1
            elif move == "W":
                pos[1] = pos[1] - 1
            if p_path.count(pos) != 0:
                return True
            p_path.append([pos[0], pos[1]])
        return False