class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        # We know that one side will be sorted
        # We must check it's in the sorted side

        while r >= l:
            m = (r+l)//2
            if target == nums[m]:
                return m
            
            # Left side is sorted
            if nums[l] <= nums[m]:
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            # Right side is sorted
            else:
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1


            
        return -1

        
       
            


        


        