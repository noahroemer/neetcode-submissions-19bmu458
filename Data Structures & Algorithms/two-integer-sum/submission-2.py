class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # we nee to track indices
        # we should track current indices via enumerate, and track pass indices and 
        # values by using a hashmap

        prev_map = {}

        for i, n in enumerate(nums):
            comp = target - n
            if comp in prev_map:
                return [prev_map[comp], i]

            prev_map[n] = i

        
      
                
        
      
        