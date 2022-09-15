class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        """
        :type items: List[List[str]]
        :type ruleKey: str
        :type ruleValue: str
        :rtype: int
        """
        counter = 0
        for item in items:
            if (ruleKey == "type" and ruleValue == item[0]) or (ruleKey == "color" and ruleValue == item[1]) or (ruleKey == "name" and ruleValue == item[2]):
                counter = counter + 1
        return counter