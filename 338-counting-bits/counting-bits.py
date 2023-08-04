class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)
        step = 1
        for i in range(1, n + 1):
            if step * 2 == i:
                step = i
            dp[i] = 1 + dp[i - step]
        return dp