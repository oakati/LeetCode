class Solution(object):
    def minBitFlips(self, start, goal):
        """
        :type start: int
        :type goal: int
        :rtype: int
        """
        start = bin(start)[2:]
        goal = bin(goal)[2:]
        counter = 0
        
        if len(goal) > len(start):
            start = "0"*(len(goal)-len(start)) + start
        else:
            goal = "0"*(len(start)-len(goal)) + goal
        
        for i in range(0, len(goal)):
            if start[i] != goal[i]:
                counter = counter + 1
        return counter