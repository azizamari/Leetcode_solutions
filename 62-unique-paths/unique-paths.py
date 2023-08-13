class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp=[[0]*(n+1) for _ in range(m+1)]
        dp[1][1]=1
        for i in range(m+1):
            for j in range(n+1):
                if j+1 <= n:
                    dp[i][j+1]+=dp[i][j]
                if i+1 <= m:
                    dp[i+1][j]+=dp[i][j]
        return dp[m][n]