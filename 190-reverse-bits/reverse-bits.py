class Solution:
    def reverseBits(self, n: int) -> int:
        x=str(bin(n))[2:][::-1]
        x=x+(32-len(x))*'0'
        return int(x,2)