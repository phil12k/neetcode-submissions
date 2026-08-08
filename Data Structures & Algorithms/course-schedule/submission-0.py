class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {i:[] for i in range(numCourses)}
        state = [0]* numCourses


        for course, prep in prerequisites:
            adj[course].append(prep)

        def hasCycle(v):
            if state[v] ==1: return True
            if state[v] ==2: return False
            state[v] =1
            for neigh in adj[v]:
                if hasCycle(neigh): return True
            state[v] =2

        
        for i in range(numCourses):
            if hasCycle(i):
                return False
        return True
