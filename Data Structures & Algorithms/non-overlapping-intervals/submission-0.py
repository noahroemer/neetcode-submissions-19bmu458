class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: (x[0], x[1]))
        res = [intervals[0]]
 
        for interval in intervals[1:]:
            if interval[0] < res[-1][1]:
                res[-1][1] = min(interval[1], res[-1][1])
            else:
                res.append(interval)
        return len(intervals) - len(res)
