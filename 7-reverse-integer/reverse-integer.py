class Solution:
    def reverse(self, x: int) -> int:
        a=abs(x)
        sign=(1 - 2*(x < 0))
        res=str(a)[::-1]
        res=res.rjust(10,'0')
        if res>'2147483647':return 0
        return int(res)*sign