class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        dp = [[0] * len(nums) for _ in range(len(nums))]
        for L in range(len(nums) - 2, 0, -1):
            for R in range(L, len(nums) - 1):
                for i in range(L, R+1):
                    coins = nums[L-1] * nums[i] * nums[R+1]
                    coins += dp[L][i-1] + dp[i+1][R]
                    dp[L][R] = max(dp[L][R], coins)
        
        return dp[1][len(nums) - 2]