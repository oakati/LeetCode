class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        str_form = str(x)
        flag = True
        for i in range(len(str_form)):
            if str_form[i] != str_form[len(str_form)-1-i]:
                flag = False
        if flag == True:
            return True
        else:
            return False