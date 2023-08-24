class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        memo={}
        self.m=len(grid)
        self.n=len(grid[0])
        def recurse(i,j):
            if i==self.m-1 and j==self.n-1:
                return grid[i][j]
            elif (i,j) in memo: return memo[(i,j)]
            elif i>=self.m or j>=self.n:
                return float('inf')
            else:
                memo[(i,j)]=min(recurse(i,j+1),recurse(i+1,j))+grid[i][j]
            return memo[(i,j)]

        return recurse(0,0)
