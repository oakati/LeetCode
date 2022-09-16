class Solution(object):
    def maxPower(self, s):
        """
        :type s: str
        :rtype: int
        """
        counter = 1
        record = 1
        for i in range(0, len(s)-1):
            if s[i] == s[i+1]:
                counter = counter + 1
                record = max(counter, record)
            else:
                counter = 1
        return record