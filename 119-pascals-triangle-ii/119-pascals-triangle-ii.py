class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        list2 = []
        for i in range(0,rowIndex+1):
            list1 = []
            for j in range(0,i+1):
                list1.append(math.factorial(i)/(math.factorial(j)*math.factorial(i-j)))
            list2.append(list1)
        return list2[-1]