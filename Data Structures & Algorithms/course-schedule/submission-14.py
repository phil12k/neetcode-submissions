class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {i: [] for i in range(numCourses)}
        state = [0]*numCourses

        def hasCycle(i):
            if state[i]==1: return True
            if state[i]==2: return False
            state[i]=1
            for preq in adj[i]:
                if hasCycle(preq):
                    return True
            state[i]=2
            return False




        #fill adj list

        for course,prep in prerequisites:
            adj[course].append(prep)
            
        for i in range(numCourses):
            if hasCycle(i):
                return False
        return True