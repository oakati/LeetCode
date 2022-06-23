class Solution(object):
    def countPrimeSetBits(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        def is_prime(n):
            if n == 1:
                return False
            for i in range(2,n):
                if (n%i) == 0:
                    return False
            return True
        counter = 0
        for i in range(left,right+1):
            a = str(bin(i))
            if is_prime(a[2:len(a)].count("1")):
                counter = counter + 1
        return counter