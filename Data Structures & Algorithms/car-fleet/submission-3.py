class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
# Return:
# What exactly am I returning?
    # return the number of fleets 

# Example:
# Tiny input + expected output by hand

# Brute:
# Dumb obvious way, even if slow

# Property:
# What special clue can improve brute force?
# sorted? BST? contiguous? frequency? top k? level order?
    # prev cars only matter to car behind it it either catches up or doesn't

# Pattern:
# sliding window / stack / heap / binary search / DFS / BFS / DP / etc.

# State:
# What variables/data structures do I need?

# Invariant:
# What must stay true?

# Progress:
# What moves/changes each step?
    # the cars 

# Update:
# When do I count/save/return answer?
    # when all elements are done

        # fleet_arrival
        # arrival time [ 1, 2, 3, 4, 5 ]

        ttt = [0] * len(speed)
        for i,p in enumerate(position):
            t = (target - p) / speed[i]
            ttt[i] = (t, p)
        
        print(ttt)
        ttt.sort(key=lambda val:val[1])
        print(ttt)

        # convert list of positions into time of arival 
        fleet_arrival = ttt[-1][0]
        fleets = 1
        # initialize first position car
        for i in range(len(ttt) - 2, -1, -1):# loop through from end to beginning
            t, p = ttt[i]
            if t <= fleet_arrival: # if arrival time of prev > current:
                continue# fleet joins
            else: 
                fleets += 1
                fleet_arrival = ttt[i][0]
                # update fleet_arrival
        return fleets