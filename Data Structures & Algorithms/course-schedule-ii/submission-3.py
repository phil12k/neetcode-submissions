class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {i:[] for i in range(numCourses)}
        state=[0]*numCourses
        order=[]


        def hasCycle(i):
            if state[i]==1: return True
            if state[i]==2: return False

            state[i]=1
            for preq in adj[i]:
                if hasCycle(preq):
                    return True
            state[i]=2
            order.append(i)
            return False





        for course, preq in prerequisites:
            adj[course].append(preq)

        for i in range(numCourses):
            if hasCycle(i):
                return []
        return order
