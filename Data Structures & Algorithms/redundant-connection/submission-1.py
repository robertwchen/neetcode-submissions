# where am I
    # at some point on the edge list
# what am I doing
    # doing the union and find operation union with union by size find with path comprpession
# what do I return
    # return the last one that is equal

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        roots = [i for i in range(0, n + 1)]
        sizes = [ 1 for i in range(0, n + 1)]
        print(roots)
        print(sizes)

        for edge in edges:
            node_a, node_b = edge
            if self.union(roots, sizes, node_a, node_b):
                return edge

    def union(self, roots, sizes, node_a, node_b):
        root_a = self.find(roots, node_a) 
        root_b = self.find(roots, node_b)

        if root_a == root_b:
            return True
        if sizes[root_a] > sizes[root_b]:
            roots[root_b] = root_a
            sizes[root_a] += sizes[root_b]
        
        else:
            roots[root_a] = root_b
            sizes[root_b] += sizes[root_a]
        return False

    def find(self, roots, node):
        if roots[node] == node:
            return node
        
        found = self.find(roots, roots[node])
        roots[node] = found
        return found

        