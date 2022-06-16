class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        i = 0
        while i < len(s)-1:
            print("i = " + str(i))
            if s[i:i+2] == "IV":
                ans += 4
                print(s[i:i+2])
                i += 2
                continue
            elif s[i:i+2] == "IX":
                ans += 9
                print(s[i:i+2])
                i += 2
                continue
            elif s[i:i+2] == "XL":
                ans += 40
                print(s[i:i+2])
                i += 2
                continue
            elif s[i:i+2] == "XC":
                ans += 90
                print(s[i:i+2])
                i += 2
                continue
            elif s[i:i+2] == "CD":
                ans += 400
                print(s[i:i+2])
                i += 2
                continue
            elif s[i:i+2] == "CM":
                ans += 900
                print(s[i:i+2])
                i += 2
                continue
            elif s[i] == "I":
                ans += 1
                print(s[i])
                i += 1
                continue
            elif s[i] == "V":
                ans += 5
                print(s[i])
                i += 1
                continue
            elif s[i] == "X":
                ans += 10
                print(s[i])
                i += 1
                continue
            elif s[i] == "L":
                ans += 50
                print(s[i])
                i += 1
                continue
            elif s[i] == "C":
                ans += 100
                print(s[i])
                i += 1
                continue
            elif s[i] == "D":
                ans += 500
                print(s[i])
                i += 1
                continue
            elif s[i] == "M":
                ans += 1000
                print(s[i])
                i += 1
                continue            
        if i == len(s)-1:
            if s[i] == "I":
                ans += 1
                print(s[i])
            elif s[i] == "V":
                ans += 5
                print(s[i])
            elif s[i] == "X":
                ans += 10
                print(s[i])
            elif s[i] == "L":
                ans += 50
                print(s[i])
            elif s[i] == "C":
                ans += 100
                print(s[i])
            elif s[i] == "D":
                ans += 500
                print(s[i])
            elif s[i] == "M":
                ans += 1000
                print(s[i])
            
        return ans