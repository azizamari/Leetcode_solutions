class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        x=sum(nums)
        if x %2!=0:
            return False
        def subset_sum(arr, target):
            n = len(arr)
            dp = [[False for _ in range(target + 1)] for _ in range(n + 1)]

            for i in range(n + 1):
                dp[i][0] = True

            for i in range(1, n + 1):
                for j in range(1, target + 1):
                    if j < arr[i - 1]:
                        dp[i][j] = dp[i - 1][j]
                    else:
                        dp[i][j] = dp[i - 1][j] or dp[i - 1][j - arr[i - 1]]

            return dp[n][target]
        return subset_sum(nums,x//2)
        