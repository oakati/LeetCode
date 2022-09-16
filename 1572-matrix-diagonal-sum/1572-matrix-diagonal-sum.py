class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        counter = 0
        for i in range(0,len(mat)):
            for j in range(0, len(mat)):
                if i == j or i+j == len(mat)-1:
                    counter = counter + mat[i][j]
        return counter