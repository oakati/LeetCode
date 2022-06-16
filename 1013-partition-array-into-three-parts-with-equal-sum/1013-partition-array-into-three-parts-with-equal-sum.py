class Solution(object):
    def canThreePartsEqualSum(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        total = sum(arr)
        p1 = 0
        p2 = 0
        p3 = total
        for j in range(1,len(arr)):
            p3 -= arr[j-1]
            p1 = 0
            p2 = total-p3
            if p2 != 2*p3:
                continue
            for i in range(j-1):
                p1 += arr[i]
                p2 -= arr[i]
                if p3 == p2:
                    if p3 == p1:
                        return True
        return False