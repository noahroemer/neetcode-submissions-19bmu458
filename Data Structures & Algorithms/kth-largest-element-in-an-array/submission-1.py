import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # get a max heap
        nums = [-n for n in nums]
        heapq.heapify(nums)

        for i in range(k):
            if i+1 == k:
                return -(heapq.heappop(nums))
            else:
                heapq.heappop(nums)
        