# where am I
    # at some node in adjacency list
# what am I doing
    # I am going to take current node from queue, and then update children, and if children 0 I push to ready
    # then I push current to result
# what do I return 
    # boolean 

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # parent_count = 
        graph = self.build_graph(numCourses, prerequisites)
        num_parents = self.build_Parent(numCourses, prerequisites)

        # find the roots
        queue = deque([])
        for course in num_parents:
            if num_parents[course] == 0:
                queue.append(course)

        count = 0
        while queue:
            current = queue.popleft()

            for child in graph[current]:
                num_parents[child] -= 1
                if num_parents[child] == 0:
                    queue.append(child)
            count += 1
        return count == numCourses





    def build_graph(self, n, edges):
        graph = {}
        for i in range(n):
            graph[i] = []
        for edge in edges:
            a, b = edge
            graph[a].append(b)
        return graph

    def build_Parent(self, n, edges):
        count = {}
        for i in range(n):
            count[i] = 0
        for edge in edges:
            a, b = edge
            count[b] += 1
        return count


        