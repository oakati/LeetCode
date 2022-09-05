class Solution(object):
    def maxScore(self, s):
        """
        :type s: str
        :rtype: int
        """
        record = 0
        for i in range(1,len(s)):
            record = max(record,s[0:i].count('0')+s[i:len(s)].count('1'))
        return record
            
            