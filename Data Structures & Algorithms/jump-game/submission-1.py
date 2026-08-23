class Solution:
    def canJump(self, nums: List[int]) -> bool:


        # Let's go backwards
        jump = 0
        target = len(nums) - 1

        for i in range(len(nums)-2, -1, -1):
            jump += 1
            if nums[i] >= jump:
                target -= jump
                jump = 0
            else:
                continue
        return target == 0
                
            
        
        