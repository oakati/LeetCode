class Solution(object):
    def bitwiseComplement(self, n):
        """
        :type n: int
        :rtype: int
        """
        n = [i for i in str(bin(n))][2:]
        for i in range(0, len(n)):
            if n[i] == "0":
                n[i] = "1"
            elif n[i] == "1":
                n[i] = "0"
        return int("".join(n), 2)