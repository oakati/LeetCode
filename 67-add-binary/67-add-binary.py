class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        out = bin(int(a, 2) + int(b,2))
        return out[2:]