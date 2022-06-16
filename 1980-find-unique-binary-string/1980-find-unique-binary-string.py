from random import randrange
class Solution(object):
    def findDifferentBinaryString(self, nums):
        """
        :type nums: List[str]
        :rtype: str
        """
        book = ["0","1"]
        while(1):
            out = ""
            for i in range(len(nums)):
                out += book[randrange(2)]
            if out not in nums:
                return out
