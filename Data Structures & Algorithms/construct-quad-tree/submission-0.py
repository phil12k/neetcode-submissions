"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val=False, isLeaf=False, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':

        n = len(grid)

        def dfs(r , c , size ) :

            val = grid[r][c]
            uniform = True

            for i in range(r, r + size ):
                for j in range(c , c + size):
                    if grid[i][j]!=val:
                        uniform = False
                        break
                    if not uniform:
                        break
            
            if uniform:
                return Node(bool(val), True)
            
            half = size // 2

            topLeft = dfs(r,c,half)
            topRight= dfs(r,c+half,half)
            bottomLeft= dfs(r+half,c,half)
            bottomRight= dfs(r+half,c+half,half)

            return Node(
                True, False,
                topLeft, topRight,
                bottomLeft, bottomRight
            )






        return dfs(0,0,n)
        
