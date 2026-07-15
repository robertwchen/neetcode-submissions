class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
# Return:
# What exactly am I returning?
    # a list 

# Example:
# Tiny input + expected output by hand

# Brute:
# Dumb obvious way, even if slow
    # loop through all elements
# Property:
# What special clue can improve brute force?
    # a greater future number solves past
# sorted? BST? contiguous? frequency? top k? level order?

# Pattern:
# sliding window / stack / heap / binary search / DFS / BFS / DP / etc.
    # stack 
# State:
# What variables/data structures do I need?
    # stack of current unresolved elements, results list
# Invariant:
# What must stay true?
    # stack must stay decreasing

# Progress:
# What moves/changes each step?


# Update:
# When do I count/save/return answer?
    # when all elements have been checked, last element can't be resolved
        # [ (0, 30), ]
        stack = [] # stores (value, index)
        result = [0] * len(temperatures)
        for i, t in enumerate(temperatures): # loop through each element
            while stack and stack[-1][1] < t: # if stack is not empty, check if current element resolves past days
                prev_i = stack.pop()[0] # if so pop it and calculate its values
                result[prev_i] = i - prev_i 

            stack.append((i, t)) # add current value to stack
        return result