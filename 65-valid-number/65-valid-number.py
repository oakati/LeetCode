class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == "inf" or s == "-inf" or s == "+inf":
            return False
        elif s == "Infinity" or s == "-Infinity" or s == "+Infinity":
            return False
        try:
            a = float(s)
        except:
            return False
        else:
            return True