class Solution(object):
    def validIPAddress(self, queryIP):
        """
        :type queryIP: str
        :rtype: str
        """
        flag4 = True
        flag6 = True
        for i in queryIP.split("."):
            if not (len(queryIP.split(".")) == 4 and i.isdigit() and int(i) <= 255 and int(i) >= 0 and str(int(i)) == i):
                flag4 = False
                break
        for i in queryIP.split(":"):
            try:
                temp = int(i,16)
            except:
                flag6 = False
                break
            if not (len(queryIP.split(":")) == 8 and len(i) >= 1 and len(i) <= 4):
                flag6 = False
                break
        if flag4 == True and flag6 == False:
            return "IPv4"
        elif flag4 == False and flag6 == True:
            return "IPv6"
        else:
            return "Neither"