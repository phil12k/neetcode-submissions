class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        row = len(heights)
        col = len(heights[0])

        pacific  = set()
        atlantic = set()

        def dfs(r,c,visited,prev):
            if r<0 or c<0 or r>=row or c>=col or heights[r][c]<prev or (r,c) in visited :
                return
            visited.add((r,c))
            dfs(r+1,c, visited , heights[r][c])
            dfs(r-1,c, visited , heights[r][c])
            dfs(r,c+1, visited , heights[r][c])
            dfs(r,c-1, visited , heights[r][c])

#pacific dfs 
        for r in range(row):
            dfs(r,0,pacific,heights[r][0])
        
        for c in range(col):
            dfs(0,c,pacific,heights[0][c])
#atlantic dfs
        for c in range(col):
            dfs(row-1,c ,atlantic,heights[row-1][c])
        
        for r in range(row):
            dfs(r,col-1 ,atlantic,heights[r][col-1])
        
        answer=[]
#vist the height grpah once
        for r in range(row):
            for c in range(col):
                if (r,c) in pacific and (r,c) in atlantic:
                    answer.append([r,c])
        return answer


