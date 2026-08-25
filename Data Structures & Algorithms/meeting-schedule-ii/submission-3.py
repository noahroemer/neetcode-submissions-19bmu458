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
        # minimum nubmer of rooms
        # find the max number of meetings going on at the same time
        # think heap. we push the end time once we get to the stop time
        # and me track max length
        begin = []
        finish = []
        
        for interval in intervals:
            begin.append(interval.start)
            finish.append(interval.end)
        print(begin, finish)

        heapq.heapify(finish)
        heapq.heapify(begin)
        # we need to add a count once we hit a start, and then 
        # pop from heap wen our time = an end time
        # while loop bc maybe multiple have same end time
        time = -1
        count = 0
        maxcount = 0
        #remove from the count first, and then add if tie
        while finish:
            time += 1
            while finish and time == finish[0]:
                count -= 1
                heapq.heappop(finish)
            while begin and time == begin[0]: # while our current time = a start of a meeting
                count += 1
                heapq.heappop(begin)
            maxcount = max(maxcount, count)
        return maxcount            
            

            


       
        


        