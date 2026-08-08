class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {i:[] for i in range(numCourses)}
        state = [0]*numCourses

        #fill the adjacency list
        for course, prep in prerequisites:
            adj[course].append(prep)

        def hasCycle(v):
            if state[v]==1:return True
            if state[v]==2:return False

            #state=1 means visiting node
            state[v] = 1 
            for neigh in adj[v]:
                if hasCycle(neigh):
                    return True

            
            #state=2 means visited node
            state[v] = 2 
            return False

        # check for cycles in cours
        for i in range(numCourses):
            if hasCycle(i): 
                return False
        return True
