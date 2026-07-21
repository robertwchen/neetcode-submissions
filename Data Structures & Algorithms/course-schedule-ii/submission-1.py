class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = self.build_graph(numCourses, prerequisites)
        num_parents = self.build_parents(prerequisites)

        queue = deque([])
        for course in num_parents:
            if num_parents[course] == 0:
                queue.append(course)

        result = []
        while queue:
            course = queue.popleft()
            
            for child in graph[course]:
                num_parents[child] -= 1
                if num_parents[child] == 0:
                    queue.append(child)
            result.append(course)

        if len(result) != len(num_parents):
            return []

        for course in graph:
            if course not in num_parents:
                result.append(course)
        return result



    def build_graph(self, n, edges):
        graph = {}
        for i in range(n):
            graph[i] = []
        for edge in edges:
            a, b = edge
            graph[b].append(a)
        return graph
    def build_parents(self, edges):
        graph = {}
        for edge in edges:
            a, b = edge
            if a not in graph:
                graph[a] = 0
            if b not in graph:
                graph[b] = 0
            graph[a] += 1
        return graph
        
        