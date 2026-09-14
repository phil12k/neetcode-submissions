class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {i:[] for i in range(n)}
        count = 0
        visited = set()

        #fill the list
        for a , b in edges:
            adj[a].append(b)
            adj[b].append(a)

        def dfs(node):
            visited.add(node)
            for neigh in adj[node]:
                if neigh not in visited:
                    dfs(neigh)

        
        for i in range(n):
            if i not in visited:
                count +=1
                dfs(i)
        return count