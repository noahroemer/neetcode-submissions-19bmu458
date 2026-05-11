class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # to find the most k frequend elements we need to use a list within lists
        # make it have the value and have the index be the count. 
        # make a hashmap for this if necessary

        # I need to make a dictionary that counts how many times each letter appears
        # then return the most seen 

        arr = [[] for _ in range(len(nums)+1)]
        dct = {}
        for num in nums:
            dct[num] = dct.get(num, 0) + 1
        for key, v in dct.items():
            arr[v].append(key)

        res = []
        for i in range(len(arr) - 1, 0, -1):
            for num in arr[i]:
                res.append(num)
                if len(res) == k:
                    return res
       
            


   
        


        
