class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Goal: Return different groups of cars, find where cars intersect at distance 10
            # goal: find convergences before distance 10
        # Store: set of positions of each car at each time and check if same: 
        # Valid:
        # Fix:
        # Answer:

        # calculate time to target for each car to get to target 
        # time to target = target - current position / speed
        # array stores [(pos, speed), (pos, speed), (pos, speed)]
                        #closest                      # furthest
        times = []
        for i,p in enumerate(position):
            s = speed[i]
            #ttt = target - p / speed[i]
            times.append((p, s))
        times.sort(reverse = True)
        print(times)

        # store current fleet arival time
        fleet_time = 0
        count = 0
        for p, s in times:
            current_time = (target - p) / s
            print(fleet_time, p, s)

            if current_time > fleet_time:
                fleet_time = current_time
                count += 1
            else:
                continue
        return count
            # if current time > fleet arrival time: 
                # fleet_arrival time = current_time
                # count += 1

            # else:
                #continue because no fleet is added


        