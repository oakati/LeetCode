class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        out = ""
        for i in range(len(digits)):
            out += str(digits[i])
        return str(int(out)+1)