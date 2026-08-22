class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        curr = intervals[0]
        # the cases are  if the current intervals doesn't overlap with the next interval
        # the current interval does overlap with the next interval
        for interval in intervals[1:]:
            if interval[0] <= curr[1]: #overlap
                curr[1] = max(interval[1], curr[1])
            else:
                res.append(curr)
                curr = interval
        res.append(curr)
        return res
                


            
        