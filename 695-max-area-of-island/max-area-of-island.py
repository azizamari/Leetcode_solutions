class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.m=len(grid)
        self.n=len(grid[0])
        def explore(i,j):
            if i<0 or i>= self.m or j<0 or j>=self.n or grid[i][j]==0:
                return 0
            else:
                grid[i][j]=0
                return 1+ explore(i+1,j) + explore(i,j+1) + explore(i,j-1) + explore(i-1,j)
        c=0
        for x in range(self.m):
            for y in range(self.n):
                print(x,y)
                if grid[x][y]==1:
                    c=max(c,explore(x,y))
        return c