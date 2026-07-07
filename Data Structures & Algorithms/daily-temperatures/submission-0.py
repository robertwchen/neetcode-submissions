class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = [] # stores tuple (index, temperature)

        for i, t in enumerate(temperatures):

            while len(stack) > 0 and (t > stack[-1][1]):
                print(stack)
                prev_i, prev_t = stack.pop()
                
                i_difference = i - prev_i
                t_difference = t - prev_t
                result[prev_i] = i_difference

            stack.append((i, t))
        return result

        