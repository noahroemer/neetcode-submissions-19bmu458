import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        while r >= l:
            m = (r+l)//2
            n = 0

            for bananas in piles:
                n += math.ceil(bananas/m)

            if n > h:
                l = m + 1
            else:
                r = m - 1
        return l
