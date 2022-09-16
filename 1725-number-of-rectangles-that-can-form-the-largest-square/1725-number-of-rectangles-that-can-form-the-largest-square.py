from statistics import mode
class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        a = max([min(i) for i in rectangles])
        counter = 0
        for i in rectangles:
            if a <= i[0] and a <= i[1]:
                counter = counter + 1
        return counter