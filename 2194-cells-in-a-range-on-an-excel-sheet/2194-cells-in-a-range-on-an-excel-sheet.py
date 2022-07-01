class Solution(object):
    def cellsInRange(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        w1 = s[0]
        n1 = s[1]
        w2 = s[3]
        n2 = s[4]
        mylist = []
        for i in range(ord(w1),ord(w2)+1):
            for j in range(int(n1),int(n2)+1):
                mylist.append(chr(i) + str(j))
        return mylist