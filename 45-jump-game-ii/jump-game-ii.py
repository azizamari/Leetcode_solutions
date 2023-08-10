class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps=0
        i=0
        pos=len(nums)-1
        while pos!=0:
            if i+nums[i]>=pos:
                pos=i
                i=0
                jumps+=1
            else:
                i+=1
        return jumps