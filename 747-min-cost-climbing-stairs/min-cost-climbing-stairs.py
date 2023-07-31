class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        self.dp={}
        def search(n):
            if len(cost)-n<=1: return 0
            else:
                if not n+1 in self.dp:
                    self.dp[n+1]=search(n+1)
                if not n+2 in self.dp:
                    self.dp[n+2]=search(n+2)
                return min(cost[n]+self.dp[n+1], cost[n+1]+self.dp[n+2])
        return search(0)