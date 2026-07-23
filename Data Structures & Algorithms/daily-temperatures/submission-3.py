# where am I
    # at some point on the temperatures array
# what am I doing
    # checking if thsi current day resolves a past day
# what do I return
    #


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        days = [0 for i in range(len(temperatures))]
        stack = [(temperatures[0], 0)]
        
        for i in range(1, len(temperatures)):
            while stack and temperatures[i] > stack[-1][0]:
                prev_temp, prev_i = stack.pop()
                days[prev_i] = i - prev_i

            stack.append((temperatures[i], i))
        return days