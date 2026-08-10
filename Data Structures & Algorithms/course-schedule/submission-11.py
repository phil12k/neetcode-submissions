class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {i:[] for i in range(numCourses)}
        state = [0]*numCourses

        #fill the list
        for course, prep in prerequisites:
            adj[course].append(prep)

        def hasCycle(i):
            if state[i]==1: return True
            if state[i]==2: return False

            state[i]=1
            for prep in adj[i]:
                if hasCycle(prep):
                    return True
            state[i]=2
            return False
            

        for i in range(numCourses):
            if hasCycle(i):
                return False
        return True
