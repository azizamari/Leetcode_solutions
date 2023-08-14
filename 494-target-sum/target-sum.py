class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        mem={}
        def ways(i, tot):
            if i == len(nums):
                return 1 if tot == target else 0
            elif not (i,tot) in mem:
                mem[(i,tot)]=ways(i+1, tot + nums[i])+ways(i+1, tot -nums[i])
                return mem[(i,tot)]
            else:
                return mem[(i,tot)]
        res=ways(0,0)
        print(mem)
        return res