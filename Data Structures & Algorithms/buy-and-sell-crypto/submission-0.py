class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        start = 0
        end = 1
        
        max_profit = 0
        while end < len(prices):
            if prices[start] > prices[end]:
                start = end
                end += 1
                continue
            profit = prices[end] - prices[start]
            max_profit = max(profit, max_profit)
            end += 1
        return max_profit
    
            
            
        