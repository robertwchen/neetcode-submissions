class MinStack:
# Return:
# What exactly am I returning?
    # 
# Example:
# Tiny input + expected output by hand

# Brute:
# Dumb obvious way, even if slow

# Property:
# What special clue can improve brute force?
# sorted? BST? contiguous? frequency? top k? level order?

# Pattern:
# sliding window / stack / heap / binary search / DFS / BFS / DP / etc.

# State:
# What variables/data structures do I need?

# Invariant:
# What must stay true?

# Progress:
# What moves/changes each step?

# Update:
# When do I count/save/return answer?

    def __init__(self):
        self.stack = []
        self.min_stack = []


    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack:
            self.min_stack.append(val)
        else:
            self.min_stack.append(min(val, self.min_stack[-1]))
        return
        
    def pop(self) -> None:
        # pop minstack pop stack
        self.stack.pop()
        self.min_stack.pop()
        return
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min_stack[-1]

sol = MinStack()
sol.push(1)
print(sol.top())
sol.pop()
print(sol.min_stack)
print(sol.stack)
        
