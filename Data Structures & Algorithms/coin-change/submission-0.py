# where am I  
    # at some point on coins
# what am I doing
    # finding minimum coins 
# what do I return

# options -> take current couin or take next coin

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        min_coins = self._coinChange(coins, amount, 0, {})
        if min_coins == float('inf'):
            return -1
        return min_coins
    

    def _coinChange(self, coins, amount, i, memo):
        key = (i, amount)
        if key in memo:
            return memo[key]
        if i == len(coins):
            return float('inf')

        if amount < 0:
            return float('inf')
        
        if amount == 0:
            return 0
        
        take_current = 1 + self._coinChange(coins, amount - coins[i], i, memo)
        skip_current = self._coinChange(coins, amount, i + 1, memo)
        memo[key] = min(take_current, skip_current)
        return memo[key]