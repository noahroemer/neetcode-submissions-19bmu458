class Solution:
    def maxArea(self, heights: List[int]) -> int:

        max_vol = 0
        l = 0
        r = len(heights) - 1

        while r > l:
            current_vol = (r-l) * min(heights[l], heights[r])
            if heights[r] > heights[l]:
                l+=1
            elif heights[r] <= heights[l]:
                r-=1
            max_vol = max(current_vol, max_vol)
        return max_vol
        