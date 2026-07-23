# where am I

# what am I doing
# what do I return

# positions       [1 2 3 4 5]
# time to target. [5 10 25, 35]

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time_to_target = []
        for i in range(len(position)):
            time_left = (target - position[i]) / speed[i]
            time_to_target.append((time_left, position[i]))
        
        #time_to_target: [(1, 3)]
                        #ttt, position
        time_to_target.sort(key = lambda pair:pair[1], reverse=True)
        print(time_to_target)
        #[(3.0, 7), (3.0, 4), (4.5, 1), (10.0, 0)]
        fleet_count = 0
        fleet_ttt = 0
        for ttt, p in time_to_target:
            if ttt > fleet_ttt:
                fleet_count += 1
                fleet_ttt = ttt
        return fleet_count
            
            
