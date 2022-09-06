class Solution(object):
    def countWords(self, words1, words2):
        """
        :type words1: List[str]
        :type words2: List[str]
        :rtype: int
        """
        counter = 0
        d_words1 = {}
        for i in words1:
            if not d_words1.has_key(i):
                d_words1[i] = 1
            else:
                d_words1[i] = d_words1[i] + 1
        d_words2 = {}
        for i in words2:
            if not d_words2.has_key(i):
                d_words2[i] = 1
            else:
                d_words2[i] = d_words2[i] + 1
        for i in d_words1.keys():
            if i in d_words2.keys() and d_words1[i] == 1 and d_words2[i] == 1:
                counter = counter + 1
        return counter