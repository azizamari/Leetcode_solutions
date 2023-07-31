class Solution:
    def rob(self, nums: List[int]) -> int:
        memo={}
        def get_res(i):
            if i>=len(nums):
                return 0
            elif i ==len(nums)-1:
                return nums[i]
            else:
                if not i+2 in memo:
                    memo[i+2]=get_res(i+2)
                if not i+3 in memo:
                    memo[i+3]=get_res(i+3)
                return max(nums[i]+memo[i+2], nums[i+1]+memo[i+3])
        return get_res(0)
