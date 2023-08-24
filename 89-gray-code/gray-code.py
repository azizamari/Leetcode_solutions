class Solution:
    def grayCode(self, n: int) -> List[int]:
        def decimal_to_graycode(n):
            return n ^ (n >> 1)
        res=[]
        for i in range( 2**n):
            res.append(decimal_to_graycode(i))
        return res