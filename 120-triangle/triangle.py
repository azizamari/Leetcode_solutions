class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp={}
        def solve(i,j):
            if i==n-1:
                return triangle[i][j]
            if (i,j) in dp:return dp[(i,j)]
            down=triangle[i][j]+solve(i+1,j)
            diagonal=triangle[i][j]+solve(i+1,j+1)
            dp[(i,j)] = min(down,diagonal)
            return dp[(i,j)]
        
        n=len(triangle)
        return solve(0,0)
