class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sub=nums[0]
        cur=0
        for n in nums:
            cur+=n
            max_sub=max(max_sub, cur)
            if cur<0:
                cur=0
        return max_sub