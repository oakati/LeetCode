class Solution(object):
    def reorderSpaces(self, text):
        """
        :type text: str
        :rtype: str
        """
        out = ""
        textcopy = text
        mylist = textcopy.split()
        mycount = text.count(" ")
        if mycount == 0:
            return text
        if (len(mylist)-1) == 0:
            text = strip(text)
            text += " "*mycount
            return text
        partition = mycount/(len(mylist)-1)
        rem = mycount - partition*(len(mylist)-1)
        for i in range(len(mylist)-1):
            out += mylist[i] + " "*partition
        out += mylist[len(mylist)-1] + " "*rem
        return out