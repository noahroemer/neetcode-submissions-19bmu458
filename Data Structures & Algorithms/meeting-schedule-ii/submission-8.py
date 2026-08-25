"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # another solution is going through the start and end times and if end  is less than start, remove from rooms
        # here we need to sort at the start
        begin = sorted([interval.start for interval in intervals])
        finish = sorted([interval.end for interval in intervals])

        rooms, maxrooms = 0, 0
        s, e = 0, 0
        
        while s < len(begin):
            if begin[s] < finish[e]:
                rooms += 1
                s += 1
            else:
                rooms -= 1
                e += 1
            maxrooms = max(maxrooms, rooms)
        return maxrooms
        
            

            

            


       
        


        