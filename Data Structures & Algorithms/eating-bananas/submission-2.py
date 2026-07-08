import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        ans = r

        while l <= r:
            hours = 0
            speed = (l + r) // 2
            for pile in piles:
                hours += math.ceil(pile / speed)
            if hours <= h:
                ans = speed
                r = speed - 1
            else:
                l = speed + 1
        return ans