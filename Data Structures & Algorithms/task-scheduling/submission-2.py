import heapq
import queue
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        counts = Counter(tasks)
        jobs = [-cnt for cnt in counts.values()] # need a max heap
        heapq.heapify(jobs)

        q = deque()
        time = 0

        while jobs or q:
            time += 1
  # while we have a job who's turn it is or on waiting
            if jobs:  # if we have an job ready to be run
                top = 1 + heapq.heappop(jobs)  # pop the top value
                if top:
                    q.append([top, time + n]) # appending the top and the time it can be used next
            if q and time == q[0][1]:  
                heapq.heappush(jobs, q.popleft()[0])
        return time
        
        