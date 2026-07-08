import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        hours = 0
        for pile in piles:
            speed = (l + r) // 2
            hours += math.ceil(pile / speed)
            if hours <= h:
                return speed
            else:
                l = speed + 1