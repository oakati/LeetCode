class Solution(object):
    def decrypt(self, code, k):
        """
        :type code: List[int]
        :type k: int
        :rtype: List[int]
        """
        temp_code = [0]*len(code)
        if k > 0:
            for i in range(0, len(code)):
                for j in range(1, k+1):
                    temp_code[i] = temp_code[i] + code[(i + j) % len(code)]
        elif k < 0:
            for i in range(0, len(code)):
                for j in range(-1, k-1, -1):
                    temp_code[i] = temp_code[i] + code[(i + j) % len(code)] 
        return temp_code