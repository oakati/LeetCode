class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        mylist = list(set(list1) & set(list2))
        myvals = []
        out = []
        for i in range(len(mylist)):
            myvals.append(list1.index(mylist[i])+list2.index(mylist[i]))
        minmyvals = min(myvals)
        for i in range(len(myvals)):
            if myvals[i] == minmyvals:
                out.append(mylist[i])
        return out
        
            
