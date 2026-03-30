class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        times = {}
        buckets = [[] for i in range(len(nums) + 1)]
        for num in nums:
            times[num] = times.get(num, 0) + 1
                
        for c, v in times.items():
            buckets[v].append(c)

        print(buckets)
        
        res = []
        for i in range(len(buckets) - 1, 0, -1):
            for j in buckets[i]:
                res.append(j)
            if len(res) == k:
                return res            
