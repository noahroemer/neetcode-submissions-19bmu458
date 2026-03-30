class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        index_num = {}

        for i, n in enumerate(nums):
            compliment = target - n

            if compliment in index_num:
                return [index_num[compliment], i]
            
            else:
                index_num[n] = i
        