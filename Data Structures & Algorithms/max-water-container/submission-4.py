class Solution:
    def maxArea(self, heights: List[int]) -> int:

        # we need to track the left and right pointer
        # we need to have max volume be tracked

        l, r = 0, len(heights) - 1
        max_vol = 0

        while r > l:
            



            # calculate 
            curr_vol = (r-l) * min(heights[l], heights[r])
            max_vol = max(max_vol, curr_vol)

            if heights[l] >= heights[r]:
                r -= 1
            elif heights[r] > heights[l]:
                l += 1
        
        return max_vol

