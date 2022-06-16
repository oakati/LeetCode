from Queue import LifoQueue
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
 
        stack = LifoQueue()
        for i in range(len(s)):
            if s[i] == "(":
                stack.put(")")
            elif s[i] == "[":
                stack.put("]")
            elif s[i] == "{":
                stack.put("}")
            elif stack.empty():
                return False
            else:
                if stack.get() == s[i]:
                    continue
                else:
                    return False
        if not stack.empty():
            return False
        return True
