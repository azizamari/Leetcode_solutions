class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums)==1: return True
        stack=[0]
        seen=set()
        seen.add(0)
        while len(stack)!=0:
            x=stack.pop()
            s=nums[x]
            while s>0:
                if not x+s in seen:
                    seen.add(x+s)
                    stack.append(x+s)
                    if x+s==len(nums)-1:return True
                s-=1
        return False
            