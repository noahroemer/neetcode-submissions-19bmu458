class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        max_profit = 0

        l, r = 0, 1

        while r < len(prices):
            if prices[l] > prices[r]:
                l = r
                
            curr = prices[r] - prices[l]
            r += 1
            max_profit = max(curr, max_profit)
        return max_profit