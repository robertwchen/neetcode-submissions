# where am I
    # at some point on the ttt array
# what am I doing
    # loop through the ttt array and see if each car forms fleet by comparing it to fleet time
# what do I return
    # number of fleet


# [ (position, time to target)]
#
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        ttt = []
        for i,p in enumerate(position):
            s = speed[i]
            time_to_target = (target - p) / s
            ttt.append((p, time_to_target))

        ttt.sort(reverse=True)

        fleets = 0
        current_ttt = 0
        for p, time in ttt:
            if fleets == 0:
                current_ttt = time
                fleets += 1
            elif time <= current_ttt:
                continue
            else:
                fleets += 1
                current_ttt = time
        return fleets

        