class Solution:
    def numTrees(self, n: int) -> int:
        dp=[1]*(n+1)
        for i in range(2,n+1):
            tot=0
            for root in range(1,i+1):
                tot+=dp[root-1]*dp[i-root]
            dp[i]=tot
        return dp[n]
