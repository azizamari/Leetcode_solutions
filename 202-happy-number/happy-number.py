class Solution:
    def isHappy(self, n: int) -> bool:
        s=set()
        def ssum(ch):
            return sum([int(x)**2 for x in str(ch)])
        cur=n
        while cur!=1 and not cur in s:
            s.add(cur)
            cur=ssum(cur)
        return cur==1