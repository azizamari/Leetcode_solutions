class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        dp={}
        output=[]
        for j in range(len(nums)):
            num=nums[j]
            if num in dp:
                output.append(dp[num])
            else: 
                x=1
                for i in range(len(nums)):
                    if i!=j: x*=nums[i]
                output.append(x)
                dp[num]=x
        return output