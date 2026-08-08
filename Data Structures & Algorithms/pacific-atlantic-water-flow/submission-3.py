class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        row = len(heights)
        col = len(heights[0])

        atlantic = set()
        pacific = set()

        def dfs(i,j,visited,prev):
            if i<0 or j<0 or i>=row or j>= col or (i,j) in visited or heights[i][j] < prev:
                return
            visited.add((i,j))
            dfs(i+1,j,visited,heights[i][j])
            dfs(i-1,j,visited,heights[i][j])
            dfs(i,j+1,visited,heights[i][j])
            dfs(i,j-1,visited,heights[i][j])

        #fill the grid for pacific
        for i in range(row):
            dfs(i,0,pacific, heights[i][0])
        for j in range(col):
            dfs(0,j,pacific, heights[0][j])
        #Fill the grid for atlantic 
        for i in range(row):
            dfs(i,col-1,atlantic,heights[i][col-1])
        for j in range(col):
            dfs(row-1,j,atlantic,heights[row-1][j])

        answer=[]
        # take intersection of pacific and atlantic visit
        for i in range(row):
            for j in range(col):
                if (i,j) in pacific and (i,j) in atlantic:
                    answer.append([i,j])
                    
        return answer