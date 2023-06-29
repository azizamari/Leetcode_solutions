class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:return 0
        c=set(nums)
        maxi=1
        for num in nums:
            if not num-1 in c:
                i=1
                while num+i in c: 
                    i+=1
                maxi=max(maxi,i) 
        return maxi



