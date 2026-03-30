class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        l, r = 1, max(piles)
        res = r
        

        while r >= l:
            m = (r+l) // 2
            time = 0
            for i in range(len(piles)):
                time += math.ceil(float(piles[i])/m)
            if time <= h:
                res = m
                r = m - 1
            elif time > h:
                l = m + 1
        return res
                


                
        
