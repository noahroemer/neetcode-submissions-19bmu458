class Solution:
    def maxArea(self, heights: List[int]) -> int:

        l, r = 0, len(heights) - 1
        max_vol = 0

        while r > l:
            current_vol = min(heights[l], heights[r]) * (r-l)
            max_vol = max(current_vol, max_vol)

            if (heights[l] <= heights[r]):
                l += 1
            elif (heights[l] > heights[r]):
                r -= 1
            
        return max_vol


        