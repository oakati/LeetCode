class Solution(object):
    def isPrefixOfWord(self, sentence, searchWord):
        """
        :type sentence: str
        :type searchWord: str
        :rtype: int
        """
        mylist = sentence.split(" ")
        for i in range(len(mylist)):
            for j in range(1,len(mylist[i])+1):
                if mylist[i][:j] == searchWord:
                    return i+1
        return -1
                