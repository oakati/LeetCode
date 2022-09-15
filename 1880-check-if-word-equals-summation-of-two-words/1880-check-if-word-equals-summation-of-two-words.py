class Solution(object):
    def isSumEqual(self, firstWord, secondWord, targetWord):
        """
        :type firstWord: str
        :type secondWord: str
        :type targetWord: str
        :rtype: bool
        """
        return int("".join([str(ord(i)-97) for i in firstWord])) + int("".join([str(ord(i)-97) for i in secondWord])) == int("".join([str(ord(i)-97) for i in targetWord]))