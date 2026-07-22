# where am I
    # at some point on the stairs
# what am I doing
    # deciding to take 1 or 2 steps after paying the cost
# what do I return
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        start_zero = self._minCostClimbingStairs(cost, 0, {})
        start_one = self._minCostClimbingStairs(cost, 1, {})
        return min(start_zero, start_one)


    def _minCostClimbingStairs(self, cost, i, memo): # returns minimum cost
        if i in memo:
            return memo[i]
        if i >= len(cost):
            return 0
        
        one_step = cost[i] + self._minCostClimbingStairs(cost, i + 1, memo)
        two_step = cost[i] + self._minCostClimbingStairs(cost, i + 2, memo)
        memo[i] = min(one_step, two_step)
        return memo[i]
        
        
        