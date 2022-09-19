class Solution(object):
    def minNumberOfHours(self, initialEnergy, initialExperience, energy, experience):
        """
        :type initialEnergy: int
        :type initialExperience: int
        :type energy: List[int]
        :type experience: List[int]
        :rtype: int
        """
        counter = sum(energy) - initialEnergy + 1
        counter = max(counter, 0)
        for xp in experience:
            if initialExperience > xp:
                initialExperience = initialExperience + xp
            else:
                counter = counter + (xp - initialExperience + 1)
                initialExperience = initialExperience + (xp - initialExperience + 1) + xp
        return counter