import math
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # we need to calculate euclidian distance then heapify
        points = [(math.sqrt(x**2 + y**2), x, y) for x, y in points]

        heapq.heapify(points)

        res = []
        for _ in range(k):
            _, x, y = heapq.heappop(points)
            res.append([x, y])
        return res


        
        