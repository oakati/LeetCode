class Solution(object):
    def findLUSlength(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        record = -1
        for i in range(len(a)):
            for j in range(i+1,len(a)+1):
                if a[i:j] not in b:
                    record = max(record,j-i)
        for i in range(len(b)):
            for j in range(i+1,len(b)+1):
                if b[i:j] not in a:
                    record = max(record,j-i)
        return record