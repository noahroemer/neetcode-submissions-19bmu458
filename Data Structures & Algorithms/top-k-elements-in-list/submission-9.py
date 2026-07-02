class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # we need to find the k most frequent elements. 
        # first thing we need to do is count each element
        # then we have a list of lists, and they are indexed by counts of the numbers. 
        # so what I'm thinking is we have a dictionary. we loop through the keys and values
        
        lsts = [[] for _ in range(len(nums)+1)]
        dct = {}
        res = []

        for num in nums:
            dct[num] = dct.get(num, 0) + 1

        for key, v in dct.items():
            lsts[v].append(key)
        

        for i, n in reversed(list(enumerate(lsts))):
            for num in n:
                res.append(num)
                
            if len(res) == k: 
                break
            print(res)
        return res
                


   
        


        
