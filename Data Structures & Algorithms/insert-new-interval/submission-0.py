class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        # what are the cases
        # the new interval comes before the old one
        # the new interval comes after the old one
        # the new interval overlaps with the initerval

        res = []
        added = 1
        
        for i, interval in enumerate(intervals):
            if newInterval[1] < interval[0]:
                res.append(newInterval)
                return res + intervals[i:]# this means the whole new comes before
                continue #?
            elif newInterval[0] > interval[1]: # check if new interval is after
                res.append(interval)
                continue 
            
            elif newInterval[0] <= interval[1] or newInterval[1] <= interval[0]:
                newInterval[0] = min(newInterval[0], interval[0])
                newInterval[1] = max(newInterval[1], interval[1])
        res.append(newInterval)
        return res

        

        