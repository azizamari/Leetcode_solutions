class Solution:
    def climbStairs(self, n: int) -> int:
        self.memo={}
        def counting(n):
            if n==0 or n==1: 
                return 1
            if not n in self.memo:
                self.memo[n]=counting(n-1)+counting(n-2)
            return self.memo[n]
        return counting(n)