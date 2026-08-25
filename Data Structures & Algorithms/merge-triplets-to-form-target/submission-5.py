class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
       # can we even perform the function
        f, s, t = 0, 0, 0
        for i in range(len(triplets)):
            if triplets[i][0] > target[0] or triplets[i][1] > target[1] or triplets[i][2] > target[2]:
                continue
            else:
                f = max(f, triplets[i][0])
                s = max(s, triplets[i][1])
                t = max(t, triplets[i][2])
            if f == target[0] and s == target[1] and t == target[2]:
                return True
        return False
        
