"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

# where am I?
    # at some node on the stack
# what am I doing?
    # map each node to 
# what do I return?
    # the clones first node
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        clone = {}
        # dfs and add all copies to the hashmap
        visited = set([node])
        stack = [node]
        
        while stack:
            current = stack.pop()
            clone[current] = Node(current.val)

            for neighbor in current.neighbors:
                if neighbor not in visited:
                    stack.append(neighbor)
                    visited.add(neighbor)


        for original in clone:
            copy = clone[original]

            for neighbor in original.neighbors:
                copy.neighbors.append(clone[neighbor])
        return clone[node]

                

        
        