class Solution(object):
    def rearrangeCharacters(self, s, target):
        """
        :type s: str
        :type target: str
        :rtype: int
        """
        record = len(s)
        
        for i in set(target):
            record = min(record, s.count(i)/target.count(i))
        return record