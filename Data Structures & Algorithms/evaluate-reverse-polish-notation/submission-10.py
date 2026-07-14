class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
# Return:
# What exactly am I returning?
    # the total

# Example:
# Tiny input + expected output by hand

# Brute:
# Dumb obvious way, even if slow

# Property:
# What special clue can improve brute force?
# sorted? BST? contiguous? frequency? top k? level order?
    # this has inside to out order of operations

# Pattern:
# sliding window / stack / heap / binary search / DFS / BFS / DP / etc.
    # stack

# State:
# What variables/data structures do I need?
    # stack, a operator function

# Invariant:
# What must stay true?
    # operations must be done with calculations


# Progress:
# What moves/changes each step?

# Update:
# When do I count/save/return answer?



            stack = []
            operators = {'+', '-', '*', '/'}

            for token in tokens: # loop throguh all elements

                if token in operators:# if is operator 
                    print(token)
                    print(stack)
                    val2 = stack.pop() # pop last 2 elements from stack
                    val1 = stack.pop() 

                    if token == '+':
                        result = val1 + val2   
                    elif token == '-':
                        result = val1 - val2
                    elif token == '*':
                        result = val1 * val2
                    elif token == '/':
                        result = int(val1 / val2)
                    stack.append(result)
                else:
                    stack.append(int(token))
            return stack[0]
                    # do operation
                    # push back to stack

                # push num to stack

        