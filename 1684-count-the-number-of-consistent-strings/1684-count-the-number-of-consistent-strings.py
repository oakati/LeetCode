class Solution(object):
    def countConsistentStrings(self, allowed, words):
        """
        :type allowed: str
        :type words: List[str]
        :rtype: int
        """
        counter = 0
        for word in words:
            flag = True
            for ch in word:
                if ch not in allowed:
                    flag = False
                    break
            if flag == True:
                counter = counter + 1
        return counter