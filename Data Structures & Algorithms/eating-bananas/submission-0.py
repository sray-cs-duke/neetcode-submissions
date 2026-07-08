import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)

        for pile in piles:
            speed = (l + r) // 2
            hours += math.ceil(pile / speed)
            if hours == h:
                return speed
            elif hours < h:
                l = speed + 1
            else:
                r = speed - 1
            