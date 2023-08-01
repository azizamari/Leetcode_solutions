class Solution:
    def rob(self, nums: List[int]) -> int:
        memo={}
        def rob1(i):
            if i>=len(nums):
                return 0
            elif i ==len(nums)-1:
                return nums[i]
            else:
                if not i+2 in memo:
                    memo[i+2]=rob1(i+2)
                if not i+3 in memo:
                    memo[i+3]=rob1(i+3)
                return max(nums[i]+memo[i+2], nums[i+1]+memo[i+3])
        temp=nums.pop()
        x=rob1(0)
        memo={}
        nums=nums[1:]
        nums.append(temp)
        return max(x, rob1(0))