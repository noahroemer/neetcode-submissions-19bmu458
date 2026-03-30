class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        numSet = set(nums)
        
        best = 0
        for num in nums:
            if (num - 1) not in numSet:
                curr = 1
                while (num + curr) in numSet:
                    curr +=1
                best = max(curr, best)
        return best                

            