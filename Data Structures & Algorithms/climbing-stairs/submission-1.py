# where am I
    # at some point on the stairs
# what am I doing
    # returning number of ways to get to stairs
# what do i Ireturn
    # number of way 

class Solution:
    def climbStairs(self, n: int) -> int:
        return self._climbingStairs(n, {})

    def _climbingStairs(self, n, memo):
        if n in memo:
            return memo[n]
        if n == 0:
            return 1
        if n < 0:
            return 0

        memo[n] = self._climbingStairs(n - 1, memo) + self._climbingStairs(n - 2, memo)
        return memo[n]
        