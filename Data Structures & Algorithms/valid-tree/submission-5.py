class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = {i:[] for i in range(n)}
        visited= set()

        for a , b in edges:
            adj[a].append(b)
            adj[b].append(a)



        def hasCycle(node, parent):
            # We found a node we've already visited -> cycle
            if node in visited:
                return True

            visited.add(node)

            for neigh in adj[node]:
                # Ignore the edge back to the parent
                if neigh == parent:
                    continue 

                # If another neighbor creates a cycle
                if hasCycle(neigh, node):
                    return True
            return False
              

        # Check both:
        # 1. No cycle
        # 2. Every node is connected
        return not hasCycle( 0, -1 ) and len(visited)==n