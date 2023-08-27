# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left=0
        right=n-1
        while left<=right:
            mid=(left+right)//2
            if isBadVersion(mid+1):
                if left==right: return mid+1
                right=mid
            else:
                left=mid+1