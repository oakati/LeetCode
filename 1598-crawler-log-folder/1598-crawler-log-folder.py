class Solution(object):
    def minOperations(self, logs):
        """
        :type logs: List[str]
        :rtype: int
        """
        counter = 0
        for log in logs:
            if log == "../":
                counter = max(counter - 1,0)
            elif log != "./":
                counter = counter + 1
        return counter