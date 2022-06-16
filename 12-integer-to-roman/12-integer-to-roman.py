class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        out = ""
        
        
        thousand = num/1000
        num -= thousand*1000
        for i in range(thousand):
            out = out + "M"
        hundred = num/100
        num -= hundred*100
        if hundred == 9:
            out = out + "CM"
        else:
            fivehundred = hundred/5
            hundred -= fivehundred*5
            for i in range(fivehundred):
                out = out + "D"
            if hundred == 4:
                out = out + "CD"
            else:
                for i in range(hundred):
                    out = out + "C"
        tens = num/10
        num -= tens*10
        if tens == 9:
            out = out + "XC"
        else:
            fivetens = tens/5
            tens -= fivetens*5
            for i in range(fivetens):
                out = out + "L"
            if tens == 4:
                out = out + "XL"
            else:
                for i in range(tens):
                    out = out + "X"
        print(tens)
        ones = num
        if ones == 9:
            out = out + "IX"
        else:
            fives = ones/5
            ones -= fives*5
            for i in range(fives):
                out = out + "V"
            if ones == 4:
                out = out + "IV"
            else:
                for i in range(ones):
                    out = out + "I"
        num -= ones*1
        return out