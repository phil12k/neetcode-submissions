class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adj = {i:[] for i in range(numCourses)}
        indegree = [0]*numCourses

        

        #fill adj list
        for course, prep in prerequisites:
            adj[prep].append(course)
            indegree[course] +=1

        q=deque()
        completed =0
        #fill indegree list if it has no preq
        for course in range(numCourses):
            if indegree[course]==0:
                completed+=1
                q.append(course)

        while q:
            course = q.popleft()
            
            for neigh in adj[course]:
                indegree[neigh]-=1
                if indegree[neigh]==0:
                    q.append(neigh)
                    completed+=1

        return completed==numCourses


        

        