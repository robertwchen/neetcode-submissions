class Solution:
    def maxProfit(self, prices: List[int]) -> int:
    # Return:
    # What exactly am I returning?
        # max_profit, 


    # Example:
        #[10, 1, 5] -> buy $1 sell $5 profit $4


    # Brute:
    # Dumb obvious way, even if slow
        # look through every pair and find max difference p2 - p1

    # Property:
    # What special clue can improve brute force?
    # sorted? BST? contiguous? frequency? top k? level order?
        # profit is calculated from 2 points -> use 2 pointer

    # Pattern:
    # sliding window / stack / heap / binary search / DFS / BFS / DP / etc.
        # 2 pointer

    # State:
    # What variables/data structures do I need?
        # max_profit, current_profit, p1, p2

    # Invariant:
    # What must stay true?
        # p1 < p2, p2 < len, p1 < len, 

    # Progress:
    # What moves/changes each step?
        # p1 moves to p2 when p2 <= p1 (new minimum)
         

    # Update:
    # When do I count/save/return answer?

        p1 = 0
        p2 = 1
        max_profit = 0

        while p2 < len(prices):
            profit = prices[p2] - prices[p1]
            max_profit = max(profit, max_profit)

            # take max of current and max profit
            if prices[p2] <= prices[p1]:
                p1 = p2
            p2 += 1

        return max_profit

        