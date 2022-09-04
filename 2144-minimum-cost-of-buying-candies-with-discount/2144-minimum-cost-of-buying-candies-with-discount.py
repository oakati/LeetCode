class Solution(object):
    def minimumCost(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        cost.sort(reverse=True)
        m_sum = 0
        for i in range(0,len(cost)):
            if i % 3 != 2:
                m_sum += cost[i]
        return m_sum