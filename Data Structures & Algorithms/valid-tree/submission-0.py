class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
                # Build adjacency list
        graph = {i: [] for i in range(n)}

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited = set()

        def dfs(node, parent):
            # We found a node we've already visited -> cycle
            if node in visited:
                return False

            visited.add(node)

            for neighbor in graph[node]:
                # Ignore the edge back to the parent
                if neighbor == parent:
                    continue

                # If another neighbor creates a cycle
                if not dfs(neighbor, node):
                    return False

            return True

        # Check both:
        # 1. No cycle
        # 2. Every node is connected
        return dfs(0, -1) and len(visited) == n