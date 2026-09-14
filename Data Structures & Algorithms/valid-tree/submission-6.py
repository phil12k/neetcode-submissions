class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = {i:[] for i in range(n)}
        visited = set()

        #fill the adj list
        for a , b in edges:
            adj[a].append(b)
            adj[b].append(a)

        def hasCycle(node,parent):
            if node in visited:
                return True

            visited.add(node)

            for neigh in adj[node]:
                if parent == neigh:
                    continue
                if hasCycle(neigh,node):
                    return True
            return False

        return not hasCycle(0,-1) and len(visited)==n
