class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        print(intervals)

        res = []
        curr = intervals[0]
        # the cases are  if the current intervals doesn't overlap with the next interval
        # the current interval does overlap with the next interval
        for i, interval in enumerate(intervals[1:]):
            if interval[0] <= curr[1]: #overlap
                print("ran")
                curr[1] = max(interval[1], curr[1])
            else:
                res.append(curr)
                curr = interval
        res.append(curr)
        return res
                


            
        