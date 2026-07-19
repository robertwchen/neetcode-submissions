# where am I
    # at some point in temperatures
# what am I doing
    # pushing on the stack if
# what do I return

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # push a day on stack
        result = [0] * len(temperatures)
        stack = [] # stores (i, temp)
        # look for a future day to resolve it
        for i, temperature in enumerate(temperatures):
            # check if stack and if current element resolves past element
            while stack and temperature > stack[-1][1]:
                prev_i, prev_temp = stack.pop()
                print(prev_temp)
                result[prev_i] = i - prev_i
            stack.append((i, temperature))
        return result
                # if it doesn then pop it and change val
            
            # push current element on the stack
            
        