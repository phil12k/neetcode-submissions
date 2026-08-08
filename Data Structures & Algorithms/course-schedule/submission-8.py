class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #create adj list
        adj = {i:[] for i in range(numCourses)}
        state = [0]*numCourses

        #fill the list
        for course, prep in prerequisites:
            adj[course].append(prep)

        #check for cycle
        def hasCycle(v):
            if state[v]==1: return True
            if state[v]==2: return False
            
            state[v]=1
            #check if adj list is connect to other course
            for course in adj[v]:
                if hasCycle(course):
                    return True
            state[v]=2
            return False


#check for cycle in adj list
        for i in range(numCourses):
            if hasCycle(i):
                return False
        return True

        