class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {i:[] for i in range(numCourses)}
        state = [0]*numCourses
        list = []

        for course, prep in prerequisites:
            adj[course].append(prep)
        
        def hasCycle(v):
            if state[v] == 1: return True
            if state[v] == 2: return False

            state[v]=1
            for neigh in adj[v]:
                if hasCycle(neigh):
                    return True
            state[v]=2
            list.append(v)
            return False

        for v in range(numCourses):
            if hasCycle(v):
                return []

        #for course, prep in prerequisites:
        #    list.append(prep)
        #    list.append(course)
        return list
