class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        total = 0
        max_total = float('-inf')

        for r in range(len(nums)):
            total += nums[r]
            max_total = max(max_total, total)
            if total < 0:
                total = 0
        return max_total