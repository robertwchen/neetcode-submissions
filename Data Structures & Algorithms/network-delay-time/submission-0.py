# where am I
    # at current lowest cost in graph
# what am I doing
    # updating children weights then marking as visited
# what do I return
    # the smallest in the table 

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        visited = set()
        graph = self.build_graph(n, times)
        costs = {i: float('inf') for i in range(1, n + 1)} # {1:inf ....n:inf}
        costs[k] = 0

        min_heap = [(0, k)]
        
        max_time = 0
        while min_heap:
            current_time, node = heapq.heappop(min_heap) # starts at 0
            if node in visited:
                continue
            visited.add(node)
            max_time = max(max_time, current_time)
            
            for neighbor in graph[node]:
                new_time = graph[node][neighbor]
                costs[neighbor] = min(costs[neighbor], new_time + current_time)
                heapq.heappush(min_heap, (costs[neighbor], neighbor))
            # add weights to children and add it to the stack
            # if children in visited: continue

        if len(visited) != n:
            return -1
        return max_time


    def build_graph(self, n, times):
        graph = {}
        for i in range(1, n + 1):
            graph[i] = {}
        
        for time in times:
            a, b, t = time
            graph[a][b] = t
        return graph

        
        




        

        