class Solution:
    def findMin(self, nums: List[int]) -> int:
        # it is rotatted, we mus find find minimum

        # find the middle, one side is ordered
         
        # how to know on right side, if first right < last right

        l, r = 0, len(nums) -1

        while r > l:
            mid = (l+r)//2

            if nums[r] < nums[mid]:
                l = mid + 1
            else:
                r = mid
        return nums[l]