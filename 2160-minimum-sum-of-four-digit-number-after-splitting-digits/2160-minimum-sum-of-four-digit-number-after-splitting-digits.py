class Solution(object):
    def minimumSum(self, num):
        """
        :type num: int
        :rtype: int
        """
        str1 = ""
        str2 = ""
        mystr = str(num)
        mylist = list(mystr)
        mylist.sort()
        i = 0
        while i < len(str(num)):
            str1 = str1 + mylist[i]
            i = i + 1
            if i < len(str(num)):
                str2 = str2 + mylist[i]
                i = i + 1
        return int(str1)+int(str2)
