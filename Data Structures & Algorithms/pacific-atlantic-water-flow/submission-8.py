class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        row = len(heights)
        col = len(heights[0])

        pac = set()
        atl = set()

        def dfs(i,j,visited,prev):
            if i<0 or j<0 or i>=row or j>=col or heights[i][j]<prev or (i,j) in visited :
                return
            visited.add((i,j))
            dfs(i+1,j,visited,heights[i][j])
            dfs(i-1,j,visited,heights[i][j])
            dfs(i,j+1,visited,heights[i][j])
            dfs(i,j-1,visited,heights[i][j])

        #fill the grid from pacific borders
        for i in range(row):
            dfs(i,0,pac,heights[i][0])

        for j in range(col):
            dfs(0,j,pac,heights[0][j])

        #fill the grid from atlantic borders
        for i in range(row):
            dfs(i,col-1,atl,heights[i][col-1])
        
        for j in range(col):
            dfs(row-1,j,atl,heights[row-1][j])

        ans = []
        
        for i in range(row):
            for j in range(col):
                if (i,j) in pac and (i,j) in atl:
                    ans.append([i,j])
        return ans
                    
            